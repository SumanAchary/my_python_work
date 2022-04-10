def removeDuplicates(head):
    if head is None or head.next is None:
        return head
    hash = set()

    current = head
    hash.add(head.data)

    while current.next is not None:

        if current.next.data in hash:
            current.next = current.next.next
        else:
            hash.add(current.next.data)
            current = current.next

    return head


def findNode(head, n):
    count = 0
    found = False
    while head is not None:
        if head.data == n:
            found = True
            return count
        head = head.next
        count += 1
    if found:
        return count
    return -1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# this is the implemented function definition
def printReverse(head):
    if head is None:
        return None
    printReverse(head.next)
    print(head.data, end=' ')


def appendLastNToFirst(head, n):
    if n == 0 or head is None:
        return head
    f = head
    s = head
    initial = head
    for i in range(n):
        f = f.next
    while f.next is not None:
        s = s.next
        f = f.next
    temp = s.next
    s.next = None
    f.next = initial
    head = temp
    return head


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def deleteNodeRec(head, pos):
    if head is None:
        return None
    if pos == 0:
        if head is None:
            return head
        head = head.next
        return head  # this line

    small_head = deleteNodeRec(head.next, pos - 1)
    head.next = small_head
    return head


def insert_recursive(head, position, data):
    if position < 0:
        return head
    if position == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    if head is None:
        return None
    small_head = insert_recursive(head.next, position - 1, data)
    head.next = small_head
    return head


def take_input():
    input_list = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for curr_data in input_list:
        if curr_data == -1:
            break
        newNode = Node(curr_data)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


def print_linked_list(head):
    if head is None:
        return head
    while head is not None:
        print(head.data, end=' --> ')
        head = head.next


head = take_input()
print(print_linked_list(head))
appendLastNToFirst(head, 3)
print("AFTER append last @ 3 position")
print(print_linked_list(head))
