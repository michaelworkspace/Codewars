def unique_in_order(iter):
	n = []
	for i in range(len(iter)-1):
		if iter[i] == iter[i+1]:
			continue
		else:
			n.append(iter[i])
	n.append(iter[-1])
	return n

print(unique_in_order([1,2,2,3,3]))
print(unique_in_order('AAAABBBCCDAABBB'))
