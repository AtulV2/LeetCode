class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        
        substr = ""
        for i in range(len(strs[0])):
            
            temp_substr = strs[0][0:i+1]

            add = True
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or temp_substr != strs[j][0:i+1]:              
                    add = False
                    break 

            if add:
                substr = temp_substr 
            else:
                break
                
        return substr