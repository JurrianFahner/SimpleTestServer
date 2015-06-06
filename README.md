# SimpleTestServer
This repository contains a simple test server written in python for testing purposes. This server runs on port 8080 by default.

[Web.py](http://webpy.org) is embedded, to avoid broken repositories. 

To use this simple server on a linux environment it is as easy as:
```bash
python start.py
```

It can also be used to build a docker image:
```bash
docker build -t sts https://github.com/JurrianFahner/SimpleTestServer
docker run -d -p 8080:8080 sts python start.py
```
If hostname is not set on docker run, then the docker id will be shown as hostname of that specfic container.