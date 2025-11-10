from curl_cffi import requests
# import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


cookies = {
    'buvid3': '32ACC2AE-3B63-1425-3848-14027C6F9A4773957infoc',
    'b_nut': '1762503073',
    'b_lsid': '18C981C5_19A5D5EA262',
    '_uuid': '10B6714D5-FC110-BEC6-6587-5512CCB72ACA74408infoc',
    'home_feed_column': '4',
    'browser_resolution': '1280-551',
    'buvid4': '4309652C-1C76-836C-5446-52320F4E8BF075311-025110716-dl4lFHhRxN58Bql+tuiTNg%3D%3D',
    'bmg_af_switch': '1',
    'bmg_src_def_domain': 'i0.hdslb.com',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI3NjIyNzUsImlhdCI6MTc2MjUwMzAxNSwicGx0IjotMX0.EAKcaE4Fo52XpV5KMDYHctiB6Au85lsusMMPHae-h3o',
    'bili_ticket_expires': '1762762215',
    'buvid_fp': '57f6c37f4cb2289d783ad55de9246dd1',
    'CURRENT_QUALITY': '0',
    'rpdid': "|(~YkRYklml0J'u~Ykl|JJul",
    'sid': '4qhc5q49',
    'CURRENT_FNVAL': '4048',
}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,gu;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.bilibili.com/c/game/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    # 'cookie': "buvid3=32ACC2AE-3B63-1425-3848-14027C6F9A4773957infoc; b_nut=1762503073; b_lsid=18C981C5_19A5D5EA262; _uuid=10B6714D5-FC110-BEC6-6587-5512CCB72ACA74408infoc; home_feed_column=4; browser_resolution=1280-551; buvid4=4309652C-1C76-836C-5446-52320F4E8BF075311-025110716-dl4lFHhRxN58Bql+tuiTNg%3D%3D; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI3NjIyNzUsImlhdCI6MTc2MjUwMzAxNSwicGx0IjotMX0.EAKcaE4Fo52XpV5KMDYHctiB6Au85lsusMMPHae-h3o; bili_ticket_expires=1762762215; buvid_fp=57f6c37f4cb2289d783ad55de9246dd1; CURRENT_QUALITY=0; rpdid=|(~YkRYklml0J'u~Ykl|JJul; sid=4qhc5q49; CURRENT_FNVAL=4048",
}
params = {
    'spm_id_from': '333.40138.feed-card.all.click',
}

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# token = "token"
# proxyModeUrl = "http://{}:@proxy.scrape.do:8080".format(token)
## proxyModeUrl = "http://{}:super=true@proxy.scrape.do:8080".format(token)
## proxyModeUrl = "http://{}:super=true&geoCode=us@proxy.scrape.do:8080".format(token)
# proxies = {
#     "http": proxyModeUrl,
#     "https": proxyModeUrl,
# }

# proxy_url = "http://user-spqf6yqq8t-country-in:aQuQe050b3rmtbxD+V@dc.decodo.com:10001"
# proxies = {
#     "http": proxy_url,
#     "https": proxy_url,
# }

# scraper_api_token = 'token'
# proxies = {
#     "http": f"http://scraperapi:{scraper_api_token}@proxy-server.scraperapi.com:8001",
#     "https": f"http://scraperapi:{scraper_api_token}@proxy-server.scraperapi.com:8001"
# }

def response_check(start_iteration, num_requests):
    """Perform multiple requests inside one thread to reduce overhead."""
    batch_results = []
    for i in range(num_requests):
        iteration = start_iteration + i
        st = time.time()
        try:
            response = requests.get(
                'https://www.bilibili.com/video/BV1k2aizzEXD/',
                # params=params,
                # headers=headers,
                # cookies=cookies,
                impersonate='chrome120',
                # proxies=proxies,
                # verify=False,
                timeout=120
            )
            if fr'"coin":5287' in response.text:
                return_dict = {
                    'iteration': iteration,
                    'status': response.status_code,
                    'response': 'good',
                    'time_taken': time.time()-st
                }
                batch_results.append(return_dict)
                print(return_dict)
            else:
                return_dict = {
                    'iteration': iteration,
                    'status': response.status_code,
                    'response': 'bad',
                    'time_taken': time.time() - st
                }
                batch_results.append(return_dict)
                print(return_dict)
        except Exception as e:
            return_dict = {
                'iteration': iteration,
                'status': None,
                'response': f'error: {e}',
                'time_taken': time.time() - st
            }
            batch_results.append(return_dict)
            print(return_dict)
    return batch_results

results = []
thread_count = 20
total_requests = 3000
requests_per_thread = 1  # Each worker handles 10 requests

with ThreadPoolExecutor(max_workers=thread_count) as executor:
    futures = []
    for start in range(1, total_requests + 1, requests_per_thread):
        futures.append(executor.submit(response_check, start, requests_per_thread))

    for future in as_completed(futures):
        batch = future.result()
        for result in batch:
            # print(result)
            results.append(result)

# Save results to Excel
file_name = 'bilibili_pdp_feasibility_test'
df = pd.DataFrame(results)
df.to_excel(f'{file_name}.xlsx', index=False)
print(f"Results saved to {file_name}.xlsx")


