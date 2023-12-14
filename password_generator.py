import random

class Solution:
    def shuffle(self,s: str) -> str:
        templist= list(s)
        random.shuffle(templist)

        return "".join(templist)



uppercase= chr(random.randint(65,90))+chr(random.randint(65,90))
lowercase= chr(random.randint(97,122))+chr(random.randint(97,122))
character= chr(random.randint(33,47))+chr(random.randint(33,47))
digit=chr(random.randint(48,57))+chr(random.randint(48,57))



password= uppercase+lowercase+character+digit
sol=Solution()
password=sol.shuffle(password)
print(password)



