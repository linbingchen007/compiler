import re
keywords = {
    r'[\s\t\n]*and[\s\t\n]+': (1, 'AND'),
    r'[\s\t\n]*array': (2, 'ARRAY'),
    r'[\s\t\n]*begin[\s\t\n]+': (3, 'BEGIN'),
    r'[\s\t\n]*case[\s\t\n]+': (4, 'CASE'),
    r'[\s\t\n]*const[\s\t\n]+': (5, 'CONST'),
    r'[\s\t\n]*div[\s\t\n]+': (6, 'DIV'),
    r'[\s\t\n]*do[\s\t\n]+': (7, 'DO'),
    r'[\s\t\n]*downto[\s\t\n]+': (8, 'DOWNTO'),
    r'[\s\t\n]*else[\s\t\n]+': (9, 'ELSE'),
    r'[\s\t\n]*end': (10, 'END'),
    r'[\s\t\n]*file[\s\t\n]+': (11, 'FILE'),
    r'[\s\t\n]*for[\s\t\n]+': (12, 'FOR'),
    r'[\s\t\n]*function[\s\t\n]+': (13, 'FUNC'),
    r'[\s\t\n]*goto[\s\t\n]+': (14, 'GOTO'),
    r'[\s\t\n]*if[\s\t\n]+': (15, 'IF'),
    r'[\s\t\n]*in[\s\t\n]+': (16, 'IN'),
    r'[\s\t\n]*label[\s\t\n]+': (17, 'LABEL'),
    r'[\s\t\n]*mod[\s\t\n]+': (18, 'MOD'),
    r'[\s\t\n]*nil': (19, 'NIL'),
    r'[\s\t\n]*not[\s\t\n]+': (20, 'NOT'),
    r'[\s\t\n]*of[\s\t\n]+': (21, 'OF'),
    r'[\s\t\n]*or[\s\t\n]+': (22, 'OR'),
    r'[\s\t\n]*packed[\s\t\n]+': (23, 'PACKED'),
    r'[\s\t\n]*procedure[\s\t\n]+': (24, 'PROC'),
    r'[\s\t\n]*program[\s\t\n]+': (25, 'PROG'),
    r'[\s\t\n]*record[\s\t\n]+': (26, 'RECORD'),
    r'[\s\t\n]*repeat[\s\t\n]+': (27, 'REPEAT'),
    r'[\s\t\n]*set[\s\t\n]+': (28, 'SET'),
    r'[\s\t\n]*then[\s\t\n]+': (29, 'THEN'),
    r'[\s\t\n]*to[\s\t\n]+': (30, 'TO'),
    r'[\s\t\n]*type': (31, 'TYPE'),
    r'[\s\t\n]*until[\s\t\n]+': (32, 'UNTIL'),
    r'[\s\t\n]*var[\s\t\n]+': (33, 'VAR'),
    r'[\s\t\n]*while[\s\t\n]+': (34, 'WHILE'),
    r'[\s\t\n]*with[\s\t\n]+': (35, 'WITH'),
    r'[\s\t\n]*\+': (40, 'PLUS'),
    r'[\s\t\n]*\-': (41, 'MINUS'),
    r'[\s\t\n]*\*\*': (60, 'EXP'),
    r'[\s\t\n]*\*': (42, 'MULTI'),
    r'[\s\t\n]*/': (43, 'RDIV'),
    r'[\s\t\n]*=': (44, 'EQ'),
    r'[\s\t\n]*<>': (49, 'NE'),
    r'[\s\t\n]*<=': (47, 'LE'),
    r'[\s\t\n]*<': (45, 'LT'),
    r'[\s\t\n]*>=': (48, 'GE'),
    r'[\s\t\n]*>': (46, 'GT'),
    r'[\s\t\n]*\(': (50, 'LR_BRAC'),
    r'[\s\t\n]*\)': (51, 'RR_BRAC'),
    r'[\s\t\n]*,': (52, 'COMMA'),
    r'[\s\t\n]*`': (53, 'P_MARK'),
    r'[\s\t\n]*\.\.': (55, 'RANGE'),
    r'[\s\t\n]*\.': (54, 'F_STOP'),
    r'[\s\t\n]*:=': (57, 'ASSIGN'),
    r'[\s\t\n]*:': (56, 'COLON'),
    r'[\s\t\n]*;': (58, 'SEMIC'),
    r'[\s\t\n]*\^': (59, 'CAP'),
    r'[\s\t\n]*\[': (61, 'LS_BRAC'),
    r'[\s\t\n]*\]': (62, 'RS_BRAC'),
    # r"[\s\t\n]*'":(63,'Q_MARK'),
}
up_keywords = {
    r'[\s\t\n]*AND[\s\t\n]+': (1, 'AND'),
    r'[\s\t\n]*ARRAY': (2, 'ARRAY'),
    r'[\s\t\n]*BEGIN[\s\t\n]+': (3, 'BEGIN'),
    r'[\s\t\n]*CASE[\s\t\n]+': (4, 'CASE'),
    r'[\s\t\n]*CONST[\s\t\n]+': (5, 'CONST'),
    r'[\s\t\n]*DIV[\s\t\n]+': (6, 'DIV'),
    r'[\s\t\n]*DO[\s\t\n]+': (7, 'DO'),
    r'[\s\t\n]*DOWNTO[\s\t\n]+': (8, 'DOWNTO'),
    r'[\s\t\n]*ELSE[\s\t\n]+': (9, 'ELSE'),
    r'[\s\t\n]*END': (10, 'END'),
    r'[\s\t\n]*FILE[\s\t\n]+': (11, 'FILE'),
    r'[\s\t\n]*FOR[\s\t\n]+': (12, 'FOR'),
    r'[\s\t\n]*FUNCTION[\s\t\n]+': (13, 'FUNC'),
    r'[\s\t\n]*GOTO[\s\t\n]+': (14, 'GOTO'),
    r'[\s\t\n]*IF[\s\t\n]+': (15, 'IF'),
    r'[\s\t\n]*IN[\s\t\n]+': (16, 'IN'),
    r'[\s\t\n]*LABEL[\s\t\n]+': (17, 'LABEL'),
    r'[\s\t\n]*MOD[\s\t\n]+': (18, 'MOD'),
    r'[\s\t\n]*NIL': (19, 'NIL'),
    r'[\s\t\n]*NOT[\s\t\n]+': (20, 'NOT'),
    r'[\s\t\n]*OF[\s\t\n]+': (21, 'OF'),
    r'[\s\t\n]*OR[\s\t\n]+': (22, 'OR'),
    r'[\s\t\n]*PACKED[\s\t\n]+': (23, 'PACKED'),
    r'[\s\t\n]*PROCEDURE[\s\t\n]+': (24, 'PROC'),
    r'[\s\t\n]*PROGRAM[\s\t\n]+': (25, 'PROG'),
    r'[\s\t\n]*RECORD[\s\t\n]+': (26, 'RECORD'),
    r'[\s\t\n]*REPEAT[\s\t\n]+': (27, 'REPEAT'),
    r'[\s\t\n]*SET[\s\t\n]+': (28, 'SET'),
    r'[\s\t\n]*THEN[\s\t\n]+': (29, 'THEN'),
    r'[\s\t\n]*TO[\s\t\n]+': (30, 'TO'),
    r'[\s\t\n]*TYPE': (31, 'TYPE'),
    r'[\s\t\n]*UNTIL[\s\t\n]+': (32, 'UNTIL'),
    r'[\s\t\n]*VAR[\s\t\n]+': (33, 'VAR'),
    r'[\s\t\n]*WHILE[\s\t\n]+': (34, 'WHILE'),
    r'[\s\t\n]*WITH[\s\t\n]+': (35, 'WITH'),
    # r"[\s\t\n]*'":(63,'Q_MARK'),
}
re_tab = [
    (r"[\s\t\n]*([a-zA-Z][a-zA-Z0-9]*)", (36, 'ID')),
    (r"[\s\t\n]*([0-9]+.[0-9]+)", (38, 'REAL')),
    (r"[\s\t\n]*([0-9]+)", (37, 'INT')),

    #(r"^'[\s\S]'$",(39,'STRING')),
]


