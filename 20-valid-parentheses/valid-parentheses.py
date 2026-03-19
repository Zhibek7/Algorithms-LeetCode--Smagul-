class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Словарь для быстрого поиска парных скобок
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping: # Если текущий символ - закрывающая скобка
                # Извлекаем верхний элемент стека
                top_element = stack.pop() if stack else '#'
                
                # Если извлеченный элемент не совпадает с ожидаемой открывающей скобкой, возвращаем False
                if mapping[char] != top_element:
                    return False
            else:
                # Если это открывающая скобка, помещаем ее в стек (PUSH)
                stack.append(char)
                
        # Если стек пуст, все скобки были закрыты правильно
        return not stack