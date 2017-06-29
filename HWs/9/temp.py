
# import sys
# reads = sys.stdin.read().splitlines()
# for e in reads:
# 	print e
# # your main algorithm should go below
# # answer = "".join(reads)
# # print answer

# import fileinput
# s1 = ""
# for line in fileinput.input():
#     line = line.strip() # Remove the trailing newline
#     # do_something(line)  # Each line is a short read
#     # print line
#     s1 = overlap(s1,line)
# print s1
# lines = []
def overlap(s1,s2): #O(k^2n^2)
	flag = False
	if len(s1) < len(s2):
		flag = True
		s1,s2 = s2, s1
	if len(s2) == 0:
		return s1
	temp = []
	for i in xrange(0,len(s1) - len(s2)):
		if s1[i:i+len(s2)] == s2:
			# print "Here1"
			# return i, len(s2)
			temp.append((i, len(s2), 1))
			# if (temp[0])

	for i in xrange(len(s1) - len(s2), len(s1)): #inside
		if s1[i:] == s2[:len(s1) - i]:
			# print "here2"
			# return i, len(s1) - i
			temp.append((i, len(s1)- i,2))
	
	for i in xrange(0,-len(s2) , -1):
		if s1[:len(s2) + i] == s2[-i:]:
			# print "here3"
			# print "s2[",i,",",len(s2) + i ,"] = ", s1[-1] , "  ", s2[-1]
			temp.append((i,len(s2)+ i, 3))

	if len(temp) == 0:
		return None
	current = temp[0]
	for i in range(len(temp)):
		# print temp[i]
		a = current[1]
		b = temp[i][1]
		# print a,b
		if a < b:
			current = temp[i]
	if current[2] == 1:
		# lines.remove(s2)
		# print "here1"
		return (s1, current[1])
	elif current[2] == 2:
		# print "here2"
		index = current[0]
		return (s1[:index] + s2, current[1])
	else:#if current[2] == 3:
		# print "here3"
		index = current[1]
		return (s2[:-index] + s1, current[1])
	# return None


	# return current


	# return None
# print overlap("xyabcdezzzzz", "zzzzzabcdexyab")
# print overlap("", "zzzzzabcdexyab")

# print overlap("xxdsdsfsByab","abcd")

# print overlap("zzab", "abcxx")
print overlap("yyytzzasbczz","zzabczyyy")


# import fileinput
# s1 = ""
# # i = 0
# lines = []
# result = []
# for line in fileinput.input():
#     line = line.strip() # Remove the trailing newline
#     # do_something(line)  # Each line is a short read
#     # print line
#     # s1 = overlap(s1,line)
#     lines.append(line)
#     # print i," = ", s1
#     # i +=1


# # for i in range(len(lines)):
# # 	s1 = overlap(s1,lines[i])
# # print s1
# while(len(lines) > 2):
# 	x = len(lines)
# 	table = []
# 	for i in range(x):
# 		table.append(0)
# 	result = []
# 	for i in range(x -1):
# 		temp = []
# 		table[i] = 2
# 		for j in range(i + 1,x):
# 			# print i, j
# 			if (table[j] == 0):
# 				S = overlap(lines[i],lines[j])
# 				if S != None:
# 					# print "s1 = ", lines[i]
# 					# print "s2 = ", lines[j]
# 					# print S[0],", overlap = ", S[1]
# 					temp.append((S,j))
			
# 		current = 0
# 		if len(temp) != 0:
# 			value = temp[0][0]
# 			y = temp[0][1]
# 			for S in temp:
# 				if current < S[0][1]:
# 					value = S[0][0]
# 					current = S[0][1]
# 					y = S[1]	

# 			table[y] = 1
# 			result.append(value)
# 		else:
# 			result.append(lines[i])
# 	lines = result
# 	print "length1 = ", len(result)

# s1 = overlap(result[0], result[1])
# print s1[0]
# for e in result:
# 	print e		


