def modify_operator(ast, new_operator):
    if ast.type == 'operator':
        ast.value = new_operator
    else:
        raise ValueError("Can't modify operator of an operand node.")
