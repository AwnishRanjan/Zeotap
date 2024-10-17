# from ast_node import Node
class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type 
        self.left = left
        self.right = right
        self.value = value
        
    def __repr__(self):
        return f"Node(type={self.type}, left={self.left}, right={self.right}, value={self.value})"
    
def parse_condition(condition):
    condition = condition.strip()
    if '>' in condition:
        field, value = condition.split('>')
        return field.strip(), '>', int(value.strip())
    elif '<' in condition:
        field, value = condition.split('<')
        return field.strip(), '<', int(value.strip())
    elif '=' in condition:
        field, value = condition.split('=')
        return field.strip(), '=', value.strip().replace("'", "")
    else:
        raise ValueError(f"Invalid condition format: {condition}")

def create_rule(rule_string):
    rule_string = rule_string.strip()

    if 'AND' in rule_string:
        parts = rule_string.split(' AND ')
        left = create_rule(parts[0].strip())
        right = create_rule(parts[1].strip())
        return Node(type='operator', left=left, right=right, value='AND')
    elif 'OR' in rule_string:
        parts = rule_string.split(' OR ')
        left = create_rule(parts[0].strip())
        right = create_rule(parts[1].strip())
        return Node(type='operator', left=left, right=right, value='OR')
    else:
        field, operator, value = parse_condition(rule_string)
        return Node(type='operand', value=(field, operator, value))
