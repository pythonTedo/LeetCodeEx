def smallestEvenMultiple(self, n: int) -> int:
        if (n % 2 == 0) and (n % n == 0):
            return n
        elif n % n == 0:
            return n*2
        
print(smallestEvenMultiple(5))
'''
Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.
'''
