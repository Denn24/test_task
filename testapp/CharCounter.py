from collections import Counter

def calcCount(str):
   charSet = set(str)
   map = {}
   counter = Counter(str)
   for char in charSet:
       if char == " ":
           continue
       map.update({char: counter[char]})
   return map
