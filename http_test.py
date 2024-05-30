import urllib.request

def http(hostname: str):
    resp_code = urllib.request.urlopen(hostname).getcode()
    return resp_code