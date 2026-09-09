class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create(values, index):
    if index >= len(values) or values[index] == "-":
        return None

    root = Node(values[index])

    root.left = create(values, 2 * index + 1)
    root.right = create(values, 2 * index + 2)

    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


n = int(input())
values = input().split()

root = create(values, 0)

print("Inorder:", end=" ")
inorder(root)
print()

print("Postorder:", end=" ")
postorder(root)
print()