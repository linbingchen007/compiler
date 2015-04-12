[nonterminal]
	program subprogram_declarations
	identifier_list declarations compound_statement
	declaration type standard_type
[terminal]
	prog id lr_brac rr_brac semic comma var colon range of
	array int real [ ]
[start]
	program'
[production]
	program' => program ;
	program => prog id lr_brac identifier_list rr_brac semic
			   declarations
			   subprogram_declarations
			   compound_statement ;
	identifier_list => id | identifier_list comma id ;
	declarations => var declaration semic | ;
	declaration => declaration semic identifier_list : type |
				   identifier_list : type ;
	type => standard_type |
			array [ int range int ] of standard_type ;
	standard_type => int | real ;