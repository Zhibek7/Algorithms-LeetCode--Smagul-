# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, min_val, max_val):
            # Пустое дерево считается валидным
            if not node:
                return True
            
            # Проверяем нарушение основного свойства BST
            if not (min_val < node.val < max_val):
                return False
            
            # Рекурсивно проверяем левое поддерево (оно должно быть меньше node.val)
            # и правое поддерево (должно быть больше node.val)
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        # Для корня границы от минус бесконечности до плюс бесконечности
        return validate(root, float('-inf'), float('inf'))