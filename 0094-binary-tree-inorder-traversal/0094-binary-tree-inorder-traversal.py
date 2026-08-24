class Solution(object):
    def inorderTraversal(self, root):
        visited = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)       
            visited.append(node.val) 
            inorder(node.right)      

        inorder(root)

        return visited