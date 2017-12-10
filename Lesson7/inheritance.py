class Parent():
	"""This is the documentation of class Parent() which can be accessed by calling __doc__"""

	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last Name: "+self.last_name)
		print("Eye Color: "+self.eye_color)

class Child(Parent): #Takes Parent as a parameter
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color) #To use all the functions defined in Parent's __init__
		self.number_of_toys = number_of_toys

	def show_info(self):
		print("Last Name- "+self.last_name)
		print("Eye Color- "+self.eye_color)
		print("Number of toys- "+str(self.number_of_toys))

billy_cyrus = Parent("Cyrus", "blue")
miley_cyrus = Child("Cyrus","Blue",5)
# print(miley_cyrus.last_name)
# print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()