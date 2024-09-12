import time
import requests
import json
from bs4 import BeautifulSoup
from X_APP_Token import get_v2_token

# 话题链接
url = 'https://api.coolapk.com/v6/page/dataList?url\u003d%23%2Ffeed%2FmultiTagFeedList%3FlistType%3Ddateline_desc%26hiddenTagRelation%3D1%26ignoreEntityById%3D1%26cacheExpires%3D60%26tag%3D%25E8%2596%2585%25E7%25BE%258A%25E6%25AF%259B%25E5%25B0%258F%25E5%2588%2586%25E9%2598%259F\u0026title\u003d%E6%9C%80%E6%96%B0%E5%8F%91%E5%B8%83\u0026subTitle\u003d\u0026page\u003d1\u0026firstItem\u003d56016385'

ID = []

# 更新token
def update_token():
    headers['X-App-Token'] = get_v2_token()


# 获取帖子列表
headers = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; PIC-AL00 Build/HUAWEIPIC-AL00) (#Build; HUAWEI; PIC-AL00; PIC-AL00 8.0.0.377(C00); 8.0.0) +CoolMarket/13.1.1-2303202-universal",
    "X-Requested-With": "XMLHttpRequest",
    "X-Sdk-Int": "26",
    "X-Sdk-Locale": "zh-CN",
    "X-App-Id": "com.coolapk.market",
    "X-App-Token": "v2JDJ5JDEwJE1UY3hPRFV3TlRneU5nLzBhNDQ1MHVCQkRrMWJqUVBYRk4vT0Z3LjVUaWZRRUdnMFdLdWhx",
    "X-App-Version": "13.1.1",
    "X-Api-Version": "13",
    "X-App-Device": "gM1cDMmRmZmRmZxYTLmdjYm1iM4MGMtUmZkZTL1ImNjZmZmZGI7kCMwMEK3czMuAjLw4COgADMMFULDlEUgsDMwwUQtMUSQByOJV0VBVFSgsTSFdVQVhEI7gTN6QEM6MTN6kTR6YDO6QzQgsDI7AyOlN2M2F0dWlnNsJjc2M2NylHT0BzUxBHOx9UMrNFVOVEezUFR",
    "X-Dark-Mode": "0",
    "X-App-Channel": "coolapk",
    "X-App-Mode": "universal",
    "X-App-Supported": "2303202",
    "Host": "api.coolapk.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

# 获取帖子内容
headers1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "SESSID=882c-65700151e7ff4-1701839185-9459",
    "Host": "www.coolapk.com",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": "'Microsoft Edge';'v='119', 'Chromium';v='119', 'Not?A_Brand';v='24'",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "'Windows'",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}

update_token()

res = requests.get(url,headers=headers)
# 检查请求是否正确响应
print(res.status_code)

# 获取帖子内容
def get_detail(i):
    # print('message:', i.get('message'))
    print('pic:', i.get('pic'))
    shareUrl = i.get('shareUrl')
    print('shareUrl:', shareUrl)
    ID.append(i.get('id'))
    if shareUrl:
        pass
    html = requests.get(shareUrl, headers=headers1).text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        if soup.find('div', class_='feed-message') == None:
            if soup.find('div', class_='feed-article-message') == None:
                pass
            else:
                content = soup.find('div', class_='feed-article-message').text
        else:
            content = soup.find('div', class_='feed-message').text
        print('content:', content)
    except:
        pass


while True:
    res = requests.get(url,headers=headers)  # 获取帖子列表
    a = res.json()
    for i in a.get('data'):
        if i.get('id') in ID:
            continue
        else:
            try:
                get_detail(i)  # 获取帖子内容
            except:
                continue
