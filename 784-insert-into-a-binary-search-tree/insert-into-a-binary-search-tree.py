# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Если достигли NIL, создаем и возвращаем новый узел
        if not root:
            return TreeNode(val)
        
        # Сравниваем вставляемое значение со значением узла
        if val < root.val:
            # Идем в левое поддерево
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Идем в правое поддерево
            root.right = self.insertIntoBST(root.right, val)
            
        return root