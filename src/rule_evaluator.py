def evaluate_condition(field, operator, value, data):
    if operator == '>':
        return data.get(field, 0) > value
    elif operator == '<':
        return data.get(field, 0) < value
    elif operator == '=':
        return data.get(field) == value
    return False

def evaluate_rule(ast, data):
    if ast.type == 'operator':
        if ast.value == 'AND':
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == 'OR':
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    elif ast.type == 'operand':
        field, operator, value = ast.value
        return evaluate_condition(field, operator, value, data)
