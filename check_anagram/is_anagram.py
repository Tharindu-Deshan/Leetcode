def is_anagram(str1,str2):
    count=[0]*26
    for i in str1:
        char_idx = ord(i)-97
        count[char_idx]+=1
    for i in str2:
        char_idx = ord(i)-97
        count[char_idx]-=1
    for i in count:
        if(i!=0):
            return False
    return True