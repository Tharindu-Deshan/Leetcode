def plaindrome(str):
    if(len(str)==0):
        return True
    elif(str[0]!=str[-1]):
        return False
    else:
        return plaindrome(str[1:-1])
print(plaindrome("ghgf"))