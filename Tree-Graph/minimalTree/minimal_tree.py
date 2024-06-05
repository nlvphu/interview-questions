from node import Node

# The algorithm is as follows:
# 1. Insert into the tree the middle element of the array.
# 2. Insert (into the left subtree) the left subarray elements.
# 3. Insert (into the right subtree) the right subarray elements.
# 4. Recurse.

def createMinimalBST(array, left, right):
    if left>right:
        return None
    
    mid = (left + right)//2
    
    node = Node(array[mid])

    node.left =  createMinimalBST(array, left, mid - 1)
    node.right = createMinimalBST(array, mid + 1, right)

    return node