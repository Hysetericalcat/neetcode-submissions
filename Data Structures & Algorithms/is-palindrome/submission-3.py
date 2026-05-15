class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list(s)
        new_list = []
        for i,letter in enumerate(s_list)  :
            s_list[i] = s_list[i].lower()
            if letter.isalnum():
                new_list.append(s_list[i])
            else:
                print("letter not alphanumeric")    
        print(new_list)
        left = 0
        right = len(new_list)-1
        while(left<right):
            if new_list[left]!=new_list[right]:
               return False
            left+=1
            right = right-1

        return True

