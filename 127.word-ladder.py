#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        if beginWord in words:
            words.remove(beginWord)

        n = range(len(beginWord))
        alp = 'abcdefghijklmnopqrstuvwxyz'

        def loop(variant,curr):
            nonlocal words
            words.remove(variant)
            return (variant,curr)

        def bfs(node):
            nonlocal words
            q = deque([(node,1)])
            while q:
                node,curr = q.popleft()
                if node == endWord:
                    return curr
                curr+=1
                q.extend([loop(variant,curr) for variants in [[node[0:i]+c+node[i+1:] for i in n if node[0:i]+c+node[i+1:] in words] for c in alp] for variant in variants if variant != node])
            return 0

        return bfs(beginWord)
# @lc code=end