# Here this works very effectively when the strings of the inputs are long.
#if the strings are very short we can use the "".join(sorted(str)) to make the key of anagram dictionary. 

def anagram_key_efficient(str1):
        alphabet=[0]*26
        for i in str1:
            alphabet_position = ord(i)-97
            alphabet[alphabet_position]+=1
        alphabet_tuple=tuple(alphabet)
        return alphabet_tuple

anagram_dict={}

def group_anagrams(strs):
    for i in strs:
        sorted_str=anagram_key_efficient(i)
        if(sorted_str in anagram_dict):
             anagram_dict[sorted_str].append(i)
        else:
             anagram_dict[sorted_str]=[i]
     
    
    return list(anagram_dict.values())
         



x=["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(x))