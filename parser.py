from tool import Produce, Solution
import lexical_analyzer
import os

def iseql(prea,preb,posta,postb):
    return prea==preb and posta==postb

def tokentonum(tokenx):
    if(tokenx[0]=='INT'):
        return int(tokenx[1])
    elif (tokenx[0]=='REAL'):
        return float(tokenx[1])
    else:
        print tokenx
        pass #! ID
def numtoken(res):
    if type(res)==type(1):
        return ('INT',res)
    else:
        return ('REAL',res)
class Parser():

    def __init__(self, intokens, parsetab,lexbuff):
        self.parsetab = parsetab
        self.lexbuff = lexbuff
        self.lexptr = 0
        self.stk = [0]
        self.stkitem=["program'"]
        self.ans = []
        self.intokens = intokens
        self.intokens.append('$')
    def semantic_analyze(self,pre,oripost,post):
        if oripost[0]!= '\xa6\xc5' and  len(oripost)==1:
            #print '*,*'
            return post[0]
        else:
            if iseql(pre,'simple_lexpression',oripost,['simple_lexpression', 'laddop', 'lterm']):
                if post[1][0]=='PLUS':
                    res = tokentonum(post[0])+tokentonum(post[2])
                    return numtoken(res)                    
                #!!! MUL
            elif iseql(pre,'lprimary',oripost,['lr_brac', 'lexpression', 'rr_brac']):
                return post[1]
            elif iseql(pre,'lterm',oripost,['lterm', 'lmulop', 'lfactor']):
                if post[1][0]=='MULTI':
                    res = tokentonum(post[0])*tokentonum(post[2])
                    return numtoken(res)
            else:
                return post

    def play(self):
        i = 0
        #print self.intokens
        #print self.intokens[i]
        #print self.stk[len(self.stk)-1]
        #print self.parsetab[self.stk[len(self.stk)-1]]
        next = self.parsetab[self.stk[len(self.stk) - 1]][self.intokens[i]]
        #print next
        ac=True
        while(next != "accept"):
            if type(next) == type((1, 2)):
                if next[0] == 's':
                    self.stk.append(next[1])
                    self.stkitem.append(self.lexbuff[self.lexptr]) 
                    self.lexptr+=1
                    i += 1
                elif next[0] == 'r':
                    self.ans.append(next[1])
                    #print next[1].post
                    tpost=[]
                    if next[1].post[0] != '\xa6\xc5':
                        for j in range(len(next[1].post)):
                            #print (self.stk[len(self.stk)-1],next[1].post[j])
                            self.stk.pop()
                            tpost.append(self.stkitem.pop())
                    tpost.reverse()                    
                    self.stk.append(
                        self.parsetab[self.stk[len(self.stk) - 1]][next[1].pre])
                    self.stkitem.append(self.semantic_analyze(next[1].pre,next[1].post,tpost))
                    print self.stkitem[len(self.stkitem)-1]
                    print next[1].__unicode__()
            #print self.stk[len(self.stk)-1]
            #print self.parsetab[self.stk[len(self.stk)-1]]
            try:
                next = self.parsetab[
                    self.stk[len(self.stk) - 1]][self.intokens[i]]
            except:
            	print "failed"
            	ac=False
            	break
            # print next
        # print self.ans
        print (self.stk)
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
with open(os.name == 'nt' and prefix + "lower_tab" or "lower_tab", 'r') as f:
    raw_str = f.read()
    sol = Solution()
    ans = sol.table_analyzer(raw_str)
#################################
# print [item[0].lower() for item in hehe]
#print ans
#print "toolok"
ok = Parser([item[0].lower() for item in hehe], ans,hehe)
ret = ok.play()
for i in range(len(ret) - 1, -1, -1):
    print ret[i].__unicode__()

print hehe
