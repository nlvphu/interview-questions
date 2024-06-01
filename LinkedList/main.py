from linked_list import LinkedList

from remove_dup import *
from return_Kth_to_Last import returnKthLast
from sum_list import *

if __name__ == "__main__":
    # llist = LinkedList()
    # llist.insert_at_end(1)
    # llist.insert_at_end(1)
    # llist.insert_at_end(3)
    # llist.insert_at_end(2)
    # llist.insert_at_end(2)
    # llist.display()  # Output: 1 -> 2 -> 3 -> None

    # llist.delete_node(2)
    # llist.display()  # Output: 1 -> 3 -> None

    # removeDup_01(llist)
    # print("After remove duplicates")
    # llist.display()

    # removeDup_02(llist)
    # print("After remove duplicates")
    # llist.display()
    
    # print("Return Kth element to the last: \n")
    # print(returnKthLast(llist, 3))
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    llist_1.insert_at_end(7)
    llist_1.insert_at_end(1)
    llist_1.insert_at_end(6)

    llist_1.display()

    print(getNumericValue(llist_1))

    llist_2.insert_at_end(5)
    llist_2.insert_at_end(9)
    llist_2.insert_at_end(2)

    llist_2.display()

    print(getNumericValue(llist_2))


    print("Sum 2 linked list and display the sum in reversed order")
    ans = sum_list(llist_1, llist_2)

    ans.display()