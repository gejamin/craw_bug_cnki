import requests
import time
def get_proxy_ip():
    import requests

    # 提取代理API接口，获取1个代理IP
    api_url = "http://dps.kdlapi.com/api/getdps/?orderid=960828771175085&num=1&pt=1&format=json&sep=1"

    # 获取API接口返回的代理IP
    try:
        proxy_ip = requests.get(api_url).text
        import json
        data = json.loads(proxy_ip)

        # 白名单方式（需提前设置白名单）
        proxies = {
            "http": "http://" + data['data']['proxy_list'][0],
            "https": "http://" + data['data']['proxy_list'][0]
        }
    except:
        time.sleep(1)
        try:
            proxy_ip = requests.get(api_url).text
            import json
            data = json.loads(proxy_ip)

            # 白名单方式（需提前设置白名单）
            proxies = {
                "http": "http://" + data['data']['proxy_list'][0],
                "https": "http://" + data['data']['proxy_list'][0]
            }
        except:
            time.sleep(1)
            try:
                proxy_ip = requests.get(api_url).text
                import json
                data = json.loads(proxy_ip)

                # 白名单方式（需提前设置白名单）
                proxies = {
                    "http": "http://" + data['data']['proxy_list'][0],
                    "https": "http://" + data['data']['proxy_list'][0]
                }
            except:
                time.sleep(1)
                try:
                    proxy_ip = requests.get(api_url).text
                    import json
                    data = json.loads(proxy_ip)

                    # 白名单方式（需提前设置白名单）
                    proxies = {
                        "http": "http://" + data['data']['proxy_list'][0],
                        "https": "http://" + data['data']['proxy_list'][0]
                    }
                except:
                    pass

    print('更换ip: {}'.format(data['data']['proxy_list'][0]))
    return proxies