class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        flag = False
        for index in range(len(s2) - len(s1) + 1):
            substring = s2[index : index + len(s1)]
            if sorted(substring) == sorted(s1):
                flag = True
            if flag == True:
                return True
        return False