function is_anagram(str1,str2){
    const count=Array(26).fill(0);
    for(i=0;i<str1.length;i++){
        idx=str1.charCodeAt(i)-97
        count[idx]+=1
    }
    for(i=0;i<str2.length;i++){
        idx=str2.charCodeAt(i)-97
        count[idx]-=1
    }
    console.log(count)
    for (i=0;i<26;i++){
        if(count[i]!=0){
            return false
        } 
    }
    return true
}


console.log(is_anagram("hi","ih"))