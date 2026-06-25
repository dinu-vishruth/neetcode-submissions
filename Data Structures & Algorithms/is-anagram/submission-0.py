class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        f2={}
        for i in t:
            f2[i]=f2.get(i,0)+1
        return f==f2