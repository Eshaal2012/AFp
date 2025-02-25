#Access file codingal.txt and implement write mode on it

file = open("codingal.txt", "w")
file.write("Hello, this is a file created by Python!")
file.close()

file = open("codingal.txt", "r")
print(file.read())
file.close()