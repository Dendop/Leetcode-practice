class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        
def main():
    
    sol = Solution()
    magic = sol.climbStairs(4)
    print(magic)
if __name__ == "__main__":
    main()