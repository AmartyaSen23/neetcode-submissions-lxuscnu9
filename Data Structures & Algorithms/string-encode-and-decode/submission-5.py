class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in range(0,len(strs)):
            b=strs[i]
            s+=b;
            s+="😭"
        return s
    def decode(self, s: str) -> List[str]:
        res=[]
        sa=""
        for i in range(0,len(s)):
            if (s[i]=="😭"):
                res.append(sa)
                sa=""
                continue
            sa+=(s[i])
        return res
