from tool import Produce, Solution
import lexical_analyzer
import os


class Parser():

    def __init__(self, intokens, parsetab):
        self.parsetab = parsetab
        self.stk = [0]
        self.ans = []
        self.intokens = intokens
        self.intokens.append('$')

    def play(self):
        i = 0
        print self.intokens
        print self.intokens[i]
        print self.stk[len(self.stk)-1]
        print self.parsetab[self.stk[len(self.stk)-1]]
        next = self.parsetab[self.stk[len(self.stk) - 1]][self.intokens[i]]
        print next
        ac=True
        while(next != "accept"):
            if type(next) == type((1, 2)):
                if next[0] == 's':
                    self.stk.append(next[1])
                    i += 1
                elif next[0] == 'r':
                    self.ans.append(next[1])
                    # print next[1].post
                    if next[1].post[0] != '\xa6\xc5':
                        for j in range(len(next[1].post)):
                            self.stk.pop()
                    self.stk.append(
                        self.parsetab[self.stk[len(self.stk) - 1]][next[1].pre])
            print self.stk[len(self.stk)-1]
            print self.parsetab[self.stk[len(self.stk)-1]]
            try:
                next = self.parsetab[
                    self.stk[len(self.stk) - 1]][self.intokens[i]]
            except:
            	print "failed"
            	ac=False
            	break
            # print next
        # print self.ans
        if ac:
        	print "----------------------------------------"
        	print "YaY!!Accept!!!!!"
        	print "----------------------------------------"
        return self.ans


cnm = lexical_analyzer.Solution()
prefix = ''
if os.name == 'nt':
    prefix = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\'
file_object = open(prefix + 'code.txt')
text = ""
try:
    text = file_object.read()
except:
    print 'error'
hehe = cnm.lex_analyzer(text)
#######################

ans = {}
with open(os.name == 'nt' and prefix + "tab.txt" or "tab.txt", 'r') as f:
    raw_str = f.read()
    sol = Solution()
    ans = sol.table_analyzer(raw_str)
#################################
# print [item[0].lower() for item in hehe]
print ans
print "toolok"
ok = Parser([item[0].lower() for item in hehe], ans)
ret = ok.play()
for i in range(len(ret) - 1, -1, -1):
    print ret[i].__unicode__()
