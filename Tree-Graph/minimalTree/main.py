from minimal_tree import *

def inOrderTraversal(root):
    if root == None:
        return

    inOrderTraversal(root.left)
    print(root.val, " ")
    inOrderTraversal(root.right)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    minimalTree = createMinimalBST(arr, 0, len(arr)-1)

    inOrderTraversal(minimalTree)