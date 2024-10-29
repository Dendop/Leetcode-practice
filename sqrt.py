class Solution:
    def mySqrt(self, x: int) -> int:
        num = 1
        while (num * num) < x:
            num += 1
            
        num -= 1
        print(num)
        




def main():
    obj = Solution()
    obj.mySqrt(254)


if __name__ == "__main__":
    main()