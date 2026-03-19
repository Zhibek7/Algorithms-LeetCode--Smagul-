class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                # Если это число, кладем в стек
                stack.append(int(token))
            else:
                # Если оператор, достаем два операнда (первый извлеченный - правый операнд)
                num2 = stack.pop()
                num1 = stack.pop()
                
                # Выполняем операцию и кладем результат обратно
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # int() в Python обрезает дробную часть к нулю, что и требуется
                    stack.append(int(num1 / num2))
                    
        # Итоговый результат останется единственным элементом в стеке
        return stack[0]