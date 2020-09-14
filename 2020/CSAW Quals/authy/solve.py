import hashpumpy
from base64 import b64encode
import requests

inputId = "admin=False&access_sensitive=False&note=someNote&admin=True&access_sensitive=True&author=me&entrynum=783"
inputHash = "2dff57726cd588741d73c554d0eb4e1ebb0d9b32"

for i in range(2, 20):
    try:
        print(f"Doing {i}/19")
        result = hashpumpy.hashpump(
            inputHash, inputId, '&admin=True&entrynum=7&access_sensitive=True', i)
            
        resultIdentifier = b64encode(result[1].decode(
            "ISO-8859-1").encode('unicode-escape')).decode()

        r = requests.post('http://crypto.chal.csaw.io:5003/view',
                          data={'id': resultIdentifier,
                                'integrity': result[0]},
                          headers={"Content-Type": "application/x-www-form-urlencoded"})

        if "disobeyed our rules" in r.text:
            print(r.text)
            break
    except:
        pass
