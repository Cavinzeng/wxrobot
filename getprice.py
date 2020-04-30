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
    soup  = BeautifulSoup(r.text,'html.parser')
    try:
        first = soup.find_all('a',attrs={'class':'coin-name'})[0]
        # print(first)
        trueurl='https://www.mytokencap.com'+first.get('href')
        # print(trueurl)
        r = requests.get(trueurl, headers=headers, verify=False, timeout=30)
        soup1 = BeautifulSoup(r.text, 'html.parser')
        priceinfo = soup1.find_all('div', attrs={'class': "price-wrapper wrapper-left"})[0].find_all('div')
        # print(priceinfo)
        price=priceinfo[0].text[5:].replace(" ","").strip()
        change=priceinfo[1]
        changeprice=change.find_all('span')[0].text.replace(" ","").replace('\n','')
        changepercent = change.find_all('span')[1].text.strip()
        usdprice = priceinfo[2].text.replace(" ","").strip()
        print(usdprice)
        # print(price,changeprice,changepercent)
        return price,usdprice,changeprice,changepercent
    except Exception as e:
        print(e)
        raise ValueError('获取失败')
if __name__ == '__main__':
    getcoinprice('sc')
