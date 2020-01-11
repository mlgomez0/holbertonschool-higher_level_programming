#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if (type(data) != int):
            raise TypeError("data must be an integer")
        elif (type(next_node) != Node and next_node != None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (type(data) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (type(value) != Node and value != None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        NewNode = Node(value)
        if (self.__head == None):
            self.__head = Node(value)
            return self.__head
        else:
            temp = self.__head
            while (temp.next_node):
                temp = temp.next_node
            temp.next_node = NewNode
            return self.__head
    def lprint(self):
        temp2 = self.__head
        while temp2 is not None:
            print(temp2.__data)
            temp2 = temp2.next_node



