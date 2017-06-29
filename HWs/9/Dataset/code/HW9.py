import operator 
import fileinput


def overlap(s1,s2): #O(k^2n^2)
	if len(s1) < len(s2):
		s1,s2 = s2, s1
	if len(s2) == 0:
		return s1

	if s2 in s1: 
		return (s1, len(s2))

	k = ("", 0,0) # keep track of the most number of over lap between 2 substrings .
	# 0: string overlap, 1: number of overlap, 2: type of overlap

	for i in xrange(len(s1) - len(s2), len(s1)): 
		if s1[i:] == s2[:len(s1) - i]:
			if k[1] < (len(s1)- i):
				k = (i, len(s1)- i,2)



	for i in xrange(0,-len(s2) , -1):
		if s1[:len(s2) + i] == s2[-i:]:
			if k[1] < (len(s2) + i):
				k = (i,len(s2)+ i, 3)

	if k[1] == 0:
		return None

	if k[2] == 2:
		index = k[0]
		return (s1[:index] + s2, k[1])
	else:
		index = k[0]
		return (s2[:-index] + s1, k[1])


close = set([])
lines = []
for line in fileinput.input():
    line = line.strip() # Remove the trailing newline
    if line not in close:
		close.add(line)
		lines.append(line)

while(len(lines) > 2):
	x = len(lines)
	s1 = lines[0]
	temp = []
	k = ("",0,0)
	for i in range(1,x):
		S = overlap(s1,lines[i])
		if S != None:
			temp.append((S[0],S[1],i))
			if k[1] < S[1]:
				k = (S[0],S[1],i)

	if k[1] != 0:
		lines.pop(k[2])    # remove the element of the # of max overlap 
		lines = lines[1:]  # remove the 1st element in the lines list
		lines.append(k[0]) # add the new substring to the end of the lines list
	else:
		lines = lines[1:]   # remove the 1st element in the lines list
		lines.append(s1)	# add it to the end of the lines list

if len(lines) == 2:
	print "Hello"
	s1 = overlap(lines[0], lines[1])
	print s1[0]
else:
	print lines[0]







