import os

this_file_path = os.path.abspath(__file__)
#print(this_file_path)
BASE_DIR = os.path.dirname(this_file_path)
#print(BASE_DIR)

ENTIER_PROJ = os.path.dirname(BASE_DIR)
#print(ENTIER_PROJ)
fname = os.path.join(BASE_DIR,'template/hey.txt')


#open
with open(fname, 'r') as f:
	r = f.read()
print(r.format(name='Emino'))