text = "closet of sun"
print(text)

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print("================")
print(text[-1])
print(text[-2])
print(text[-3])

# slicing in strings
print("================")
print("slicing in strings")
print(text[0:4])
print(text[:]) # print the whole string
print(text[:7])
print(text[11:])

# slicing in tuple
print("================")
print("slicing in tuple")
devops = ("dev", "ops", "python", "java")
print(devops[0:2])
print(devops[:])  # print the whole tuple
print(devops[2:3][0])  # accessing the first element of the sliced tuple
print(devops[2:5][0][2:6])  # accessing a slice of the first element of the sliced tuple