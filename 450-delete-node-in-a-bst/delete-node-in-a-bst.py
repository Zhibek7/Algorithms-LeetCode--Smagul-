# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Сначала ищем узел для удаления
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Узел найден. 
            
            # Случай 1 и 2: Узла нет левого или правого ребенка
            if not root.left:   # заменяем z его правым ребенком
                return root.right
            elif not root.right: # заменяем z его левым ребенком
                return root.left
            
            # Случай 3: У узла 2 ребенка. Находим преемника в правом поддереве.
            # Преемник - это минимальный элемент в правом поддереве.
            successor = root.right
            while successor.left:
                successor = successor.left
                
            # Заменяем значение текущего узла на значение преемника
            root.val = successor.val
            # Удаляем преемника из правого поддерева
            root.right = self.deleteNode(root.right, successor.val)
            
        return root