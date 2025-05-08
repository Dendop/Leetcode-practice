class Solution:
    def method(self, n:int) -> int:
        result = []
        while n > 0:
            magic = n % 2
            if magic == 1:
                result.append(magic)
            n = n // 2
        return len(result)

def main():
    sol = Solution()
    
    print(sol.method(1234))
    
if __name__ == "__main__":
    main()
