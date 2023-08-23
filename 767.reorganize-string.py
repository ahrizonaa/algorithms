#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        freq = Counter(s)
        ans = []
        letters = ''.join([c*n for c,n in sorted(freq.items(), reverse=True, key=lambda tup:tup[1])])
        mid = math.ceil(len(letters)/2)
        
        for i in range(mid):
            ans.append(letters[i])
            if i+mid<len(letters):
                if ans[-1]==letters[i+mid]:
                    return ''
                ans.append(letters[i+mid])
        
        return ''.join(ans)
# @lc code=end

