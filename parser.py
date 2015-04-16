from tool import Produce, Solution
import lexical_analyzer
class Parser():
    def __init__(self,intokens,parsetab):
        self.parsetab=parsetab
        self.stk=[0]
        self.ans=[]
        self.intokens=intokens
        self.intokens.append('$')
    def play(self):
        i=0
        #print self.intokens
        #print self.intokens[i]
        print self.stk[len(self.stk)-1]
        print self.parsetab[self.stk[len(self.stk)-1]]
        next=self.parsetab[self.stk[len(self.stk)-1]][self.intokens[i]]
        print next
        while(next!="accept"):
            if type(next)==type((1,2)):
                if next[0]=='s':
                    self.stk.append(next[1]) 
                    i+=1                  
                elif next[0]=='r':
                    self.ans.append(next[1])
                    print next[1].post
                    if next[1].post[0] != '\xa6\xc5':
                        for j in range(len(next[1].post)):
                            self.stk.pop()
                    self.stk.append(self.parsetab[self.stk[len(self.stk)-1]][next[1].pre])
            print self.stk[len(self.stk)-1]
            print self.parsetab[self.stk[len(self.stk)-1]]
            next=self.parsetab[self.stk[len(self.stk)-1]][self.intokens[i]]
            print next
        #print self.ans
        return self.ans
        


cnm = lexical_analyzer.Solution()
file_object = open('D:\\code.txt')
text = ""
try:
    text = file_object.read()
except:
    print 'error'
hehe = cnm.lex_analyzer(text)
#######################

ans={}
with open("D:\\tab.txt",'r') as f:
    raw_str = f.read()
    sol = Solution()
    ans = sol.table_analyzer(raw_str)
#################################
print [item[0].lower() for item in hehe]
ok = Parser([item[0].lower() for item in hehe],ans)
ret = ok.play()


