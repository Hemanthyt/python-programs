
class Solution:
    def reverse_exponentiation(self, n):
        # code here
        reverse = int(str(n)[::-1])
        return pow(n,reverse)