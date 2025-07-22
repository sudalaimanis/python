import re

log = "Jul 22 03:15:01 server ERROR: Connection refused"
match = re.search(r"ERROR: (.+)", log)
if match:
    print("Error found:", match.group(1))
