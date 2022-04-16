class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 0:
            i=0
            j = 1
            set_ = set(s[i])

            max_count = 0

            while j < len(s):
                if s[j] not in set_:
                    set_.add(s[j])
                    j += 1
                else:
                    if max_count < len(set_):
                        max_count = len(set_)

                    set_.remove(s[i])

                    if i == j:
                        i += 1
                        j += 1

                    i += 1

            if max_count < len(set_):
                max_count = len(set_)        

            return max_count
        
        return 0