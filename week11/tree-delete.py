# case 1: 삭제하려는 노드가 단말 노드인 경우
def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None

    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    return root


# case 2: 자식이 하나인 노드 삭제
def delete_bst_case2(parent, node, root):
    if node.left is not None
        child = node.left

    else:
        child = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child

    return root

# case 3: 자식이 둘 이상인 노드 삭제
def delete_bst_case3(parent, node, root):
    succp = node
    suucc = node.right
    while (succ.left != None):
        succp = succ
        succ = succ.left

    if (succp.left == succ):
        succp.left = succ.right
    node.key = succ.key
    node.value = succ.value
    return root

