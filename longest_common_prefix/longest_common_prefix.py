class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix=""
        is_prefix=True
        index_str=-1
        for i in strs[0]:
            is_prefix=True
            index_str+=1
            for j in strs[1:]:
                if (not(index_str < len(j))):
                    return longest_prefix

                if( i != j[index_str] ):
                    is_prefix=False
                    break
            if(is_prefix):
                longest_prefix+=i
            else:
                return longest_prefix
        return longest_prefix
        

    def longestCommonPrefixEnumeration(self,strs):
        longest_prefix = ""
        if(len(strs)>0):
            first_string= strs[0]
        else:
            return longest_prefix

        for i,char in enumerate(first_string):
            
            for j in strs[1:]:

                if((i>=len(j)) or ((char != j[i]))):
                        return longest_prefix
            longest_prefix+=char
            
        return longest_prefix