import re
import os

prefix = ""
if os.name == 'nt':
    prefix = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\'

raw_str=""
with open(os.name == 'nt' and prefix + "raw_grammar" or "raw_grammar", 'r') as f:
    raw_str = f.read()
    print raw_str
    raw_str=raw_str.replace(',\n',' ;\n')
    raw_str=re.sub(r'[0-9]+\.','',raw_str)
    print raw_str
with open(os.name == 'nt' and prefix + "clean_grammar" or "clean_grammar", 'w') as f:
	f.write(raw_str)
    #print raw_str
