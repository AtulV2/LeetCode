class Solution(object):
    def generate(self, numRows):
        stack = []
        for k in range(1,numRows+1):
            if k == 1:
                stack.append([1])
            elif k == 2:
                stack.append([1,1])
            else:

                preArr =  stack[-1]

                temp = [1]
                for i in range(0,len(preArr)-1):
                    sum =  preArr[i] + preArr[i+1]
                    temp.append(sum)
                temp.append(1)

                stack.append(temp)
            
        return stack


