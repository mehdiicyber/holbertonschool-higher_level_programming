#!/bin/bash
# Verilən URL-ə sorğu göndərir və gələn cavabın daxili ölçüsünü (body size) bayt ilə göstərir.
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'
