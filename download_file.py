import os
import requests
import random

file_dir = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(file_dir)
DOWNLAOD_DRS = os.path.join(BASE_DIR,'download')

os.makedirs(DOWNLAOD_DRS,exist_ok=True)

def download(DOWNLAOD_DRS):
	url = 'https://dazedimg-dazedgroup.netdna-ssl.com/900/azure/dazed-prod/1240/9/1249851.jpg'

	nm = random.randint(0,10)
	downloaded_img = os.path.join(DOWNLAOD_DRS,f'download{nm}.jpg')
	r = requests.get(url,stream=True)
	with open(downloaded_img,'wb') as f: #wb: write byte
		f.write(r.content)
		print('download successfuly')


if __name__ == '__main__':
	download(DOWNLAOD_DRS)