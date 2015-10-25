![build travis cli](https://api.travis-ci.org/JurrianFahner/SimpleTestServer.svg?branch=master)
# SimpleTestServer
This repository contains a simple test server written in python for testing purposes. This server runs on port 8080 by default.

To use this simple server on a linux environment it is as easy as (after cloning this repository):
```bash
python start.py
```

It can also be used to build a docker image:
```bash
docker build -t sts https://github.com/JurrianFahner/SimpleTestServer.git
docker run -d -p 8080:8080 sts
```
If hostname is not set on docker run, then the docker id will be shown as hostname of that specfic container.

The docker image can also be pulled from dockerhub, by issuing the following command:
```bash
docker run -p 8080:8080 --hostname hostname -d ensignprojects/sts
```