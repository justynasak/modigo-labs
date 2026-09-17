def is_balanced(text):
    # TODO: return True if all brackets in `text` are properly matched and nested,
    # False otherwise. Ignore non-bracket characters
    pairs = {')': '(',']':'[','}':'{'}
    stack = []
    for char in text:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack