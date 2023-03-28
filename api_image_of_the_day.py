


















"""from urllib.request import urlopen
import json

params =
API_KEY=''
#api url
r=requests.get(''+params=)
#parametros
#https://apod.nasa.gov/apod/image/2303/WR124_Webb1024.png

if r.status_code ==200:
    results =json.loads(r.read().decode("utf-8"))
    url=results["hdurl"]
    if results["media_type"] =="image":
        with open("https://apod.nasa.gov/apod/image/2303/WR124_Webb1024.png","wb")as f:
            f.write(urlopen(url).read())
    else:
        print("url")
else:
    print("no se pudo descargar la imagen, intenta de otra forma perra.")"""


