import re
keywords={
	'and':(1,'AND'),
	'array':(2,'ARRAY'),
	'begin':(3,'BEGIN'),
	'case':(4,'CASE'),
	'const':(5,'CONST'),
	'div':(6,'DIV'),
	'do':(7,'DO'),
	'downto':(8,'DOWNTO'),
	'else':(9,'ELSE'),
	'end':(10,'END'),
	'file':(11,'FILE'),
	'for':(12,'FOR'),
	'function':(13,'FUNC'),
	'goto':(14,'GOTO'),
	'if':(15,'IF'),
	'in':(16,'IN'),
	'label':(17,'LABEL'),
	'mod':(18,'MOD'),
	'nil':(19,'NIL'),
	'not':(20,'NOT'),
	'of':(21,'OF'),
	'or':(22,'OR'),
	'packed':(23,'PACKED'),
	'procedure':(24,'PROC'),
	'program':(25,'PROG'),
	'record':(26,'RECORD'),
	'repeat':(27,'REPEAT'),
	'set':(28,'SET'),
	'then':(29,'THEN'),
	'to':(30,'TO'),
	'type':(31,'TYPE'),
	'until':(32,'UNTIL'),
	'var':(33,'VAR'),
	'while':(34,'WHILE'),
	'with':(35,'WITH'),
	'+':(40,'PLUS'),
	'-':(41,'MINUS'),
	'*':(42,'MULTI'),
	'/':(43,'RDIV'),
	'=':(44,'EQ'),
	'<':(45,'LT'),
	'>':(46,'GT'),
	'<=':(47,'LE'),
	'>=':(48,'GE'),
	'<>':(49,'NE'),
	'(':(50,'LR_BRAC'),
	')':(51,'RR_BRAC'),
	',':(52,'COMMA'),
	'`':(53,'P_MARK'),
	'.':(54,'F_STOP'),
	'..':(55,'RANGE'),
	':':(56,'COLON'),
	':=':(57,'ASSIGN'),
	';':(58,'SEMIC'),
	'^':(59,'CAP'),
	'**':(60,'EXP'),
	'[':(61,'LS_BRAC'),
	']':(62,'RS_BRAC'),
	"'":(63,'Q_MARK'),
}
re_tab=[
	(r"^[a-zA-Z][a-zA-Z0-9]*$",(36,'ID')),
	(r"^[0-9]+$",(37,'INT')),
	(r"^[0-9]+.[0-9]+$",(38,'REAL')),
	(r"^'[\s\S]'$",(39,'STRING')),
	]

class Solution:
	def another_lex_analyzer(self,t_str):
		pass
	def lex_analyzer(self,t_str):
		ret=[]
		raw_words = re.split(r'[\s\t\n]+',t_str)
		#print raw_words
		for raw_word in raw_words:
			if raw_word in keywords:
				ret.append((keywords[raw_word][1],0))
			else:
				for re_pattern in re_tab:
					re_res= re.match(re_pattern[0],raw_word)
					if re_res:
						ret.append((re_pattern[1][1],re_res.group(0)))
		print ret
		return ret

cnm=Solution()
file_object=open('tst.txt')
text=""
try:
	text = file_object.read()
except:
	print 'error'
cnm.lex_analyzer(text)