# Part 1 of the Python Review lab.

def hello_world():
	print("Hello World!")

def greet_by_name(name):
	print("Hello, "+ name)

def encode(x):
	encoded=x*3953531
	return int(encoded)



def decode(coded_message):
	decoded= coded_message/3953531
	return int(decoded)

print(decode(encode(50)))