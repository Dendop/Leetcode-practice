class Solution:
    def isHappy(self, n: int) -> bool:
        sm_list = [int(d) for d in str(n)]
        if n == 1:
            return True
        else:
            result = 0
            for i in sm_list:
                result += i**2
        
            if result == 1:
                return True
            elif result <= 4:
                return False
            else:
                return self.isHappy(result)
        
def main():

    sol = Solution()
    magic = sol.isHappy(4) ##7 should be true
    print(magic)


if __name__ == "__main__":
    main()

"""
Loop until it's equal 1, if equal == 1 return true else return false
Example 1:
Input: n = 19
Output: true
Explanation:
(1*1) + (9*9) = 82
(8*8) + (2*2) = 68
(6*6) + (8*8) = 100
(1*1) + (0*0) + (0*0) = 1
Example 2:

Input: n = 2
Output: false
"""