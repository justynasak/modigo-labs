def evaluate(expression):
    # TODO: parse and evaluate the arithmetic expression yourself, respecting
    # operator precedence and parentheses. Do not use eval() or exec().
    tokens = tokenize(expression)
    pos = [0]
    
    def peek():
        return tokens[pos[0]] if pos[0] < len(tokens) else None
    
    def advance():
        tok = tokens[pos[0]]
        pos[0] += 1
        return tok

    def parse_factor():
        tok = advance()
        if tok == '(':
            value = parse_expression()
            advance()
            return value
        return float(tok)

    def parse_term():
        value = parse_factor()
        while peek() in ('*','/'):
            op = advance()
            rhs = parse_factor()
            value = value * rhs if op == "*" else value/rhs
        return value

    def parse_expression():
        value = parse_term()
        while peek() in ('+','-'):
            op = advance()
            rhs = parse_term()
            value = value + rhs if op == '+' else value - rhs
        return value

    return parse_expression()

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch == ' ':
            i += 1
        elif ch in '+-/*()':
            tokens.append(ch)
            i += 1
        else:
            j = i
            while j< len(expression) and expression[j].isdigit():
                j += 1
            tokens.append(expression[i:j])
            i = j
    return tokens