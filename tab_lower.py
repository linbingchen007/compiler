import re
import os

prefix = ""
if os.name == 'nt':
    prefix = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\'

raw_str = ""
with open(os.name == 'nt' and prefix + "tab.txt" or "tab.txt", 'r') as f:
    raw_str = f.read()
    raw_str = raw_str.lower()
with open(os.name == 'nt' and prefix + "lower_tab" or "lower_tab", 'w') as f:
    f.write(raw_str)
