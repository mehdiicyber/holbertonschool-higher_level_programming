#!/bin/bash
#
curl -sI -X OPTIONS "$1" | grep -i "Allow" | cut -d ' ' -f 2- | tr -d '\r'
