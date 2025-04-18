class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        my_list = [int(d) for d in str(num)]
        result = 0
        for i in my_list:
            result += i
        if result < 10:
            return result
        else:
            return self.addDigits(result)
        
def main():
    sol = Solution()
    magic = sol.addDigits(38)
    print(magic)

if __name__ == "__main__":
    main()
    
'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
'''