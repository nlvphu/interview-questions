from linked_list import LinkedList

#assume k is valid for the linkedlist
#solution 1: runner go forward more k steps, then move together 2 pointers when the runner reach the end, cur is the value we need
def returnKthLast(llist: LinkedList, k: int):
    cur = llist.head
    runner =  cur

    for _ in range(k):
        runner = runner.next
    
    while runner:
        cur = cur.next
        runner = runner.next
    
    return cur.data

