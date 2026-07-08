def first_non_repeating_char(str):
    char_freq_dict={}
    for i in str:
        if(i in char_freq_dict):
            char_freq_dict[i]+=1
        else:
            char_freq_dict[i]=1
    
    for i in char_freq_dict.keys():
        if(char_freq_dict[i]==1):
            return i
    return None

print(first_non_repeating_char("hellowwod"))


#l:[0,1],k:[1,6]

def firstUniqChar(s):
    char_idx_freq_dict={}
    for i in range(len(s)):
        if(s[i] not in char_idx_freq_dict):
            char_idx_freq_dict[s[i]]=[i,1]
        else:
            char_idx_freq_dict[s[i]][1]+=1
    for i in char_idx_freq_dict:
        if(char_idx_freq_dict[i][1]==1):
            return i
    return -1