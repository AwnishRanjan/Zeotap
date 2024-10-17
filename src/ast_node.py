class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type 
        self.left = left
        self.right = right
        self.value = value
        
    def __repr__(self):
        return f"Node(type={self.type}, left={self.left}, right={self.right}, value={self.value})"
