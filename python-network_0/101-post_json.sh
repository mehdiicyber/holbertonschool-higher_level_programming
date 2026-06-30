#!/bin/bash
# URL-ə fayldan oxunan JSON POST sorğusu göndərir və cavabı göstərir
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
