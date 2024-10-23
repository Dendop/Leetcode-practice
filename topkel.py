def main():
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    my_dict = {}
    
    for num in nums:
        if num not in my_dict:
            my_dict[num] = []
        my_dict[num].append(num)
            
        
    new_list = list(my_dict.values())
    #print(new_list)
    
    result =[]
    
    for sub in new_list:
        if len(sub) >= k:
            result.append(sub[0])
            
        
    print(result)
    
if __name__ == "__main__":
    main()