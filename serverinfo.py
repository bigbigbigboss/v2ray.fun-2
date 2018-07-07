#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import urllib2
import base64
import os
import json
#获取本机IP地址
myip = urllib2.urlopen('http://api.ipify.org').read()
myip = myip.strip()

#判断传输配置
mystreamnetwork=str(readjson.ConfStreamNetwork)

if readjson.ConfStreamNetwork=="kcp" :
    if(readjson.ConfStreamHeader=="utp"):
        mystreamnetwork="mKCP 伪装 BT下载流量"
    elif(readjson.ConfStreamHeader=="srtp"):
        mystreamnetwork="mKCP 伪装 FaceTime通话"
    elif(readjson.ConfStreamHeader=="wechat-video"):
        mystreamnetwork="mKCP 伪装 微信视频流量"
    else:
        mystreamnetwork="mKCP"
elif readjson.ConfStreamNetwork=="http":
    mystreamnetwork="HTTP伪装"
elif readjson.ConfStreamNetwork=="ws":
    mystreamnetwork="WebSocket"

if (readjson.ConfStreamSecurity=="tls"):
    mystreamsecurity="TLS：开启"
else:
    mystreamsecurity="TLS：关闭"

#输出信息
print("服务器IP：%s") % str(myip)
print("主端口：%s") % str(readjson.ConfPort)
print("UUID：%s") % str(readjson.ConfUUID)
print("alter ID: %s") % str(readjson.ConfAlterId)
print("加密方式：%s") % str(readjson.ConfSecurity)
print("传输方式：%s") % str(mystreamnetwork)
if readjson.ConfigDynPortRange:
    print("动态端口范围:%s") % str(readjson.ConfigDynPortRange)
else:
    print("动态端口:禁止")

config = {
    "v": "2",
    "ps": "v2rayN & v2rayNG 2.0 config",
    "add": "",
    "port": "",
    "id": "",
    "aid": "",
    "net": "",
    "type": "none",
    "host": "",
    "path": "/",
    "tls": "",
}

config["add"] = str(myip)
config["port"] = str(readjson.ConfPort)
config["id"] = str(readjson.ConfUUID)
config["aid"] = str(readjson.ConfAlterId)
config["net"] = str(mystreamnetwork)

if mystreamnetwork == "kcp":
    config["type"] = str(readjson.ConfStreamHeader)

if (readjson.ConfSecurity == "tls"):
    config["tls"] = "tls"

# config["host"] = str(readjson.ConfPath)

base64Str = base64.encodestring(json.dumps(config))
base64Str = ''.join(base64Str.split())
vmessurl="vmess://"+base64Str
#green show
print("\033[32m")
print("%s") % vmessurl
print("\033[0m")
os.system("qrcode -w 200 -o ~/config_v2rayN.png "+ vmessurl)

mystreamnetwork=str(readjson.ConfStreamNetwork)

if readjson.ConfStreamNetwork=="http":
    mystreamnetwork="http"
elif readjson.ConfStreamNetwork=="ws":
    mystreamnetwork="websocket"
else:
    mystreamnetwork="none"

base64Str=base64.urlsafe_b64encode(str(readjson.ConfSecurity)+":"+str(readjson.ConfUUID)+"@"+str(myip)+":"+str(readjson.ConfPort))
vmessurl="vmess://"+base64Str+"?obfs="+str(mystreamnetwork)
print("\033[32m")
print("%s") % vmessurl
print("\033[0m")
os.system("qrcode -w 200 -o ~/config_pepi.png "+ vmessurl)
