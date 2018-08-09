import time

def anagram1(first, second):
	start_time = time.time()
	first = first.replace(' ', '').lower()
	second = second.replace(' ', '').lower()
	if len(first) == len(second):
		for c in first:
			if c not in second:
				return False
		print('Anagram 1 take: ' + str(time.time() - start_time))
		return True
	return False

def anagram2(first, second):
	start_time = time.time()
	first = first.replace(' ', '').lower()
	second = second.replace(' ', '').lower()
	if len(first) != len(second):
		return False
	if sorted(first) == sorted(second):
		print('Anagram 2 take: ' + str(time.time() - start_time))
		return True
	else:
		return False


print(anagram1('GoD', 'dog'))
print(anagram2('GoD', 'dog'))