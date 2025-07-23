import re
text = "Chennai is the IT hub"
pattern =r"IT"

replacement = "World Tech"

result = re.sub(pattern,replacement,text)
print(result)