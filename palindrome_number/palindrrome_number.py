def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        for i in range(len(x)//2):
            left=i
            right=len(x)-i-1
            if(x[left]!=x[right]):
                return False
        return True