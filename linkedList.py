class Node:

    def __init__(self, num, nextNode):
        self.num = num              #self is property of object
        self.nextNode = nextNode

class Product:

    def __init__(self, title, rating, isDeal, price, isPrime, delivery, nextProduct):
        self.title = title
        self.rating = rating
        self.deal = isDeal
        self.price = price
        self.discount = isPrime
        self.delivery = delivery
        self.nextProduct = nextProduct
class LinkedList:

    head = None                 # property of class not object... not the case in java
    lastNode = None
    __size = 0

    def append(self, object):

        LinkedList.__size += 1
        node = Node(object, None)
        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        if LinkedList.head is None:
            LinkedList.head = node
            LinkedList.tail = node
            print(">> [APPEND] LinkedList.head:", LinkedList.head, "[NEXT NODE]:", LinkedList.head.nextNode)
            print(">> [APPEND] LinkedList.tail:", LinkedList.tail)
        else:
            LinkedList.tail.nextNode = node
            print(">> [APPEND] LinkedList.tail.nextNode:", LinkedList.tail.nextNode)
            LinkedList.tail = node
            print(">> [APPEND] LinkedList.tail:", LinkedList.tail)

        print()

    def appendBeginning(self, object):

        LinkedList.__size += 1
        node = Node(object, None)
        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        temp = LinkedList.head
        LinkedList.head = node
        node.nextNode = temp

        print()

    def printList(self):

        temp = LinkedList.head

        while temp.nextNode is not None:
            print(temp.num)
            temp = temp.nextNode

        print(temp.num)

    def size(self):
        return LinkedList.__size

# Lets Create Node Object
# node = Node(85, None)

# Object of LinkedList
lRef = LinkedList()

lRef.append(85)
lRef.append(80)
lRef.append(55)
lRef.append(78)

lRef.printList()

lRef.appendBeginning(98)

lRef.printList()

print(">> Size of Linked List is:", lRef.size())
