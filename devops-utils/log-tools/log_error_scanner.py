import re

# Path to your log file (change to /var/log/syslog or /var/log/error.log)
log_file = "/var/log/syslog"

pattern = r"ERROR: (.+)"

with open(log_file, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            print("Error found:", match.group(1))
