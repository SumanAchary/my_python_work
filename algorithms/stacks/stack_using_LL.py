from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data=None) :
        self.data = data
        self.next = None


class Stack :
    #Define data members and __init__()
    def __init__(self):
        self.__head = None
        self.__count = 0
        
    def getSize(self) :
        return self.__count

    def isEmpty(self) :
        if self.__head == None:
            return True
        return False


    def push(self, data) :
        if self.__head == None:
            self.__head = Node(data)
            self.__count += 1
        else:
            new_head = Node(data)
            new_head.next = self.__head
            self.__head = new_head
            self.__count += 1

    def pop(self) :
        if not self.isEmpty():
            top_element = self.__head.data
            self.__head = self.__head.next
            self.__count -= 1
            return top_element
        return -1
    
    def top(self) :
        #Implement the top() function
        if self.__count:
            return self.__head.data
        return -1
#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
