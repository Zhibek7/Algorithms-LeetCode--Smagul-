# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        
        def postorder(node):
            if node:
                # 1. Обойти левое поддерево
                postorder(node.left)
                # 2. Обойти правое поддерево
                postorder(node.right)
                # 3. Обработать текущий узел x
                r.append(node.val)
                
        postorder(root)
        return r 