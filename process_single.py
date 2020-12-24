import requests
import pandas as pd
import bs4
import get_proxies


def process_single(journal_code,journal_name):
    print('开启{}摘要获取'.format(journal_name))
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36",
        "Cookie": "Ecp_ClientId=5200923201802479718; cnkiUserKey=08db5bf3-a428-1986-5443-01d3939c06d5; UM_distinctid=17510f3831c3fd-01727c365eb93-c781f38-1aeaa0-17510f3831d9af; Ecp_ClientIp=183.173.62.190; Hm_lvt_07a576e0f1481e3cafe74b0eb336a2d7=1607681841; CNZZDATA4207386=cnzz_eid%3D907857934-1607677914-https%253A%252F%252Fwap.cnki.net%252F%26ntime%3D1607677914; _pk_ref=%5B%22%22%2C%22%22%2C1608629062%2C%22https%3A%2F%2Fkns.cnki.net%2Fkns8%2Fdefaultresult%2Findex%22%5D; _pk_id=c31eb566-e2d6-4723-99f8-6d598c45e4c2.1607604239.30.1608629062.1608629062.; Ecp_IpLoginFail=20122258.200.129.230; amid=4d4ca51d-d27d-4e90-bc30-397136aeff41; E7F38EA2E837979238D6F8CFF3FB9516=9871D3A2C554B27151CACF1422EEC048=&4040592CEC1880AA70936989F05E7C31=&2D53A8FB7ABF5BE7F4A3CF4B565CC75C="
    }
    url='https://wap.cnki.net/touch/web/Journal/Article/'+journal_code
    num_journals=30
    num_seasons=24
    num_years=[a for a in range(2010,2020)]
    proxies=get_proxies.get_proxy_ip()


    for num_year in num_years:
        for num_season in range(1,num_seasons):
            for num_journal in range(1,num_journals):
                temp_url=url+str(num_year)+str(num_season).zfill(2)+str(num_journal).zfill(3)+'.html'
                try:
                    response=requests.get(url=temp_url,headers=headers,proxies=proxies,timeout=10)
                    if response.status_code == 200:
                        response.encoding = 'utf-8'
                        text = bs4.BeautifulSoup(response.content, 'html.parser')
                        abstract = text.find('div', class_='c-card__aritcle')
                        temp = pd.Series(abstract.text)
                        abstract = pd.DataFrame([temp])
                        abstract.to_csv('./data/abstract{}.csv'.format(num_year), header=None, mode='a',
                                        encoding='utf-8-sig')
                        print('写入{}第{}年的第{}刊的第{}篇文献'.format(journal_name,num_year, num_season, num_journal))
                    else:
                        print('未找到{}第{}年的第{}刊的第{}篇文献'.format(journal_name,num_year, num_season, num_journal))
                        continue
                except:
                    print('网络不通')
                    proxies=get_proxies.get_proxy_ip()
                    try:
                        response = requests.get(url=temp_url, headers=headers, proxies=proxies, timeout=10)
                        if response.status_code == 200:
                            response.encoding = 'utf-8'
                            text = bs4.BeautifulSoup(response.content, 'html.parser')
                            abstract = text.find('div', class_='c-card__aritcle')
                            temp = pd.Series(abstract.text)
                            abstract = pd.DataFrame([temp])
                            abstract.to_csv('./data/abstract{}.csv'.format(num_year), header=None, mode='a',
                                            encoding='utf-8-sig')
                            print('写入{}第{}年的第{}刊的第{}篇文献'.format(journal_name,num_year, num_season, num_journal))
                        else:
                            print('未找到{}第{}年的第{}刊的第{}篇文献'.format(journal_name,num_year, num_season, num_journal))
                            continue
                    except:
                        print('网络不通')
                        proxies = get_proxies.get_proxy_ip()
                        try:
                            response = requests.get(url=temp_url, headers=headers, proxies=proxies, timeout=10)
                            if response.status_code == 200:
                                response.encoding = 'utf-8'
                                text = bs4.BeautifulSoup(response.content, 'html.parser')
                                abstract = text.find('div', class_='c-card__aritcle')
                                temp = pd.Series(abstract.text)
                                abstract = pd.DataFrame([temp])
                                abstract.to_csv('./data/abstract{}.csv'.format(num_year), header=None, mode='a',encoding='utf-8-sig')
                                print('写入{}第{}年的第{}刊的第{}篇文献'.format(journal_name,num_year, num_season, num_journal))
                            else:
                                print('未找到{}第{}年的第{}刊的第{}篇文献'.format(journal_name,num_year, num_season, num_journal))
                                continue
                        except:
                            print('无法连接网络，自动退出程序')
                            continue





#   https://wap.cnki.net/touch/web/Journal/Article/ZGDC201001002.html