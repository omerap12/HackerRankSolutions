# https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true

def pairs(k, arr):
	used_pairs = set()
	set_arr = set(arr)
	for number in arr:
		if number - k in set_arr:
			used_pairs.add((number - k, number))
	return len(used_pairs)
