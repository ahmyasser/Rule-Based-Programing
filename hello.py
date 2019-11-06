pre = input('please enter preconditions')
db = pre
rule1 = [['a' , 'b'],['c']]
rule2 = [['a' , 'b' , 'c'],['D']]
rule3 = [['a' , 'b' , 'D'],['E']]
rules = [rule1 , rule2 , rule3]
j = 0
while True:
	if j == len(rules):
		break;
	for rule in rules:
		x = 0
		for i in db:
			if  i in rule[0]:
				x = x+1
		if len(rule[0]) == x:
			db.append(rule[1][0])

	j = j + 1
 
print(list(dict.fromkeys(db)))
