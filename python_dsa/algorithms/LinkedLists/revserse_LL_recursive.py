def reverseLinkedListRec(head):
    if head is None or head.next is None:
        return head
    small_head = reverseLinkedListRec(head.next)
    curr = small_head
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return small_head


# optimized
def reverseLinkedListRec2(head):
    if head is None or head.next is None:
        return head, head

    smallHead, smallTail = reverseLinkedListRec2(head.next)
    smallTail.next = head
    head.next = None
    return smallHead, smallTail


# boiler plate for LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
        print(head.data, end=" --> ")
        head = head.next


head = take_input()
print(print_linked_list(head))
new = reverseLinkedListRec(head)
print(print_linked_list(new))
