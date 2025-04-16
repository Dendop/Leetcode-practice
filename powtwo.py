class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        for i in range(30):
            result = 2 ** i
            if result == n:
                return True
        return False
    """
    return True if n is power of two, else return false
    Example 1:

    Input: n = 1
    Output: true
    Explanation: 20 = 1
    Example 2:

    Input: n = 16
    Output: true
    Explanation: 24 = 16
    Example 3:

    Input: n = 3
    Output: false
     
    """
    
    
    
def main():
    sol = Solution()
    magic = sol.isPowerOfTwo(8)
    print(magic)
    

if __name__ == "__main__":
    main()