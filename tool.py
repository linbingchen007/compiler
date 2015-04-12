import re
class Produce:
	def __init__(self,pre,post):
		self.pre=pre
		self.post=post
class Solution:
	def table_analyzer(self,raw_str):
		re_res=re.findall(r"<tr[^>]*>([\s\S]*?)</tr>",raw_str)
		#print re_res
		fst = True
		titles=[]
		j=0
		ret={}
		for tr in re_res:
			re_items= re.findall(r"<td[^>]*>([\s\S]*?)</td>",tr)
			if fst:
				#print re_items
				titles=re_items
				fst = False
			else:
				ret[j]={}
				for i in range(1,len(titles)+1):
					if re_items[i][0]==" ":
						continue
					elif re_items[i][0]=="s":
						ret[j][titles[i-1]]=("s", int(re_items[i].split(' ')[1]))
					elif re_items[i][0]=='r':
						words=re_items[i].split(' ')
						ret[j][titles[i-1]]=("r", Produce(words[1],words[3:]))
					elif re_items[i][0]=='a':
						ret[j][titles[i-1]]="accept"
					else:
						ret[j][titles[i-1]]=int(re_items[i])
				j+=1
		#for i in range(j):
			#print ret[i]
		return ret




with open("D:\\tab.txt",'r') as f:
	raw_str = f.read()
	sol = Solution()
	ans = sol.table_analyzer(raw_str)