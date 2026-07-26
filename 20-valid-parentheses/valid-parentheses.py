class Solution(object):
    # another problem solved
    
    def isValid(self, s):
        stack=[]
        for bracket in s:
            if bracket =="(" or bracket =="{" or bracket =="[":
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                character =stack.pop()
                if(
                (bracket==")" and character=="(") or (bracket=="}" and character=="{") or (bracket=="]" and character=="[")
                ):
                   continue
                else:
                    return False
        return len(stack)==0