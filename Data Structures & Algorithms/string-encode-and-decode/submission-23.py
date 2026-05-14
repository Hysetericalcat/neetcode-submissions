class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i,word in enumerate(strs):
            length = len(word)
            s = str(len(word))+ "#" + word
            encoded_string=encoded_string+s
        print(encoded_string)
        return encoded_string    


    def decode(self, s: str) -> List[str]:
        output_array = []
        seen = []
        str_list = list(s)
        last_index=0
        i = 0
        while(i<len(s)):
            if str_list[i] == "#" :
                word_len = int(s[last_index:i])
                output_array.append(s[i+1:i+word_len+1])
                last_index = i+word_len+1
                i =  last_index
            i = i + 1
        return output_array
                   


              

        