import requests
def check_http(url,proxies):
    response=requests.get(url,proxies=proxies,timeout=20)
    if response.status_code==200:
        status=1
    else:
        status=0
    return status

