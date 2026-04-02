# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        
        def inorder(node):
            if node: # Если узел существует (не равен NIL)
                # 1. Обходим левое поддерево
                inorder(node.left)
                # 2. Обрабатываем текущий узел
                r.append(node.val)
                # 3. Обходим правое поддерево
                inorder(node.right)
                
        inorder(root)
        return r