__author__ = "Felipe Coral Sasso"

"""
Description:

Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Every space should stay, so you cannot use words from Prelude.

Example:

reverseWords("This is an example!"); // returns  "sihT si na !elpmaxe"
reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
reverseWords "An example!"    -- "nA !elpmaxe"
reverseWords "double  spaces" -- "elbuod  secaps"
"""

def reverse_words(str):
    return " ".join(map(lambda x: x[::-1], [i for i in str.split(" ")]))
    
