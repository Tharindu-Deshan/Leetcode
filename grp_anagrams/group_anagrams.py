def group_anagrams(strs):
    def is_anagram(str1,str2):
        if(len(str1)!=str2):
            return False
        similar_chars_in_str1_dict ={}
        similar_chars_in_str2_dict ={}
        for char in str1:
            if(char in similar_chars_in_str1_dict):
                similar_chars_in_str1_dict[char]+=1
            else:
                similar_chars_in_str1_dict[char]=1
                
        for char in str2:
            if(char in similar_chars_in_str2_dict):
                similar_chars_in_str2_dict[char]+=1
            else:
                similar_chars_in_str2_dict[char]=1
        
        if(len(similar_chars_in_str2_dict) != len(similar_chars_in_str1_dict)):
            return False

        for key in similar_chars_in_str1_dict:
            if(similar_chars_in_str1_dict.get(key,0) != similar_chars_in_str2_dict.get(key,0)):
                return False
        else:
            return True
    
    anagram_dict = {}

    
        
        
        

