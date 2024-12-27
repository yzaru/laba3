class Node:
    def __init__(self, value, priority=0):
        self.value = value
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def add(self, value, priority):
        new_node = Node(value, priority)
        if self.head is None or self.head.priority < priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self):
        if self.head is None:
            print("Очередь пуста")
            return
        removed = self.head
        self.head = self.head.next
        return removed.value

    def display(self):
        current = self.head
        if not current:
            print("Очередь пуста")
            return
        while current:
            print(f"{current.value} (priority {current.priority})", end=" -> ")
            current = current.next
        print("None")


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def dequeue(self):
        if self.head is None:
            print("Очередь пуста")
            return
        removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed.value

    def display(self):
        current = self.head
        if not current:
            print("Очередь пуста")
            return
        while current:
            print(f"{current.value}", end=" -> ")
            current = current.next
        print("None")


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Стек пуст")
            return
        removed = self.head
        self.head = self.head.next
        return removed.value

    def display(self):
        current = self.head
        if not current:
            print("Стек пуст")
            return
        while current:
            print(f"{current.value}", end=" -> ")
            current = current.next
        print("None")


# Тестирование PriorityQueue
print("--- Priority Queue ---")
priority_queue = PriorityQueue()
priority_queue.add("Task1", 1)
priority_queue.add("Task2", 3)
priority_queue.add("Task3", 2)
priority_queue.display()
priority_queue.remove()
priority_queue.display()

# Тестирование Queue
print("--- Queue ---")
queue = Queue()
queue.enqueue("Item1")
queue.enqueue("Item2")
queue.enqueue("Item3")
queue.display()
queue.dequeue()
queue.display()

# Тестирование Stack
print("--- Stack ---")
stack = Stack()
stack.push("Element1")
stack.push("Element2")
stack.push("Element3")
stack.display()
stack.pop()
stack.display()
