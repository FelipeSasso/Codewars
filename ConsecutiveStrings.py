__author__ = "Felipe Coral Sasso"

"""
Description:

You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

"""

def longest_consec(strarr, k):
	
	a = len(strarr)
	longest = ""
	
	for i in range(0, a-k+1, 1):
		b = "" 
		for i in range(i, i+k, 1):
			b += strarr[i]
	
		longest = b if len(b) > len(longest) else longest
	return longest
