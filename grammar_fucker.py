import re
import os

prefix = ""
if os.name == 'nt':
    prefix = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\'

raw_str = ""
with open(os.name == 'nt' and prefix + "clean_grammar" or "clean_grammar", 'r') as f:
    mp = {}
    raw_str = f.read()
    raw_words = re.split(r'[\s\t\n]+', raw_str)
    print raw_words
    for raw_word in raw_words:
        if raw_word in mp:
            continue
        else:
            mp[raw_word] = 1
            if ord(raw_word[0]) >= ord('a') and ord(raw_word[0]) <= ord('z'):
                print raw_word
                raw_str = raw_str.replace(raw_word, 'l' + raw_word)
with open(os.name == 'nt' and prefix + "fucked_grammar" or "fucked_grammar", 'w') as f:
    f.write(raw_str)
