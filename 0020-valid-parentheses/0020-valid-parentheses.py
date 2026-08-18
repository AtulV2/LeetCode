class Solution(object):
    def isValid(self, s):
        
        stack = []
        for symbol in s:
            if symbol in "([{":
                stack.append(symbol)
        
            if symbol == ")":
                stack.append(symbol)
                if len(stack) >= 2 and stack[-2] == "(":
                    stack.pop()
                    stack.pop()
            if symbol == "]":
                stack.append(symbol)
                if len(stack) >= 2 and stack[-2] == "[":
                    stack.pop()
                    stack.pop()
            if symbol == "}":
                stack.append(symbol)
                if len(stack) >= 2 and stack[-2] == "{":
                    stack.pop()
                    stack.pop()


        if len(stack) != 0:
            return False
        else:
            return True


                
    

        