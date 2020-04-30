# 随机密码
import random
import configparser
import base64
import requests
import json,re
import time

requests.packages.urllib3.disable_warnings()
def loads_jsonp(_jsonp):

    """
    解析jsonp数据格式为json
    :return:
    """
    try:
        return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')
def randomnum(num):
    seed = "123456789"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt
def randompsw(num):
    seed = "1234567890abcdefghijkmnopqrstuvwxyz"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt
def randomzimu(num):
    seed = "abcdefghijkmnopqrstuvwxyz"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt
def randsaccount(num):

    seed1="1234567890abcdefghjkmnopqrstuvwxyz"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed1))
    salt = ''.join(sa)
    return salt
def randaccount(num):

    seed1="1234567890abcdefghjkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed1))
    salt = ''.join(sa)
    return salt

def randACCOUNT(num):

    seed1 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed1))
    salt = ''.join(sa)
    return salt
    #  读取文档信息
def gettxt(filename):
    lines = None
    try:
        with open(filename,'r',encoding='utf-8-sig') as f:
            lines = f.readlines()
            # print(lines,type(lines))
    except Exception as e:
        print('获得文本出错',e)
    return lines


def oneid():
    id = '86'+randomnum(13)
    return id
def oneref():
    refs=gettxt('./info/ref.txt')
    ref = random.choice(refs).strip()
    return ref
def onename():
    try:
        names = gettxt('./info/name.txt')
        name=names[0]
        names.remove(name)
        with open('./info/name.txt','w',encoding='utf-8')as f:
            f.writelines(names)
    except Exception as e:
        raise ('文本为空，请添加',e)
    return name.strip()


def oneinfo(filename):
    try:
        infos = gettxt(filename)
        info=infos[0]
        infos.remove(info)
        with open(filename,'w',encoding='utf-8')as f:
            f.writelines(infos)
    except Exception as e:
        raise ('文本为空，请添加',e)
    return info.strip()
def oneraninfo(filename):
    try:
        infos = gettxt(filename)
        info = random.choice(infos)
        infos.remove(info)
        with open(filename,'w',encoding='utf-8')as f:
            f.writelines(infos)
    except Exception as e:
        raise ('文本为空，请添加',e)
    return info.strip()
def getini(filename,setting,key):
    config = configparser.ConfigParser()
    try:
        config.read(filename)
        value = config.get(setting,key)
    except Exception as e:
        raise NameError('获取配置文件出错',e)
    return value
def jpg_base64(filename):
    with open(filename, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = 'data:image/jpeg;base64,'+base64_data.decode()
    return s
def litin1(filename):
    with open(filename, 'rb') as f:

        s = f.read().decode('latin1')
    return s


def str2header(headers_raw,*args):
    fun = headers_raw.strip().split('\n')[0].split(' ')[0]
    if headers_raw is None:
        return None
    headers = headers_raw.splitlines()
    headers_tuples = [header.split(':', 1) for header in headers]
    ua = args[0] if args else 'Linux; Android 6.0.1; MuMu Build/V417IR; wv'
    result_dict = {}
    for header_item in headers_tuples:
        # print(len(header_item))
        if not len(header_item) == 2:
            continue
        item_key = header_item[0].strip()
        item_value = header_item[1].strip()
        if item_key == 'User-Agent':
            result_dict[item_key] = item_value.format(ua)
        else:
            result_dict[item_key] = item_value
    return fun,result_dict

def str2data(data_raw):
    if data_raw is None:
        return None
    datas = data_raw.splitlines()
    datas_tuples = [data.split('	', 1) for data in datas]
    result_dict = {}
    for data_item in datas_tuples:
        # print(len(header_item))
        if not len(data_item) == 2:
            continue
        item_key = data_item[0].strip()
        item_value = data_item[1].strip()
        result_dict[item_key] = item_value
    return result_dict
def get_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999,100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)
def creathtml(svgdata):
    rawdate='''
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>SVG</title>
      </head>
      <body>
        {}
      </body>
    </html>
    '''.format(svgdata)
    with open('code.html','w',encoding='utf-8')as f:
        f.writelines(rawdate)
def screencut():
    from selenium import webdriver

    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("file:///D:\PY\scc\mode\code.html")
    browser.maximize_window()
    print(browser.title)
    try:
        base64data = browser.get_screenshot_as_base64()

    except Exception as e:
        print(e)
    browser.close()
    return base64data



def tihuan(uaend,uacore):
    ua = 'Mozilla/5.0 ('+uacore + ')' + uaend
    return ua


