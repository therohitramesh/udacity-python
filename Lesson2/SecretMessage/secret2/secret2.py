import os

def rename_files():
	
	file_list = os.listdir("/home/rohitramesh/version-control/udacity-python/Lesson2/SecretMessage/secret2/alphabet")
	saved_path = os.getcwd()
	print("You're curently in "+saved_path)
	os.chdir("/home/rohitramesh/version-control/udacity-python/Lesson2/SecretMessage/secret2/alphabet")

	for file_name in file_list :
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files()