class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(node, result=None):
    if result is None:
        result = []
    if node is not None:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result=None):
    if result is None:
        result = []
    if node is not None:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result


def postorder(node, result=None):
    if result is None:
        result = []
    if node is not None:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)
    return result


def build_tree():
    # Left subtree of 'A' -> 'S'
    h_node = Node("H", Node("J"), Node("U"))
    w_node = Node("W", Node("A"), Node("A"))
    s_node = Node("S", h_node, w_node)

    # Right subtree of 'A' -> 'T'
    l_node = Node("L", Node("A"), Node("Y"))
    d_node = Node("D", Node("A"), None)
    t_node = Node("T", l_node, d_node)

    # Root node 'A'
    return Node("A", s_node, t_node)


if __name__ == "__main__":
    root = build_tree()
    print("Preorder :", " -> ".join(preorder(root)))
    print("Inorder  :", " -> ".join(inorder(root)))
    print("Postorder:", " -> ".join(postorder(root)))