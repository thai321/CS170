
def overlap(s1,s2): #O(k^2n^2)
	if len(s1) < len(s2):
		s1,s2 = s2, s1
	# print "len(s2) = ", len(s2)
	for i in xrange(0,len(s1) - len(s2)):
		if s1[i:i+len(s2)] == s2:
			print "Here1"
			return i, len(s2)

	for i in xrange(len(s1) - len(s2), len(s1)): #inside
		if s1[i:] == s2[:len(s1) - i]:
			print "here2"
			return i, len(s1) - i
	
	for i in xrange(0,-len(s2) , -1):
		if s1[:len(s2) + i] == s2[-i:]:
			print "here3"
			print "s2[",i,",",len(s2) + i ,"] = ", s1[-1] , "  ", s2[-1]
			return i, len(s2) + i
	
	# for i in xrange(0,len(s1) - len(s2)):
	# 	if s1[i:i+len(s2)] == s2:
	# 		return i, len(s2)

	return None
	# 
# def print_overlap(s1,s2):
# 	i = overlap(s1,s2)
# 	if i is None:
# 		print "ERROR"
# 		return

# 	# print s1 + "."* (len(s2) - len(s1) + i)
# 	# print "."*i + s2
# 	print "%3d"%i, s1 + "." *(len(s2) - len(s1) + i)
# 	print "%3d"%i, "."*i + s2

def print_overlap(s1,s2):
	i = overlap(s1,s2)
	if i is None:
		print "ERROR"
		return
	if i[0] >= 0 and i[0] < i[1]:
		if len(s1) > len(s2):
			print s1
		else:
			print s2
	elif i[0] >= 0 and i[0] > i[1]:
		# if len(s1) > len(s2)
		print s1 + s2[i[1]:]

	# print "i = ", i
	# print s2[0:i[0]] + s1[i[1]:]
	# print s1 + "."* (len(s2) - len(s1) + i)
	# print "."*i + s2
	# print "%3d"%i, s1 + "." *(len(s2) - len(s1) + i)
	# print "%3d"%i, "."*i + s2

# print print_overlap("xyabc", "abcd")
# print print_overlap("xxdsdsfsByab","abcd")
# print print_overlap("abcxx","zzab")
# print print_overlap("xyabcdzzz","abcd")
# print overlap("abcxx", "zzab")
# print_overlap("abcxx", "zzab")
# print_overlap("abcde","zabc")

# print overlap("xyabcdzzz", "abcd")
# print overlap("xxdsdsfsByab","abcd")


import difflib
def get_overlap(s1, s2):
    s = difflib.SequenceMatcher(None, s1, s2)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2)) 
    return s1[pos_a:pos_a+size]

# s1 = "CGATTCCAGGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTC"
# s2 = "GGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGC"

# s1 = "TGCCTCGAACTTTCCCGTACCACAG"
# s2 = "TGCCTCGAACTTTCCCGTACCACAGGATTCACGTT"

# s1 = "TGCCTCGAACTTTCCCGTACCACAGGATTCACGTT"
# s2 = "GATTCACGTTGCTAAGGACACGAAA"
s1 = "TGCCTCGAACTTTCCCGTACCACAGGATTCACGTTGCTAAGGACACGAAA"
s2 = "TGCCTCGAACTTTCCCGTACCACAGGA"
print overlap(s1,s2)
print_overlap(s1,s2)
# print s1[0:25]
# s1 = get_overlap(s1, s2)
# s2 = "GATTCACGTTGCTAAGGACACGAAA"
# s1 = get_overlap(s1, s2)

# s2 = "TGCCTCGAACTTTCCCGTACCACAGGA"
# s1 = get_overlap(s1,s2)
# print "s1 = " , s1
# print(get_overlap(s1, s2)) 



