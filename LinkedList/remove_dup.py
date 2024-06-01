from linked_list import LinkedList

#solution 1: use hash table
def removeDup_01(llist: LinkedList):
    table = []
    
    cur = llist.head
    prev = None

    while cur:
        if cur.data in table:
            prev.next = cur.next
        else:
            table.append(cur.data)
            prev = cur
        
        cur = cur.next
        
#The above solution takes O(N) time, where N is the number of elements in the linked list.

#solution 2: don't use hash table, use  runner technique
def removeDup_02(llist: LinkedList):
    cur = llist.head

    prev = None

    while cur:
        runner = cur.next
        prev = cur

        while runner:
            if runner.data == cur.data:
                prev.next = runner.next
            else:
                prev = runner
                 
            runner = runner.next
        
        cur = cur.next

#This code runs in O ( 1) space, but O( N2) time
    
