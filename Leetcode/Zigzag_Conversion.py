class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        l = max(len(s), numRows)
        a = ["" for _ in range(l)]
        i = 0
        up = False
        for k in s:
            a[i] += k
            if not up:
                i += 1
            else:
                i -= 1
            
            if i >= numRows:
                up = True
                i -= 2
            
            if i < 0:
                up = False
                i += 2

        result = ''.join(a)

        return result