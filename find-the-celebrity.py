# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidates = set([i for i in range(n)])
        eliminated = set()
        left=0
        right=1

        while right < n:
            if knows(left,right):
                eliminated.add(left)
                if left in candidates:
                    candidates.remove(left)
                if right not in eliminated:
                    candidates.add(right)
            else:
                eliminated.add(right)
                if right in candidates:
                    candidates.remove(right)
                if left not in eliminated:
                    candidates.add(left)

            if knows(right,left):
                eliminated.add(right)
                if right in candidates:
                    candidates.remove(right)
                if left not in eliminated:
                    candidates.add(left)
            else:
                eliminated.add(left)
                if left in candidates:
                    candidates.remove(left)
                if right not in eliminated:
                    candidates.add(right)

            if left in eliminated:
                if right in eliminated:
                    left=right+1
                    right=left+1
                else:
                    left=right
                    right+=1
            else:
                right+=1

        if len(candidates)==1 and len(eliminated)==n-1:
            celebrity = candidates.pop()
            del candidates
            del eliminated
            for i in range(celebrity):
                if i != celebrity and knows(celebrity,i):
                    return -1
                if i != celebrity and not knows(i,celebrity):
                    return -1
            return celebrity
        return -1