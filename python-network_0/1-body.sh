#!/bin/bash
# URL-ə GET sorğusu göndərir və yalnız 200 status kodu olduqda gövdəni göstərir
curl -sL -f "$1"
