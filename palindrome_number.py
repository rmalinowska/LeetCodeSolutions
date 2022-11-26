class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        j = len(x) - 1
        while x[i] == x[j]:
            if i == j:
                return True
            elif i+1 == j:
                return True
            else:
                if i < len(x)-1 and j > 0:
                    i += 1
                    j -= 1
                else:
                    break
        return False