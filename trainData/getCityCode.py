import re
import urllib3
import requests
import json
urllib3.disable_warnings()

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9095'
response = requests.get(url, verify=False)
cStations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
eStations = [tuple(reversed(t)) for t in cStations]
cstr = "cityCode = "+json.dumps(dict(cStations), ensure_ascii=False)
estr = "cityCode = "+json.dumps(dict(eStations), ensure_ascii=False)
with open("lib/cStationName.py", "w", encoding='utf8') as f:
    f.write(str(cstr))
    print("写入以中文为键的车站文件完成...")
with open("lib/eStationName.py", "w", encoding='utf8') as f:
    f.write(str(estr))
    print("写入以英文为键的车站文件完成...")
