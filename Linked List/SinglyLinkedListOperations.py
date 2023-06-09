from ast import Delete
from operator import length_hint
from random import randrange
import math

# Class to create a new node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Class to create a Single Licked List
class LinkedList:

    # Create Empty linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Print the linked list
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    # Append a node at the end of the linked list |  T.C =  O(1) S.C = O(1)
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Insert a node at the beginning of the linked list |  T.C =  O(1) S.C = O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Inserting a new node at given position |  T.C =  O(n) S.C = O(1)
    def insert_at_given_position(self, value, position):
        new_node = Node(value)
        if (position < 0 or position > self.length):
            print("Please enter a valid index")
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif (position == 0):
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(position-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    # Traversing a s singly linked list | T.C = O(n)  S.C = O(1)
    def traverse(self):
        current = self.head
        while (current is not None):
            print(current.value)
            current = current.next

    # Search and element in a single linked list |  T.C = O(n) S.C = O(1)
    def search(self, target):
        current = self.head
        index = 0
        while (current is not None):
            if (current.value == target):
                return index
            current = current.next
            index += 1
        return -1

    # Return the element at specified index
    def get(self, index):
        if index == -1:
            return self.tail.value
        if (index < -1 or index >= self.length):
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    # Set new value for the node
    def set(self, index, newValue):
        if index == -1:
            self.tail.value = newValue
        if (index < -1 or index >= self.length):
            print("Please enter valid index")
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = newValue

    # Remove first node from linked list
    def pop_first(self):
        if self.length == 0:
            print("Linked List is Empty!!")
            return None

        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node.value

        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    # Remove the last node form linked list
    def pop(self):
        if self.length == 0:
            print("Linked List is Empty!!")
            return None

        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node.value

        current = self.head
        while current.next is not self.tail:
            current = current.next
        self.tail = current
        current.next = None
        self.length -= 1
        return popped_node.value

    # Remove node at specified index
    def remove(self, index):
        current = self.head
        if index >= self.length or index < -1:
            print("Please entre valid index")
            return None

        if index == self.length - 1 or index == -1:
            return self.pop()

        if index == 0:
            return self.pop_first()

        for _ in range(index-1):
            current = current.next
        popped_node = current.next
        current.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    # Delete complete linked list
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Reverse the singly linked list - T.C : O(n) S.C : O(1)
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    # Find the the middle node of the linked list - - T.C : O(n) S.C : O(1)
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value


new_linked_list = LinkedList()
new_linked_list.insert_at_given_position(350, 0)

new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)

new_linked_list.prepend(40)
new_linked_list.prepend(50)
new_linked_list.prepend(500)
# new_linked_list.append(80)
print(new_linked_list.__str__())


new_linked_list.insert_at_given_position(100, 2)
new_linked_list.insert_at_given_position(450, 110)

print(new_linked_list.search(100))

print(new_linked_list.length)

print(new_linked_list.__str__())
print(new_linked_list.traverse())
print(new_linked_list.get(3))
print(new_linked_list.get(5))
print(new_linked_list.get(11))
print(new_linked_list.get(-1))

new_linked_list.set(3, 1000)
print(new_linked_list.__str__())

print("Popped Node : ", new_linked_list.pop_first())
print(new_linked_list.__str__())

print("Popped Node : ", new_linked_list.pop())
print(new_linked_list.__str__())


print("Removed Node : ", new_linked_list.remove(3))
print(new_linked_list.__str__())

print(new_linked_list.remove(4))
print(new_linked_list.__str__())

new_linked_list.delete_all()
print(new_linked_list.__str__())

# Please comment above lines with remove() ,pop(), pop_first() and delete_all() function in order to see the proper result of next function calls

new_linked_list.reverse()
print("Reversed Linked List : ", new_linked_list.__str__())

print("Middle node is : ", new_linked_list.find_middle())
