import requests
from requests_html import HTMLSession
import json
url = 'http://www.xicidaili.com/'

user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
headers = {
    "User-Agent": user_agent,
    }

def get_ip_pool(type='nn', pages=1):
    session = HTMLSession()
    for page in range(1,pages+1):
        r = session.get('http://www.xicidaili.com/{}/{}'.format(type, page), headers=headers)
        ip_list = r.html.find('#ip_list')[0].text
        ip_list = ip_list.split('\n')[10:]
        ip_pool = []
        for i in range(0,len(ip_list),7):
            ip_pool.append(dict(
                zip(['ip', 'port', 'address', 'isanonymous', 'type', 'livetime', 'verifytime'],
                ip_list[i:i+7])
            ))
    # TODO: call database storage function
    
    # with open('iplist.txt', 'a', encoding='utf-8') as f:
    #     for ip_info in ip_pool:
    #         f.write(json.dumps(ip_info)+'\n')
    return ip_pool
if __name__ == '__main__':
    get_ip_pool(pages=3)