# x = len(result)
# table = []
# for i in range(x):
# 	table.append(0)
# result2 = []
# for i in range(x -1):
# 	temp = []
# 	table[i] = 2
# 	for j in range(i + 1,x):
# 		# print i, j
# 		if (table[j] == 0):
# 			S = overlap(result[i],result[j])
# 			if S != None:
# 				# print "s1 = ", result[i]
# 				# print "s2 = ", result[j]
# 				# print S[0],", overlap = ", S[1]
# 				temp.append((S,j))
		
# 	current = 0
# 	if len(temp) != 0:
# 		value = temp[0][0]
# 		y = temp[0][1]
# 		for S in temp:
# 			if current < S[0][1]:
# 				value = S[0][0]
# 				current = S[0][1]
# 				y = S[1]	

# 		table[y] = 1
# 		result2.append(value)
# 	else:
# 		result2.append(result[i])

# print "length2 = ", len(result2)
# s1 = overlap(result2[0],result2[1])
# print s1[0]

# x = len(result2)
# table = []
# for i in range(x):
# 	table.append(0)
# result3 = []
# for i in range(x -1):
# 	temp = []
# 	table[i] = 2
# 	for j in range(i + 1,x):
# 		# print i, j
# 		if (table[j] == 0):
# 			S = overlap(result2[i],result2[j])
# 			if S != None:
# 				# print "s1 = ", result2[i]
# 				# print "s2 = ", result2[j]
# 				# print S[0],", overlap = ", S[1]
# 				temp.append((S,j))
		
# 	current = 0
# 	if len(temp) != 0:
# 		value = temp[0][0]
# 		y = temp[0][1]
# 		for S in temp:
# 			if current < S[0][1]:
# 				value = S[0][0]
# 				current = S[0][1]
# 				y = S[1]	

# 		table[y] = 1
# 		result3.append(value)
# 	else:
# 		result3.append(result2[i])

# print "length3 = ", len(result3)


# x = len(result3)
# table = []
# for i in range(x):
# 	table.append(0)
# result4 = []
# for i in range(x -1):
# 	temp = []
# 	table[i] = 2
# 	for j in range(i + 1,x):
# 		# print i, j
# 		if (table[j] == 0):
# 			S = overlap(result3[i],result3[j])
# 			if S != None:
# 				# print "s1 = ", result3[i]
# 				# print "s2 = ", result3[j]
# 				# print S[0],", overlap = ", S[1]
# 				temp.append((S,j))
		
# 	current = 0
# 	if len(temp) != 0:
# 		value = temp[0][0]
# 		y = temp[0][1]
# 		for S in temp:
# 			if current < S[0][1]:
# 				value = S[0][0]
# 				current = S[0][1]
# 				y = S[1]	

# 		table[y] = 1
# 		result4.append(value)
# 	else:
# 		result4.append(result3[i])

# print "length4 = ", len(result4)


# x = len(result4)
# table = []
# for i in range(x):
# 	table.append(0)
# result5 = []
# for i in range(x -1):
# 	temp = []
# 	table[i] = 2
# 	for j in range(i + 1,x):
# 		# print i, j
# 		if (table[j] == 0):
# 			S = overlap(result4[i],result4[j])
# 			if S != None:
# 				temp.append((S,j))
		
# 	current = 0
# 	if len(temp) != 0:
# 		value = temp[0][0]
# 		y = temp[0][1]
# 		for S in temp:
# 			if current < S[0][1]:
# 				value = S[0][0]
# 				current = S[0][1]
# 				y = S[1]	

# 		table[y] = 1
# 		result5.append(value)
# 	else:
# 		result5.append(result4[i])

# print "length5 = ", len(result5)


# x = len(result5)
# table = []
# for i in range(x):
# 	table.append(0)
# result6 = []
# for i in range(x -1):
# 	temp = []
# 	table[i] = 2
# 	for j in range(i + 1,x):
# 		# print i, j
# 		if (table[j] == 0):
# 			S = overlap(result5[i],result5[j])
# 			if S != None:
# 				temp.append((S,j))
		
