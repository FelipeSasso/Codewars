__author__ = "Felipe Coral Sasso"

"""
Description:

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

"""

import string

def high(x):
	
	highest = 0
	result = ""
	
	for i in x.split(" "):
		cur = sum(map(string.lowercase.index, list(i)))
		if cur > highest:
			result = i
			highest = cur
	
	return result
