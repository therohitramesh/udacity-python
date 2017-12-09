#!/usr/bin/python
import urllib

#1. Read from a file
def read_text():
	quotes = open("/home/rohitramesh/version-control/udacity-python/Lesson5/ProfanityEditor/movie_quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

#2. Check for curse words
def check_profanity(text_to_check):
	connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	connection.close()
	if "true" in output: #or this can also be written as if output=="true"
		print("Profanity Alert!")
	elif "false" in output:
		print("This document is clean.")
	else:
		print("Error!")

read_text()
