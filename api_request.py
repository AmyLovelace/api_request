import requests
import shutil
image_url = "https://rickandmortyapi.com/api/character/avatar/2.jpeg"


filename =image_url.split("/")[-1]
r=requests.get(image_url,stream=True)

if r.status_code == 200:
    r.raw.decode_content=True

    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw,f)

    print("image successfully downloaded")
else:
    print("image couldn't be downloaded")



   