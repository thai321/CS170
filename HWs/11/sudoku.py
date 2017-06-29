

sodoku = open('sudoku.in','w')
numbers = ['a','b','c','d','e','f','g','h','i']

for n in numbers:
	for i in range(1,10):
		for j in range(1,10):
			sodoku.write(n + str(i) + str(j)+ ',')
sodoku.write('p:BOOLEAN;' + '\n')

#constraints for Row
for j in range(1,10):
	for n in numbers:
		for i in range(1,10):
			temp1 = n + str(i) + str(j)
			temp2 = n + str(1) + str(j)
			if (temp1) == (not temp2):
				sodoku.write('ASSERT(' + n + str(j) + str(1) + '=>' + 'NOT' + '(' + n + str(j) + str(i) + ')' + ')' + ';' + '\n')
#constraints for Column 
for i in range(1,10):
	for n in numbers:
		for j in range(1,10):
			temp1 = n + str(i) + str(j)
			temp2 = n + str(i) + str(1)
			if (temp1) == (not temp2):
				sodoku.write('ASSERT(' + n + str(1) + str(i) + '=>' + 'NOT' + '(' + n + str(i) + str(j) + ')' + ')' + ';' + '\n' )

#constraints for 3x3 block
def block(top, down, left, right):
	for n in numbers:
		for t in top:
			for b in down:
				for i in left:
					for j in right:
						temp1 = n + str(i) + str(j)
						temp2 = n + str(t) + str(b)
						if (temp1) == (not temp2):
							sodoku.write('ASSERT(' + n + str(t) + str(b) + '=>' + 'NOT' + '(' + n + str(i) + str(j) + ')' + ')' + ';' + '\n')	 

block(range(1,4),range(1,4),range(1,4),range(1,4))
block(range(1,4),range(4,7),range(1,4),range(4,7))
block(range(1,4),range(7,10),range(1,4),range(7,10))
block(range(4,7),range(1,4),range(4,7),range(1,4))
block(range(4,7),range(4,7),range(4,7),range(4,7))
block(range(4,7),range(7,10),range(4,7),range(7,10))
block(range(7,10),range(1,4),range(7,10),range(1,4))
block(range(7,10),range(4,7),range(7,10),range(4,7))
block(range(7,10),range(7,10),range(7,10),range(7,10))

sodoku.write('ASSERT(a33 AND a33);\n')
sodoku.write('ASSERT(a57 AND a57);\n')
sodoku.write('ASSERT(a85 AND a85);\n')

sodoku.write('ASSERT(b35 AND b35);\n')
sodoku.write('ASSERT(b83 AND b83);\n')

sodoku.write('ASSERT(c26 AND c26);\n')
sodoku.write('ASSERT(c79 AND c79);\n')

sodoku.write('ASSERT(d53 AND d53);\n')
sodoku.write('ASSERT(d95 AND d95);\n')

sodoku.write('ASSERT(e29 AND e29);\n')
sodoku.write('ASSERT(e44 AND e44);\n')
sodoku.write('ASSERT(e71 AND e71);\n')

sodoku.write('ASSERT(g46 AND g46);\n')
sodoku.write('ASSERT(g78 AND g78);\n')

sodoku.write('ASSERT(h28 AND h28);\n')

sodoku.write('ASSERT(i62 AND i62);\n')
sodoku.write('ASSERT(i99 AND i99);\n')


