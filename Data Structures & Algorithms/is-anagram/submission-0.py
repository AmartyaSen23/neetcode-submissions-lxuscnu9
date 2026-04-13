class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        if (len(s)!=len(t)):
            return False
        for i in range(len(s)):
            flag1=0
            flag2=0
            if (s[i] in hash1):
                hash1[s[i]]=hash1[s[i]]+1
                flag1=1
            if (t[i] in hash2):
                hash2[t[i]]=hash2[t[i]]+1
                flag2=1
            if (flag1==0):
                hash1[s[i]]=1
            if (flag2==0):
                hash2[t[i]]=1
        if (hash1==hash2):
            return True
        else:
            return False