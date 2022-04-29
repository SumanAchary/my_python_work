def reverseStack(s1,s2):
    if len(s1) <= 1:
        return
    while(len(s1) != 1):
        ele = s1.pop()
        s2.append(ele)
    lastElement = s1.pop()
    while(len(s1) != 0):
        ele = s2.pop()
        s1.append(ele)
    reverseStack(s1,s2)
    s1.append(lastElement)