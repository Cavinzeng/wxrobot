import requests
from tool import *
from bs4 import BeautifulSoup
def getcoinprice(coin):
    url = 'https://www.mytokencap.com/search?keyword={}&category=all'.format(coin)
    raw_headers='''
    GET /search?keyword=kjasd&category=all HTTP/1.1
    Host: www.mytokencap.com
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
    '''
    fun,headers = str2header(raw_headers)
    r = requests.get(url,headers=headers,verify=False,timeout=30)
    # print(r.text)
    soup  = BeautifulSoup(r.text,'lxml')
    try:
        price = soup.find_all('div',attrs={'class':"price mt-green"})[0].text[3:].strip()
        change = soup.find_all('div',attrs={'class':"percent percent-up"})[0]
        changeprice=change.find_all('span')[0].text
        changepercent = change.find_all('span')[1].text.strip()
        # print(price,changeprice,changepercent)
        return price,changeprice,changepercent
    except:
        raise ValueError('获取失败')
if __name__ == '__main__':
    getcoinprice('eth')