class Solution:

    def lex_analyzer(self, t_str):
        ret = []
        strlen = len(t_str)
        i = 0
        while i < strlen:
            # print i
            fg = False
            for keyword in keywords:
                re_res = re.match(keyword, t_str[i:])
                if re_res:
                    # print keyword
                    # print re_res
                    ret.append((keywords[keyword][1], 0))
                    i += len(re_res.group(0))
                    # print re_res.group(0)
                    fg = True
                    break
            if fg:
                continue
            for keyword in up_keywords:
                re_res = re.match(keyword, t_str[i:])
                if re_res:
                    # print keyword
                    # print re_res
                    ret.append((up_keywords[keyword][1], 0))
                    i += len(re_res.group(0))
                    # print re_res.group(0)
                    fg = True
                    break
            if fg:
                continue
            for re_pattern in re_tab:
                re_res = re.match(re_pattern[0], t_str[i:])
                if re_res:
                    # print re_res
                    ret.append((re_pattern[1][1], re_res.group(1)))
                    i += len(re_res.group(0))
                    # print re_res.group(0)
                    fg = True
                    break
            if fg:
                continue
            if t_str[i] == "'":
                ret.append(('Q_MARK', 0))
                j = 1
                while i + j < strlen and (t_str[i + j] != "'" or (i + j + 1 < strlen and t_str[i + j + 1] == "'")):
                    if t_str[i + j] == "'":
                        j += 2
                    else:
                        j += 1
                ret.append(('STRING', t_str[i + 1:i + j]))
                if i + j < strlen:
                    pass
                else:
                    ret.append(('Q_MARK', 0))
                i += j
            elif t_str[i] == "{":
                j = 1
                while i + j < strlen and t_str[i + j] != "}":
                    j += 1
                i += j
            i += 1
        for lex in ret:
            print lex
        return lex
        # print ret

    # Deprecated
    """
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
	"""

cnm = Solution()
file_object = open('H:\\tst.txt')
text = ""
try:
    text = file_object.read()
except:
    print 'error'
cnm.lex_analyzer(text)
