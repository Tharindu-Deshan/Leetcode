def find_duplicates(nums):
    duplicates_list=[]
    freq_dict={}
    for i in nums:
        if(i not in freq_dict):
            freq_dict[i]=1
        else:
            freq_dict[i]+=1
            if(freq_dict[i]==2):
                duplicates_list.append(i)
    return duplicates_list
        
