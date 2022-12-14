#! /usr/bin/python

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        numbers = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,\
                  "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        i = 0
        while i < len(s):
            print(s[i])
            if i+2 <= len(s):
                if s[i:i+2] in numbers.keys():
                    print(s[i:i+2])
                    result += numbers[s[i:i+2]]
                    i += 2
                else:
                    result += numbers[s[i]]
                    i += 1
            else:
                result += numbers[s[i]]
                i += 1
        return result
