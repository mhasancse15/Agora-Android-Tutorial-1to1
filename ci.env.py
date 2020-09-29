#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os


def main():
    f = open("./app/build.gradle", 'r+')
    content = f.read()
    sdkver = ""
    if "AGORA_RTC_SDK_VER" in os.environ:
      sdkver = os.environ["AGORA_RTC_SDK_VER"]
    x = re.sub(
        r'(dependencies {$)(.*)', r"\1\n    implementation 'io.agora.rtc:full-sdk:"+sdkver+r"'\2", content, flags=re.M)
    f.seek(0)
    f.write(x)
    f.truncate()

    appId = ""
    if "AGORA_APP_ID" in os.environ:
        appId = os.environ["AGORA_APP_ID"]
    token = ""

    f = open("./app/src/main/res/values/strings.xml", 'r+')
    content = f.read()
    contentNew = re.sub(r'<#YOUR APP ID#>', appId, content)
    contentNew = re.sub(r'<#YOUR ACCESS TOKEN#>', token, contentNew)
    f.seek(0)
    f.write(contentNew)
    f.truncate()


if __name__ == "__main__":
    main()