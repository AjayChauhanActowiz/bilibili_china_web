from curl_cffi import requests
from lxml import html
import json
import re
import os
import pydash as _
import pandas as pd
import videos_link

cookies = {
    'buvid3': '32ACC2AE-3B63-1425-3848-14027C6F9A4773957infoc',
    'b_nut': '1762503073',
    '_uuid': '10B6714D5-FC110-BEC6-6587-5512CCB72ACA74408infoc',
    'home_feed_column': '4',
    'buvid4': '4309652C-1C76-836C-5446-52320F4E8BF075311-025110716-dl4lFHhRxN58Bql+tuiTNg%3D%3D',
    'bmg_af_switch': '1',
    'bmg_src_def_domain': 'i0.hdslb.com',
    'buvid_fp': '57f6c37f4cb2289d783ad55de9246dd1',
    'CURRENT_QUALITY': '0',
    'rpdid': "|(~YkRYklml0J'u~Ykl|JJul",
    'sid': '4qhc5q49',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI3NjU3NzcsImlhdCI6MTc2MjUwNjUxNywicGx0IjotMX0.w_0ZJ8gb_KT8-478RUW0jHVAWuyjik1SNBKBjRiEPAs',
    'bili_ticket_expires': '1762765717',
    'browser_resolution': '1280-242',
    'CURRENT_FNVAL': '4048',
    'b_lsid': '5C9FBAA4_19A5DB147AA',
}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,gu;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    # 'cookie': "buvid3=32ACC2AE-3B63-1425-3848-14027C6F9A4773957infoc; b_nut=1762503073; _uuid=10B6714D5-FC110-BEC6-6587-5512CCB72ACA74408infoc; home_feed_column=4; buvid4=4309652C-1C76-836C-5446-52320F4E8BF075311-025110716-dl4lFHhRxN58Bql+tuiTNg%3D%3D; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; buvid_fp=57f6c37f4cb2289d783ad55de9246dd1; CURRENT_QUALITY=0; rpdid=|(~YkRYklml0J'u~Ykl|JJul; sid=4qhc5q49; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI3NjU3NzcsImlhdCI6MTc2MjUwNjUxNywicGx0IjotMX0.w_0ZJ8gb_KT8-478RUW0jHVAWuyjik1SNBKBjRiEPAs; bili_ticket_expires=1762765717; browser_resolution=1280-242; CURRENT_FNVAL=4048; b_lsid=5C9FBAA4_19A5DB147AA",
}
def save_page(html_text, product_id):
    dir_path = f"D:/Ajay_chauhan/page_save/bilibili_china_web/2025-11-07/pdp"
    os.makedirs(dir_path, exist_ok=True)
    file_path = dir_path + f"/{product_id}.html"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_text)
    return os.path.abspath(file_path)
def pdp_data(url):
    try:
        response = requests.get(
            # 'https://www.bilibili.com/video/BV19GnUzcEQL/',
            url,
            # cookies=cookies,
            # headers=headers,
            impersonate='chrome120'
        )
        print(response.status_code)
        if response.status_code == 200:
            # tree = html.fromstring(response.text)
            # json_data = tree.xpath('//script[contains(text(),"window.__playinfo__=")]/text()')[0].replace('window.__playinfo__=','')
            match = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\})(?=;|<\/script>|$)', response.text, re.S)
            if match:
                json_data = json.loads(match.group(1))
                return_tags = []
                tags = _.get(json_data,'tags',[])
                for tag in tags:
                    return_tags.append({
                        'tag_id': _.get(tag,'tag_id',None),
                        'tag_name': _.get(tag,'tag_name',None),
                        'tag_type': _.get(tag,'tag_type',None),
                        'tag_url': _.get(tag,'jump_url',None)
                    })
                if _.get(json_data,'videoData.bvid',None):
                    save_page(response.text,_.get(json_data,'videoData.bvid',None))
                    return {
                        'url': url,
                        'bvid': _.get(json_data,'videoData.bvid',None),
                        'aid': _.get(json_data,'videoData.aid',None),
                        'title': _.get(json_data,'videoData.title',None),
                        'image': _.get(json_data,'videoData.pic',None),
                        'description': _.get(json_data,'videoData.desc',None),
                        'duration_in_sec': _.get(json_data,'videoData.duration',None),
                        'owner_id': _.get(json_data,'videoData.owner.mid',None),
                        'owner_name': _.get(json_data,'videoData.owner.name',None),
                        'owner_image': _.get(json_data,'videoData.owner.face',None),
                        'views': _.get(json_data,'videoData.stat.view',None),
                        'danmaku': _.get(json_data,'videoData.stat.danmaku',None),
                        'reply': _.get(json_data,'videoData.stat.reply',None),
                        'favorite': _.get(json_data,'videoData.stat.favorite',None),
                        'coin': _.get(json_data,'videoData.stat.coin',None),
                        'share': _.get(json_data,'videoData.stat.share',None),
                        'like': _.get(json_data,'videoData.stat.like',None),
                        'dislike': _.get(json_data,'videoData.stat.dislike',None),
                        'dimension_width': _.get(json_data,'videoData.dimension.width',None),
                        'dimension_height': _.get(json_data,'videoData.dimension.height',None),
                        'tags': json.dumps(return_tags,ensure_ascii=False) if return_tags else None
                    }
                else:
                    print('bvid not found')
                    return None
            else:
                print('match not found')
                return None
        else:
            print('response not found')
            return None
    except Exception as e:
        print(f'exception occur : {e}')
total_data = []
for link in videos_link.unique_links[:25]:
    data = pdp_data(link)
    if data:
        total_data.append(data)
    print('done')
df = pd.DataFrame(total_data)
df.fillna("N/A", inplace=True)
file_name = 'bilibili_sample_data'
df.to_excel(f"{file_name}.xlsx", index=False,engine='openpyxl')
print(f"✅ Data exported to '{file_name}.xlsx' (excluding _id and path).")
