import os

directory = input('Enter /home/ if on Ubuntu, or /Users/ if on Windows or OS X: ')
ext = input('Enter extension to look for. i.e .jpeg: ')

for root, dirs, files in os.walk(directory):
	for file in files:
		if file.endswith(ext):
			print(os.path.join(root, file))

	