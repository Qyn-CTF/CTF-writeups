# authy - 178 solves (150 points)
## Description
```
Check out this new storage application that your government has started! It's supposed to be pretty secure since everything is authenticated...

curl crypto.chal.csaw.io:5003
```

## First looks
Were given the source of the running application `handout.py`.  
We can quickly see that this is just some API, hashing our input and handing it back to us. With another option allowing us to view/verify that the signature is correct.  


## Crypto
When we post some data to `/new`, the `note` is converted from `JSON` to a representation of `form` data:
```python
info = {"admin": "False", "access_sensitive": "False" }
info.update(payload)
info["entrynum"] = 783

infostr = ""
for pos, (key, val) in enumerate(info.items()):
    infostr += "{}={}".format(key, val)
    if pos != (len(info) - 1):
        infostr += "&"
```
There's already a bug here, since the this: `infostr += "{}={}".format(key, val)` doesn't `URL encode` our payload, so we can set our note to something like: `note&admin=True`, which would work, but we can't modify the `entrynum` since it's set afterwards and I don't think there is a way to escape it somehow.  
After this conversion, the actual vulnerable part happens:
```python
infostr = infostr.encode()

identifier = base64.b64encode(infostr).decode()

hasher = hashlib.sha1()
hasher.update(SECRET + infostr)
return "Successfully added {}:{}\n".format(identifier, hasher.hexdigest())
```
Here we can see that the `sha1` hash is taken of `SECRET|infostr`, where `infostr` is the `form` like data (`sha1(SECRET || infostr)`). This is just a simple `length extension attack`.  
Continuing to the `/view` endpoint, we see it takes the `id` (`identifier`) and the `hash` in order to verify it was right:  
```python
identifier = base64.b64decode(info["id"]).decode()
checksum = info["integrity"]

params = identifier.replace('&', ' ').split(" ")
note_dict = { param.split("=")[0]: param.split("=")[1]  for param in params }

encode = base64.b64decode(info["id"]).decode('unicode-escape').encode('ISO-8859-1')
hasher = hashlib.sha1()
hasher.update(SECRET + encode)
gen_checksum = hasher.hexdigest()
```
Here we see that if you have a string such as: `admin=False&access_sensitive=False&note=someNote&admin=True&access_sensitive=True&author=me&entrynum=783` that the latest entry is chosen, so instead of `admin=False`, the later `admin=True` is used.  
And if the `entrynum`, previously set to `783` is equal to `7`, the `admin` is set to `True` and the `access_sensitive` is set to `True`, we get the flag:  
```python
entrynum = int(note_dict["entrynum"])
if 0 <= entrynum <= 10:

    if (note_dict["admin"] not in [True, "True"]):
        return ">:(\n"
    if (note_dict["access_sensitive"] not in [True, "True"]):
        return ">:(\n"

    if (entrynum == 7):
        return "\nAuthor: admin\nNote: You disobeyed our rules, but here's the note: " + FLAG + "\n\n"
    else:
        return "Hmmmmm...."

else:
    return """\nAuthor: {}
Note: {}\n\n""".format(note_dict["author"], note_dict["note"])
```
We previously found out we can just set the `admin` and `access_sensitive` to `True`, but we now need to set the `entrynum` to `7` as well.  
For this, I'm going to use some tool called `HashPump` since it has `Python` bindings for it. 
Such a length extension attack allows us to append data to the given data, so let's say for example from `/new` we get:  
`admin=False&access_sensitive=False&note=someNote&admin=True&access_sensitive=True&author=me&entrynum=783`, would result in:  
`admin=False&access_sensitive=False&note=someNote&admin=True&access_sensitive=True&author=me&entrynum=783{RANDOMDATA}{CONTROLLED DATA}`  
While still giving a correct hash. We can quickly implement something like this:
```python
import hashpumpy
inputId = "admin=False&access_sensitive=False&note=someNote&admin=True&access_sensitive=True&author=me&entrynum=783"
inputHash = "2dff57726cd588741d73c554d0eb4e1ebb0d9b32"

result = hashpumpy.hashpump(inputHash, inputId, '&admin=True&entrynum=7&access_sensitive=True', 13) #Derrived length of just trying
print(result[0]) # df20c11894172bbc5bcc0a3da2c5e723a35c553d
print(result[1]) #b'admin=False&access_sensitive=False&note=someNote&admin=True&access_sensitive=True&author=me&entrynum=783\x80\x00\x00\x00\x00\x00\x00\x00\x00\x03\xa8&admin=True&entrynum=7&access_sensitive=True'
```
*NOTE that the `13` is the `key length`, which we can just try until we succeed*
Also, I obviously don't need the extra `admin=True` in the appended data, but if you didn't catch the first bug, this would work too.  
However, just base64 encoding this and sending it to the `/view` doesn't work as it first runs `.decode()` on it and the 0x80 character is not a valid `UTF8` character.  
But we can also see that it doesn't use that value to call the `sha1(SECRET || identifier)` on it:  
```python
identifier = base64.b64decode(info["id"]).decode()
checksum = info["integrity"]
...

encode = base64.b64decode(info["id"]).decode('unicode-escape').encode('ISO-8859-1')
hasher = hashlib.sha1()
hasher.update(SECRET + encode)
```
Instead it takes the `info["id"]`, decodes it as base64, decodes it again with `unicode-escape` and then encodes it with `ISO-8859-1` and then uses that to do the `sha1` operation.  
It turns out, if we do that in reverse on our previous script that it generates normal `UTF8` characters (because of the `unicode-escape`) ->
```python
...
result = hashpumpy.hashpump(inputHash, inputId, '&admin=True&entrynum=7&access_sensitive=True', 13) #Derrived length of just trying
...
print(result[1].decode("ISO-8859-1").encode('unicode-escape')) #b'admin=False&access_sensitive=False&note=someNote&admin=True&access_sensitive=True&author=me&entrynum=783\\x80\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x03\\xa8&admin=True&entrynum=7&access_sensitive=True'
```
And `base64` encoding this and sending it to `/view` together with the new hash generated by `HashPump`, we get the flag.  
Final script:
```python
import hashpumpy
from base64 import b64encode
import requests

inputId = "admin=False&access_sensitive=False&note=someNote&admin=True&access_sensitive=True&author=me&entrynum=783"
inputHash = "2dff57726cd588741d73c554d0eb4e1ebb0d9b32"

for i in range(2, 20):
    try:
        print(f"Doing {i}/19")
        result = hashpumpy.hashpump(inputHash, inputId, '&admin=True&entrynum=7&access_sensitive=True', i)
        resultIdentifier = b64encode(result[1].decode("ISO-8859-1").encode('unicode-escape')).decode()

        r = requests.post('http://crypto.chal.csaw.io:5003/view', data={'id': resultIdentifier, 'integrity':result[0]}, headers={"Content-Type":"application/x-www-form-urlencoded"})

        if "disobeyed our rules" in r.text:
            print(r.text)
            break
    except:
        pass
``` 
`flag{h4ck_th3_h4sh}`