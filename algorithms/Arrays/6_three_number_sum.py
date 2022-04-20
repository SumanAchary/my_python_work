def skipMdeleteN(head, M, N) :
    if M == 0 or head is None :
        return None
    if N == 0 :
        return head
    currentNode = head
    temp = None
    while currentNode is not None :
        take = 0
        skip = 0
    while currentNode is not None and take < M :
        if temp is None :
            temp = currentNode
        else :
            temp.next = currentNode
            temp = currentNode
        currentNode = currentNode.next
        take += 1
    while currentNode is not None and skip < N :
        currentNode = currentNode.next
        skip += 1
    if temp is not None :
        temp.next = None
    return head