# import re mean by regular expressions. python built-in library
import re
text = "work with a focus on reliability and automation"
pattern = r"focus"

search = re.search(pattern, text)

if search:
    print("pattern matched:", search.group())
else:
    print("pattern not matched")