def oneimgname(n):
    '''
    :param : 1,2,3,4
    :return: name
    '''
    if n==1:
        newname = randompsw(random.randint(20, 30))
    elif n==2:
        newname = '微信图片_{}'.format(time.strftime('%Y%m%d%H%M%S', time.localtime(int(time.time()) - random.randint(50, 7200))))
    elif n==3:
        newname = 'IMG_{}'.format(time.strftime('%Y%m%d_%H%M%S', time.localtime(int(time.time()) - random.randint(50, 7200))))
    elif n==4:
        newname = 'Screenshot_{}'.format(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(int(time.time()) - random.randint(50, 7200))))

    return newname
def getjson(filename):
    import json
    with open(filename,'r',encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    info = []
    for i in load_dict:
        nickname = i['nick_name']
        if i['user_name']:
            wxid = i['user_name']
        else:
            wxid = i['wxid']
        info.append(nickname+'-'+wxid+'\n')
    with open(filename.split('json')[0]+'txt','w',encoding='utf-8')as f:
        f.writelines(info)
def as_num(x):
    y='{:.2f}'.format(x) # 5f表示保留5位小数点的float型
    return y
def getmd5(s):
    import hashlib
    return hashlib.md5(s.encode()).hexdigest()
if __name__ == '__main__':
    # svgdata = '<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0,0,150,50"><path d="M8 6 C75 33,57 17,135 31" stroke="#777" fill="none"/><path fill="#222" d="M84.57 25.08L84.55 25.05L84.56 25.06Q85.38 25.35 87.36 25.35L87.45 25.44L87.46 32.61L87.49 32.63Q87.53 36.90 87.65 39.80L87.64 39.79L87.54 39.69Q87.29 39.66 86.90 39.66L86.78 39.54L86.77 39.53Q85.44 39.65 84.00 40.98L83.93 40.91L83.99 40.98Q84.77 33.34 84.58 25.08ZM84.56 19.74L83.56 17.21L83.42 17.07Q85.06 16.12 85.78 15.17L85.65 15.04L85.79 15.17Q86.77 16.95 88.18 18.63L88.28 18.73L88.26 18.71Q87.48 20.25 86.11 22.38L86.00 22.28L86.09 22.37Q85.21 21.14 84.64 19.81L84.63 19.80ZM83.41 41.80L83.45 41.84L83.47 41.86Q84.47 40.77 85.73 40.28L85.64 40.19L85.77 40.32Q85.68 40.92 85.57 42.29L85.53 42.25L85.53 42.25Q86.30 42.10 86.94 42.10L86.81 41.97L86.87 42.03Q89.07 42.02 90.48 44.00L90.55 44.08L90.48 44.00Q89.19 36.62 89.27 26.46L89.33 26.52L89.39 26.58Q88.66 26.80 87.82 26.92L87.70 26.79L87.66 24.89L87.77 25.00Q86.72 25.09 85.92 25.01L85.84 24.94L86.01 25.10Q85.04 24.90 84.17 24.40L84.18 24.41L84.13 24.36Q84.31 26.45 84.31 28.51L84.30 28.50L84.32 28.51Q84.35 35.59 83.48 41.87ZM86.10 22.98L85.93 22.82L86.15 22.65L86.29 22.49L86.31 22.51Q86.68 23.26 87.71 24.75L87.69 24.73L87.76 24.79Q89.02 22.36 90.35 18.82L90.48 18.95L90.36 18.84Q89.49 18.07 87.92 16.47L88.01 16.56L87.95 16.50Q87.76 16.61 87.50 17.07L87.59 17.17L87.61 17.19Q86.59 15.87 85.68 14.42L85.61 14.34L85.77 14.51Q84.17 15.99 82.99 16.34L83.02 16.36L83.11 16.46Q84.29 20.00 86.12 23.00Z"/><path fill="#444" d="M28.28 40.20L28.21 40.13L28.21 40.14Q26.41 40.12 24.73 40.69L24.73 40.69L24.78 40.74Q25.16 36.97 25.28 33.85L25.37 33.95L25.47 34.05Q25.56 30.97 25.33 27.32L25.23 27.21L25.23 27.21Q23.87 26.88 23.11 26.50L23.09 26.49L22.76 23.52L22.67 23.44Q23.40 24.05 25.00 24.63L25.00 24.63L25.05 24.68Q24.76 22.49 24.35 19.75L24.33 19.73L24.52 19.92Q26.73 20.53 28.37 20.38L28.36 20.37L28.33 25.06L28.32 25.06Q29.66 24.91 31.00 24.42L30.91 24.33L30.96 24.38Q30.89 25.26 30.66 27.01L30.61 26.96L30.79 27.14Q29.10 27.31 28.07 27.31L28.13 27.38L28.16 27.41Q28.08 29.50 28.08 33.76L28.25 33.92L28.13 33.81Q28.12 37.95 28.20 40.12ZM31.32 23.75L31.31 23.74L31.29 23.72Q31.19 24.00 30.58 24.23L30.58 24.23L30.97 21.46L30.94 21.43Q30.02 21.61 28.61 21.84L28.66 21.89L28.60 21.83Q28.65 21.19 28.80 19.82L28.81 19.83L28.91 19.93Q28.18 19.89 27.61 19.89L27.56 19.84L27.65 19.93Q25.54 19.95 23.91 19.23L23.92 19.25L23.79 19.12Q24.43 21.73 24.70 24.21L24.74 24.25L24.57 24.08Q23.77 23.81 22.25 22.78L22.20 22.74L22.28 22.82Q22.63 24.12 22.86 26.82L22.84 26.81L22.80 26.76Q23.27 27.01 24.45 27.43L24.50 27.48L24.46 27.44Q24.51 28.09 24.55 29.50L24.47 29.43L24.84 29.45L25.00 29.53L25.07 29.61Q25.07 30.79 25.07 31.97L25.09 31.99L25.10 32.00Q25.11 36.96 24.31 41.30L24.19 41.18L24.30 41.29Q24.37 41.05 26.31 40.52L26.46 40.66L26.43 40.64Q26.46 41.31 26.34 42.68L26.28 42.62L26.34 42.67Q27.11 42.57 27.91 42.57L27.84 42.50L27.98 42.64Q29.59 42.54 31.23 43.12L31.29 43.17L31.31 43.19Q29.94 37.45 30.13 29.53L30.17 29.57L32.58 29.20L32.52 29.13Q32.70 28.33 32.78 27.30L32.75 27.27L32.86 25.18L32.89 25.21Q32.32 25.47 31.14 25.93L31.12 25.91L31.19 25.98Q31.33 24.48 31.25 24.14L31.37 24.26L31.34 24.23Q31.36 24.06 31.44 23.87Z"/><path fill="#222" d="M52.29 32.88L52.45 33.04L52.43 33.02Q55.51 32.64 58.71 32.75L58.72 32.76L58.74 32.78Q58.65 30.18 58.65 27.78L58.65 27.78L58.54 27.67Q58.56 25.22 58.75 22.66L58.84 22.76L58.85 22.77Q57.61 24.46 52.40 32.99ZM62.21 40.25L62.28 40.32L62.30 40.34Q60.66 40.07 58.87 40.00L58.71 39.83L58.85 39.97Q58.67 37.62 58.55 35.15L58.49 35.09L58.48 35.07Q53.11 34.84 48.39 36.25L48.38 36.24L48.49 36.35Q48.61 35.86 48.80 34.87L48.78 34.85L48.71 34.78Q50.63 31.76 54.21 25.47L54.10 25.36L54.03 25.29Q57.01 20.51 60.44 16.63L60.48 16.66L60.37 16.56Q61.28 16.41 62.96 16.14L63.02 16.20L63.07 16.25Q61.10 22.61 61.10 29.66L61.03 29.59L60.99 29.55Q61.10 31.14 61.18 32.63L61.23 32.69L62.46 32.73L62.53 32.81Q63.10 32.80 63.71 32.91L63.58 32.79L63.71 32.92Q63.80 33.89 64.07 35.83L64.03 35.79L64.09 35.84Q62.79 35.50 61.30 35.31L61.39 35.39L61.40 35.40Q61.66 37.45 62.34 40.38ZM63.85 32.41L63.94 32.50L63.84 32.40Q63.72 32.39 63.53 32.39L63.54 32.41L63.27 32.51L63.09 32.34Q63.05 30.93 63.05 29.52L63.00 29.46L62.98 29.44Q63.04 23.11 65.09 17.09L65.18 17.18L65.08 17.08Q64.36 17.39 62.91 17.77L62.84 17.70L62.90 17.75Q63.17 17.03 63.62 15.62L63.58 15.58L63.54 15.54Q62.22 15.89 60.16 16.12L60.35 16.31L60.34 16.30Q56.23 20.45 51.01 29.81L51.04 29.84L53.15 26.21L53.26 26.32Q52.84 27.34 52.57 27.91L52.52 27.86L48.01 36.82L48.05 36.86Q48.62 36.63 49.76 36.25L49.94 36.43L49.79 36.66L49.63 36.50Q49.58 37.25 49.27 38.51L49.28 38.51L49.24 38.47Q53.47 37.26 58.31 37.45L58.27 37.42L58.31 37.45Q58.17 38.23 58.36 40.21L58.54 40.39L58.47 40.31Q59.46 40.24 60.53 40.35L60.65 40.48L60.51 40.34Q60.77 41.13 61.03 42.50L61.02 42.49L60.93 42.39Q62.91 42.71 65.92 43.62L65.85 43.55L65.98 43.67Q65.00 41.56 64.09 38.28L63.98 38.18L65.47 38.67L65.54 38.74Q66.07 38.82 66.76 39.16L66.77 39.18L66.85 39.25Q66.08 36.77 65.93 35.10L65.87 35.04L65.81 34.98Q65.30 34.89 64.16 34.66L64.18 34.68L64.12 34.62Q63.93 33.37 63.93 32.49ZM55.92 32.32L56.02 32.42L55.87 32.27Q56.73 31.08 58.30 28.53L58.35 28.59L58.21 28.45Q58.27 29.45 58.23 30.41L58.27 30.45L58.25 30.43Q58.24 31.40 58.28 32.36L58.22 32.30L58.35 32.43Q57.64 32.25 57.07 32.25L57.13 32.32L57.11 32.30Q56.54 32.34 55.93 32.34Z"/><path fill="#222" d="M126.15 23.08L126.05 22.98L126.04 22.97Q124.27 25.73 121.60 31.36L121.58 31.34L119.59 35.60L119.73 35.73Q118.77 37.55 117.44 39.80L117.41 39.77L117.47 39.83Q117.90 39.80 116.22 39.84L116.17 39.79L116.17 39.79Q116.21 39.82 114.95 39.82L114.90 39.77L114.93 39.81Q114.32 38.43 111.38 31.27L111.29 31.17L111.40 31.28Q109.18 25.87 107.09 22.86L107.09 22.87L107.01 22.79Q107.80 25.90 107.80 29.05L107.77 29.02L107.81 29.07Q107.73 35.50 104.76 41.06L104.86 41.16L104.83 41.12Q103.43 41.40 101.07 42.13L101.19 42.24L101.06 42.12Q104.80 36.48 104.80 29.25L104.80 29.25L104.76 29.22Q104.92 20.43 99.51 13.46L99.35 13.30L99.51 13.46Q100.99 14.03 103.35 14.71L103.38 14.74L103.42 14.78Q110.52 21.57 116.61 34.90L116.59 34.88L116.56 34.85Q120.03 27.81 122.24 24.31L122.29 24.36L122.20 24.27Q125.80 18.51 129.76 15.05L129.82 15.10L129.80 15.08Q131.12 14.92 133.48 14.16L133.46 14.13L133.41 14.08Q128.52 20.80 128.52 29.40L128.36 29.25L128.36 29.25Q128.52 36.07 131.95 41.59L131.93 41.57L131.88 41.53Q130.45 41.13 127.71 40.52L127.87 40.68L127.77 40.57Q125.37 35.74 125.37 29.76L125.53 29.93L125.41 29.80Q125.47 26.43 126.15 23.08ZM127.68 41.06L127.71 41.08L127.58 40.96Q128.34 41.14 129.79 41.41L129.66 41.29L129.70 41.33Q130.11 42.04 131.07 43.53L131.17 43.63L131.11 43.57Q133.38 44.13 136.85 45.35L136.66 45.16L136.74 45.24Q130.41 38.84 130.41 29.02L130.55 29.15L130.45 29.05Q130.43 21.31 134.81 15.18L134.81 15.18L132.61 15.88L132.67 15.93Q133.72 14.44 134.37 13.56L134.32 13.51L134.24 13.43Q132.44 14.14 129.81 14.67L129.90 14.76L129.89 14.75Q123.05 20.78 117.00 33.38L116.98 33.37L117.07 33.45Q111.73 22.33 106.78 17.08L106.77 17.07L106.78 17.07Q106.55 17.15 105.98 17.04L105.88 16.94L104.78 15.76L104.62 15.60Q104.22 15.12 103.53 14.51L103.37 14.35L103.37 14.35Q100.33 13.36 98.54 12.64L98.69 12.79L98.67 12.77Q104.62 19.93 104.62 29.34L104.57 29.29L104.66 29.38Q104.49 36.83 100.34 42.69L100.37 42.72L100.47 42.81Q101.15 42.59 102.45 42.17L102.35 42.07L102.38 42.10Q102.29 42.39 100.88 44.49L100.80 44.40L100.86 44.46Q102.70 44.02 106.20 43.25L106.20 43.25L106.11 43.16Q109.96 36.25 109.77 28.48L109.67 28.37L109.63 28.33Q111.21 32.39 114.67 40.27L114.61 40.20L114.72 40.31Q114.91 40.21 115.14 40.21L115.14 40.21L115.70 40.23L115.69 40.23Q116.18 40.94 116.98 42.24L117.01 42.26L116.88 42.14Q118.61 42.22 118.61 42.22L118.49 42.11L118.61 42.23Q119.63 42.22 120.28 42.29L120.30 42.32L120.26 42.27Q121.78 38.20 125.13 30.21L125.07 30.15L125.09 30.17Q124.94 35.58 127.53 40.91Z"/></svg>'
    # creathtml(svgdata)
    getjson('../CCVC官方空投225群.json')
