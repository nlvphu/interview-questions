from linked_list import LinkedList

def getNumericValue(llist: LinkedList) -> int:
    val = 0   
    n = 0

    cur = llist.head

    while cur:
        val += cur.data * pow(10, n)
        cur = cur.next
        n += 1
    
    return val

def generateLinkedListfromNumber(val: int) -> LinkedList:
    llist = LinkedList()

    if val == 0:
        llist.insert_at_end(val)
        return

    while val:
        data = int(val%10)
        val = val // 10
        llist.insert_at_end(data)
    
    return llist


def sum_list(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    num_1 = getNumericValue(llist_1)
    num_2 = getNumericValue(llist_2)

    return generateLinkedListfromNumber(int(num_1 + num_2))
