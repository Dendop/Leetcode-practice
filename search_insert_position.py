def main():
    nums = [1, 3, 5, 6]
    target = 7
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return left
            

if __name__ == "__main__":
    main()