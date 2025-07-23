import re
text = "Chennai is the IT hub"
pattern =r"IT"

search = re.search(pattern, text)
if search:
    print("pattern found", search.group())
else:
    print("pattern not found")
