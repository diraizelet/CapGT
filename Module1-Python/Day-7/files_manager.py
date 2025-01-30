file = open("Module1-Python\\Day-7\\input.txt", "r")
file2 = open("Module1-Python\\Day-7\\output.txt", "w")

content = file.read()
file2.write(content)
print(content)
file.close()