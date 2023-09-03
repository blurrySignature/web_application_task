#!/bin/bash

docker run --rm -d \
	--hostname $(hostname) \
	-p 8000:8000 \
	--name app \
	web_application:latest
