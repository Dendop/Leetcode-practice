def main():
    
    nums = [1, 1, 2, 5, 5, 6]
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    
    nums = nums[:j]
    print(j)  
    print(nums)   
   
    
    
if __name__ == "__main__":
    main()