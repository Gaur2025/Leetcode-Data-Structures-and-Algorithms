class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # we can store alphabets of s in a queue. and then check 1st element of q in t
        if len(s) == 0:
            return True 
        
        if len(s) > len(t):
            return False


        q = collections.deque()
        for ch in range(len(s)):
            q.append(s[ch])

        # q = []


        for j in range(len(t)):
            if t[j] == q[0]:
                q.popleft()
            if len(q) == 0:
                return True

            

        
        return False

        

        