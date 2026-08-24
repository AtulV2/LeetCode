# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        visited = []
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                visited.append(root.val)
            return None
        dfs(root)
        return visited



        