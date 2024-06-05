from minimal_tree import *
from linked_list import *


#assume to create a minimal height binary tree just for look :))
def createBinaryTree(array: list) -> TreeNode:
    return createMinimalBST(array, 0, len(array) - 1)

# Implement a simple modification of the pre-order traversal algorithm, where we pass in level +
# 1 to the next recursive call
def createLinkedListByLevel(root: TreeNode, lists: list[LinkedList], level: int):
    if root == None:
        return
    
    if len(lists) == level:
        #means that it is the first time to meet this list to add
        ll = LinkedList()
        lists.append(ll)
    else:
        lists[level].insert_at_end(root.val)
    
    createLinkedListByLevel(root.left, lists, level +1)
    createLinkedListByLevel(root.right, lists, level +1)
