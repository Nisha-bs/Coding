#!/usr/bin/python3

import re
Ip = "192.168.0.1"
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
pattern = re.match(regex, Ip)
print(pattern)
