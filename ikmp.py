from icmplib import ping
import json
import os
import time


with open('/etc/ikmp/config.json') as fd:
    json_data = json.load(fd)

def host_up(hostname: str):
    host = ping(hostname, count=5, interval=0.2)
    return host.packets_senXt == host.packets_received


with open('/etc/ikmp/uptime.json', 'r') as f:
    uptimeFile = json.load(f)

interval = json_data['interval']
debug = int(json_data['debug'])

def uptime():
    for i in json_data['hosts']:
        if debug == 1 or debug == 2:
            print(json_data['hosts'][i]['address'])
        host = json_data['hosts'][i]['address']

        try:
            if host_up(host):
                if debug == 1 or debug == 2:
                    print("UP")
                uptimeFile['hosts'][i] = (f"UP")
        except Exception as e:
            if debug == 1:
                print("DOWN")
            if debug == 2:
                print("DOWN - Error :",e)
            uptimeFile['hosts'][i] = (f"DOWN")

        os.remove('/etc/ikmp/uptime.json')
        with open('/etc/ikmp/uptime.json', 'w') as f:
            json.dump(uptimeFile, f, indent=4)

while True:
    uptime();
    if debug == 1 or debug == 2:
        print(f"Waiting for {interval} seconds")
    time.sleep(int(interval))