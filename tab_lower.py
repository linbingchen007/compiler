import re
import os

prefix = ""
if os.name == 'nt':
    prefix = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\'

raw_str = ""
with open(os.name == 'nt' and prefix + "tab.txt" or "tab.txt", 'r') as f:
    mp = {}
    ans=""
    raw_str = f.read()
    raw_words = re.split(r'[\s\t\n]+', raw_str)
    #print raw_words
    for raw_word in raw_words:
        if raw_word in mp:
            continue
        else:
            mp[raw_word] = 1
            if ord(raw_word[0]) >= ord('A') and ord(raw_word[0]) <= ord('Z'):
                raw_str=raw_str.replace(raw_word,raw_word.lower())
with open(os.name == 'nt' and prefix + "lower_tab" or "lower_tab", 'w') as f:
    f.write(raw_str)
