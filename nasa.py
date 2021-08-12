import requests
import json
import os
from baseurl import BaseUrl

r = requests.get(f'{BaseUrl.url}')
json_data = r.json()
data = json.dumps(json_data, indent=4)
wdata = json.loads(data)
cdata = ''
if (wdata != None):
    username = os.getlogin()
    try:
        os.mkdir(f'C:\\Users\\{username}\\Desktop\\Nasa')
    except:
        print("Erro")
    for x in wdata:
        response2 = requests.get(wdata["url"])
        file = open(f"C:\\Users\\{username}\\Desktop\\Nasa\\sample_image.png", "wb")
        file.write(response2.content)
        file.close()
        break
    for x in wdata:
        file = open(f"C:\\Users\\{username}\\Desktop\\Nasa\\pic_of_the_day.txt", "x")
        cdata += wdata["explanation"]
        try:
            file.write(cdata)
        except:
            print("Erro")
        file.close()
        break
