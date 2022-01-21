import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

files = os.path.join(BASE_DIR,'images')

#if not os.path.exists(files):
#	print('this path doesn\'t exists')

os.makedirs(files,exist_ok=True)

img = range(0,12)
for i in img:
	fname = f'{i}.txt'
	file_path = os.path.join(files, fname)
	with open(file_path, 'w') as f:
		f.write('hey guys! we love')
