import os

def rename_files():
	# 1. Get file names from a folder
	file_list = os.listdir("/home/rohitramesh/version-control/udacity-python/Lesson2/SecretMessage/secret1/prank")
	saved_path = os.getcwd()
	print("Current working directory is "+saved_path)
	os.chdir("/home/rohitramesh/version-control/udacity-python/Lesson2/SecretMessage/secret1/prank")

	# 2. For each file, rename file
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files()