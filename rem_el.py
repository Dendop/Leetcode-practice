def main():
    nums = [3, 2, 2, 3]
    val = 2
    
    for i in range(len(nums) -1, -1, -1):
        if val == nums[i]:
            nums.pop(i)
            
    print(nums)
    
    
    
if __name__== "__main__":
    main()