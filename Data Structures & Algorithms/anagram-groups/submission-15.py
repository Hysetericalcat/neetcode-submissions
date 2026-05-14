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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr_ = []
        seen = {}
        for i in range(0,len(strs)):
            arr = []
            for j in range(0,len(strs)):
                if j in seen:
                    continue
                if self.isAnagram(strs[i],strs[j]):
                   arr.append(strs[j])
                   seen[j] = True
            if len(arr) == 0:
                continue
            arr_.append(arr)
        return arr_
                   
        
            
                
