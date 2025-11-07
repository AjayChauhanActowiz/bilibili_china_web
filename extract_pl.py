from curl_cffi import requests
from lxml import html

cookies = {
    'buvid3': '32ACC2AE-3B63-1425-3848-14027C6F9A4773957infoc',
    'b_nut': '1762503073',
    'b_lsid': '18C981C5_19A5D5EA262',
    '_uuid': '10B6714D5-FC110-BEC6-6587-5512CCB72ACA74408infoc',
    'home_feed_column': '4',
    'buvid4': '4309652C-1C76-836C-5446-52320F4E8BF075311-025110716-dl4lFHhRxN58Bql+tuiTNg%3D%3D',
    'buvid_fp': '57f6c37f4cb2289d783ad55de9246dd1',
    'CURRENT_QUALITY': '0',
    'rpdid': "|(~YkRYklml0J'u~Ykl|JJul",
    'sid': '4qhc5q49',
    'bmg_af_switch': '1',
    'bmg_src_def_domain': 'i0.hdslb.com',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI3NjU3NzcsImlhdCI6MTc2MjUwNjUxNywicGx0IjotMX0.w_0ZJ8gb_KT8-478RUW0jHVAWuyjik1SNBKBjRiEPAs',
    'bili_ticket_expires': '1762765717',
    'CURRENT_FNVAL': '2000',
    'browser_resolution': '1280-242',
}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,gu;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.bilibili.com/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    # 'cookie': "buvid3=32ACC2AE-3B63-1425-3848-14027C6F9A4773957infoc; b_nut=1762503073; b_lsid=18C981C5_19A5D5EA262; _uuid=10B6714D5-FC110-BEC6-6587-5512CCB72ACA74408infoc; home_feed_column=4; buvid4=4309652C-1C76-836C-5446-52320F4E8BF075311-025110716-dl4lFHhRxN58Bql+tuiTNg%3D%3D; buvid_fp=57f6c37f4cb2289d783ad55de9246dd1; CURRENT_QUALITY=0; rpdid=|(~YkRYklml0J'u~Ykl|JJul; sid=4qhc5q49; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI3NjU3NzcsImlhdCI6MTc2MjUwNjUxNywicGx0IjotMX0.w_0ZJ8gb_KT8-478RUW0jHVAWuyjik1SNBKBjRiEPAs; bili_ticket_expires=1762765717; CURRENT_FNVAL=2000; browser_resolution=1280-242",
}
params = {
    'keyword': '猫',
    'from_source': 'webtop_search',
    'spm_id_from': '333.1007',
    'search_source': '5',
}

response = requests.get(
    'https://search.bilibili.com/all',
    params=params,
    # cookies=cookies,
    # headers=headers,
    impersonate='chrome120'
)
print(response.status_code)
tree = html.fromstring(response.text)
print('BV1M114BiEY6' in response.text)
print([link_id.split('?')[0].replace('//www.','https://www.') if 'https' not in link_id.split('?')[0] else link_id.split('?')[0]  for link_id in tree.xpath('//div[@class="bili-video-card__wrap"]/a/@href')])
# print([link.replace('//www.','https://www.') for link in tree.xpath('//div[@class="bili-video-card__wrap"]/a[@data-mod="search-card"]/@href')])
