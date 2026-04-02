# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        
        def preorder(node):
            if node:
                # 1. Сначала обрабатываем сам узел x
                r.append(node.val)
                # 2. Обойти левое поддерево
                preorder(node.left)
                # 3. Обойти правое поддерево
                preorder(node.right)
                
        preorder(root)
        return r