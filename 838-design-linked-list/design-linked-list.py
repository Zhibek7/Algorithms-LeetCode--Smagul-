class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        # Инициализируем фиктивные голову и хвост 
        self.head = ListNode(0)
        self.tail = ListNode(0)
        # Связываем их друг с другом
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        # Добавляем после фиктивной головы
        self._add(self.head, val)

    def addAtTail(self, val: int) -> None:
        # Добавляем перед фиктивным хвостом
        self._add(self.tail.prev, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
            
        curr = self.head
        for _ in range(index):
            curr = curr.next
        # Вставляем элемент после curr
        self._add(curr, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        # Удаляем текущий элемент
        self._delete(curr)

    # Вспомогательная функция для вставки узла после узла node
    def _add(self, node: ListNode, val: int):
        new_node = ListNode(val, node.next, node)
        node.next.prev = new_node
        node.next = new_node
        self.size += 1

    # Вспомогательная функция для удаления конкретного узла
    def _delete(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1