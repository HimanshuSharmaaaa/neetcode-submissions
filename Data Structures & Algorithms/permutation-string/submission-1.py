class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        need={}
        for ch in s1:
            need[ch]=need.get(ch,0)+1

        window={}
        k=len(s1)

        for right in range(len(s2)):
            ch=s2[right]
            window[ch]=window.get(ch,0)+1

            if right>=k:
                out=s2[right-k]
                window[out]-=1
                if window[out]==0:
                    del window[out]

            if window==need:
                return True

        return False                    

         