def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    if len(s) % 2 == 1:
        return False
    
    comps = {'(':')', '{':'}', '[':']'}
    
    stack = []

    for i in s:

        if i in comps:
            stack.append(comps[i])
        else:
            if len(stack):
                curr = stack.pop()
                if curr != i:
                    return False
            else:
                return False
    
    return len(stack) == 0

print(isValid("()"))

print(isValid("()[]{}"))

print(isValid("(]"))

print(isValid("([])"))