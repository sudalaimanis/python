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
print(devops[2:5][0][2:6][-1]) # accessing the last character of the sliced string

# slicing in list
print("================")
print("slicing in list")
devops_list = ["dev", "cloudops", "docker", "java","ansible"]
print(devops_list[0:2])
print(devops_list[:])  # print the whole list
print(devops_list[2:3][0])  # accessing the first element of the sliced list
print(devops_list[2:5][0][2:6])  # accessing a slice of the first element of the sliced list
print(devops_list[2:5][0][2:6][-1]) # accessing the last character of the sliced string

# dictionary slicing
print("================")
print("dictionary slicing")
devops_dict = {
    "dev": "developer",
    "python": "programming language",
    "java": "programming language",
    "devops":("dev", "cloudops", "docker", "java","ansible")
}
print(devops_dict["dev"])
print(devops_dict["devops"][-1][:5])  # accessing the last element of the tuple and slicing it the key "devops"
print(devops_dict["python"])
print(devops_dict["java"])
print(devops_dict["dev"][:2])  # slicing the value of the key "dev"
print(devops_dict["python"][:6])  # slicing the value of the key "python"
print(devops_dict["java"][:4])  # slicing the value of