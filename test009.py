def main():
    nums = [1, 2 ,3 ,3]
    target = 5
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i,j])
            
    
if __name__ == "__main__":
    main()