# 	current = 0
# 	if len(temp) != 0:
# 		value = temp[0][0]
# 		y = temp[0][1]
# 		for S in temp:
# 			if current < S[0][1]:
# 				value = S[0][0]
# 				current = S[0][1]
# 				y = S[1]	

# 		table[y] = 1
# 		result6.append(value)
# 	else:
# 		result6.append(result5[i])

# print "length6 = ", len(result6)

# s1 = overlap(result6[0],result6[1])
# print s1[0]

















# print len(result)

# for i in range(len(lines)):
# 	# s1 = overlap(s1,lines[i])
# 	print lines[i]
# print s1






# print len(lines)
# table = []
# for i in range(len(lines)):
# 	table.append(0)
# # print "linessss",range(lines)

# for i in range(len(lines) - 1):
# 	# table[i] = 1
# 	for j in range(i+1,len(lines)):
# 		# print i, j
# 		if(table[j] == 0):
# 			temp = overlap(lines[i],lines[j])
# 			if temp != None:	
# 				# if temp[1] == 1:
# 				# 	if temp[2]:
# 				# 		# lines.remove(i)
# 				# 		result.append(temp[0])
# 				# 	else:
# 				# 		lines.remove(j)
# 				# elif temp[1] == 2:
# 				# 	if temp[2]:
# 				# 		lines.remove(i)
# 				# 		lines.remove(j)
# 				# print temp
# 				result.append(temp)
# 				# lines.pop(i)
# 				# lines.pop(j)
# 				table[j] = 1
# 				table[i] = 1
# 				break
# 	if table[i] != 1:
# 		table[i] = 2

# for i in range(len(table)):
# 	if table[i] == 2:
# 		result.append(lines[i])
# 	# print "table = ", table[i]
# # for e in result:
# # 	print e
# print "lenght1 = ", len(result)

# # s1 = result[0]
# # for i in range(1,len(result)):
# # 	s1 = overlap(s1,result[i])


# # print s1
# result2 = []
# table = []
# for i in range(len(result)):
# 	table.append(0)

# for i in range(len(result) - 1):
# 	for j in range(i+1,len(result)):
# 		# print i, j
# 		if(table[j] == 0):
# 			temp = overlap(result[i],result[j])
# 			if temp != None:	
# 				result2.append(temp)
# 				table[j] = 1
# 				break

# for i in range(len(table)):
# 	if table[i] == 2:
# 		result2.append(result[i])

# print "lenght2 = ", len(result2)



# result3 = []
# table = []
# for i in range(len(result2)):
# 	table.append(0)

# for i in range(len(result2) - 1):
# 	for j in range(i+1,len(result2)):
# 		# print i, j
# 		if(table[j] == 0):
# 			temp = overlap(result2[i],result2[j])
# 			if temp != None:	
# 				result3.append(temp)
# 				table[j] = 1
# 				break
# for i in range(len(table)):
# 	if table[i] == 2:
# 		result3.append(result2[i])

# print "lenght3 = ", len(result3)



# result4 = []
# table = []
# for i in range(len(result3)):
# 	table.append(0)

# for i in range(len(result3) - 1):
# 	for j in range(i+1,len(result3)):
# 		# print i, j
# 		if(table[j] == 0):
# 			temp = overlap(result3[i],result3[j])
# 			if temp != None:	
# 				result4.append(temp)
# 				table[j] = 1
# 				break
# for i in range(len(table)):
# 	if table[i] == 2:
# 		result4.append(result3[i])

# print "lenght4 = ", len(result4)
# # print result4[0]


# result5 = []
# table = []
# for i in range(len(result4)):
# 	table.append(0)

# for i in range(len(result4) - 1):
# 	for j in range(i+1,len(result4)):
# 		# print i, j
# 		if(table[j] == 0):
# 			temp = overlap(result4[i],result4[j])
# 			if temp != None:	
# 				result5.append(temp)
# 				table[j] = 1
# 				break
# for i in range(len(table)):
# 	if table[i] == 2:
# 		result5.append(result4[i])

# print "lenght5 = ", len(result5)
# print result5[1]








