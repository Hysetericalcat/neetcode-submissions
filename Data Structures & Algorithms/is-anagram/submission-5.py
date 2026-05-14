class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set(s)
        t_set = set(t)
        if len(s_set)!=len(t_set):
            return False
        len_ = len(s_set)
        for char in s_set :
           if s.count(char)!=t.count(char):
              return False
        return True