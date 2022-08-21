def is_balanced_paran(string):
    s = []
    for char in string:
        if char in "({[":
            s.append(char)
        elif char == ")":
            if not s or s[-1] != "(":
                return False
            s.pop()

        elif char == "}":
            if not s or s[-1] != "{":
                return False
            s.pop()

        elif char == "]":
            if not s or s[-1] != "[":
                return False
            s.pop()

    if not s:
        return True
    return False


string = input()
print(is_balanced_paran(string))
