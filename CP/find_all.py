import os


ext = input('Enter extension to look for. i.e .jpeg: ')

for root, dirs, files in os.walk('/'):
	for file in files:
		if file.endswith(ext):
			print(os.path.join(root, file))

	