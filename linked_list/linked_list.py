#!/usr/bin/python
"""Linked list sandbox"""

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

linked_list = SinglyLinkedList()
node1 = Node(1)
node2 = Node(2)

linked_list.head = node1
linked_list.head.next = node2
linked_list.tail = node2
