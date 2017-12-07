import time
import webbrowser

count=0

while(count<3):
	time.sleep(10)
	print("You are taking a break at "+time.ctime())
	webbrowser.open("https://www.youtube.com/watch?v=vWaljXUiCaE&list=RDMMvWaljXUiCaE")
	count+=1
