class Solution:
    def isPalindrome(self, s: str) -> bool:
        string1 = "".join(i for i in s if i.isalnum())
        string1=string1.lower()

        left,right=0,len(string1)-1

        while left<right:
            if string1[left] != string1[right]:
                return False

            left+=1
            right-=1
        return True