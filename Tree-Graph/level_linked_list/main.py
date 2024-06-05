from level_linked_list import *   

if __name__ == '__main__':
    
    array = [4,6,2,7,8,9,10,3,20,12]

    root = createBinaryTree(array)
    lists = [LinkedList()]

    createLinkedListByLevel(root, lists, 0)
    
    for i in range(len(lists)):
        lists[i].display()
