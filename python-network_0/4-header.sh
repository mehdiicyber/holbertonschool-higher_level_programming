#!/bin/bash
# URL-ə xüsusi başlıq (Header) ilə GET sorğusu göndərir və cavabı göstərir
curl -sH "X-School-User-Id: 98" "$1"
