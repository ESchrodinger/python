# 数据来源 ：https://www.bilibili.com/

import requests
import socket

# 发送请求

url = 'HTTP://www.bilibili.com/'
headers = {
    # 伪装信息
'Cookie': "buvid3=41F19977-33D3-0215-9010-80B36FC00D0729574infoc; _uuid=9AFE91029-10CBA-5DB6-863E-7BA8AA102927A30378infoc; buvid4=FEB3AA45-0FB4-4F82-6FF6-75B7A0E5166C31080-022062011-gQYcMJ6NCoIVvvwdtBvdsQ%3D%3D; CURRENT_BLACKGAP=0; rpdid=|(JY)Ju~uk|k0J'uYllYmYmJJ; i-wanna-go-back=-1; nostalgia_conf=-1; fingerprint=44bdb0979bb1a45c96ba526d23338c2f; buvid_fp_plain=undefined; SESSDATA=2b135585%2C1674454903%2C7fa98%2A71; bili_jct=3c047f9b86a64895952660a41b70fad7; DedeUserID=282522675; DedeUserID__ckMd5=298ef3d9989fab66; sid=8n3295ic; buvid_fp=b61a8bfc5410b2a3e51efa2f6ebcd339; blackside_state=0; b_ut=5; LIVE_BUVID=AUTO7116594927280043; CURRENT_QUALITY=64; bsource=search_baidu; b_nut=100; bp_video_offset_282522675=725678108306309100; theme_style=light; CURRENT_FNVAL=4048; PVID=2; b_lsid=A26A285B_1845AE69F4B; innersign=0",

'Referer': 'https://www.baidu.com/link?url=PqjdNcNNYRpaurH4vdeHYvTmu5VlCIbrxsxwJHSFIT3&wd=&eqid=abf37f9400090d29000000066368a3a8',

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36 SECSSOBrowserChrome'
}

response = requests.get(url=url, headers=headers)
# response2 = requests.get(url='http://www.baidu.com/')

# 这个是就是html的数据
print(response.text)
html_data = response.text

# 解析数据，把想要的内容提取出来


