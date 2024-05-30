from icmplib import ping
import json
import os
import time
import requests

with open('config.json') as fd:
    json_data = json.load(fd)

def icmp(hostname: str):
    host = ping(hostname, count=5, interval=0.2)
    return host.packets_sent == host.packets_received

def http(hostname: str):
    try:
        r = requests.head(hostname)
        return str(r.status_code)
    except:
        return False

with open('uptime.json', 'r') as f:
    uptimeFile = json.load(f)

interval = json_data['interval']
debug = int(json_data['debug'])

def uptime():
    for i in json_data['hosts']:
        if json_data['hosts'][i]['monitor_type'] == "icmp":
            if debug == 1 or debug == 2:
                print(json_data['hosts'][i]['address'])
            host = json_data['hosts'][i]['address']

            try:
                if icmp(host):
                    if debug == 1 or debug == 2:
                        print("UP")
                    uptimeFile['hosts'][i] = (f"UP")
            except Exception as e:
                if debug == 1:
                    print("DOWN")
                if debug == 2:
                    print("DOWN - Error :", e)
                uptimeFile['hosts'][i] = (f"DOWN")

            os.remove('uptime.json')
            with open('uptime.json', 'w') as f:
                json.dump(uptimeFile, f, indent=4)


        elif json_data['hosts'][i]['monitor_type'] == "http":
            if debug == 1 or debug == 2:
                print(json_data['hosts'][i]['address'])
            host = json_data['hosts'][i]['address']
            expResp = json_data['hosts'][i]['HERC']

            respCode = http(host)

            try:
                if respCode in expResp:
                    if debug == 1:
                        print("UP")
                    if debug == 2:
                        print("UP",respCode)
                    uptimeFile['hosts'][i] = (f"UP")
                else:
                    if debug == 1:
                        print("DOWN")
                    if debug == 2:
                        print("DOWN",respCode)
                    uptimeFile['hosts'][i] = (f"DOWN")
            except Exception as e:
                if debug == 1:
                    print("DOWN")
                if debug == 2:
                    print("DOWN - Error :", e)
                uptimeFile['hosts'][i] = (f"DOWN")

            os.remove('uptime.json')
            with open('uptime.json', 'w') as f:
                json.dump(uptimeFile, f, indent=4)

while True:
    uptime();
    if debug == 1 or debug == 2:
        print(f"Waiting for {interval} seconds")
    time.sleep(int(interval))