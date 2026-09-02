class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        
        stack_list = []

        if len(s)==1:
            return False

        for char in s:
            if char in lookup:
                stack_list.append(char)
            else:
                if not stack_list:
                    return False

                x = stack_list.pop()
                if lookup.get(x) != char:
                    return False

        
        return len(stack_list) == 0