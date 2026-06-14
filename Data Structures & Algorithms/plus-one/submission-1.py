class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mystr = ""
        
        while len(digits) > 0:
            i = 0
            print(digits[i])
            mystr = mystr + "" + str(digits[i]) + ""
            digits.pop(i)
            i += 1
        
        mystr = str(int(mystr) + 1)
        li = []
        for i in range(len(mystr)):
            li.append(mystr[i])
        
        return li


        