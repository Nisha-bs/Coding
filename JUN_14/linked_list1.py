#!/usr/bin/python3

class Node:

    def __init__(self, data):
        self.data = data
        self.nxt = None

class Linked_List:

    def __init__(self):
        self.head = None
    
    def beginning(self,data):
        node = Node(data)
        node.nxt = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            tmp = self.head
            while tmp is not None:
                prev = tmp
                tmp = tmp.nxt
            prev.nxt = node

    def __len__(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.nxt
        return count

    def insert_in_middle(self,data,pos):
        node = Node(data)
        if pos == 0:
            self.beginning(data)
        if self.head is None:
            self.head = node
            return
        count = 0
        if pos < length:
            tmp = self.head
            while tmp != None:
                count += 1
                prev_node = tmp
                tmp = tmp.nxt
                #print(count)
                if count == pos:
                    node.nxt = tmp
                    prev_node.nxt = node
                    break
    
    def delete(self, pos = None):
        if pos == None:
            self.delete_last_node()
        else:
            self.delete_in_middle(pos)


    def delete_last_node(self):
        tmp = self.head
        if tmp == None:
            return None
        if tmp.nxt == None:
            self.head = None
            return None
        while tmp.nxt != None:
            prev_node = tmp
            tmp = tmp.nxt
        prev_node.nxt = None
    
    def delete_in_middle(self,pos):
        tmp = self.head
        if tmp == None or pos == 0:
            return None
        if tmp.nxt == None:
            self.head = None
            return None
        count = 0
        if pos < length:
            tmp = self.head
            while tmp.nxt != None:
                count += 1
                prev_node = tmp
                tmp = tmp.nxt
                #print(count)
                if count == pos:
                    prev_node.nxt = tmp.nxt
                    break
    
    def element_pos_element(self,pos=None, ele=None):
        if ele == None:
            self.pos_ele(pos)
        else:
            self.ele_pos(ele)

    def pos_ele(self, pos):
        if self.head == None:
            return None
        if pos == 0:
            return self.head
        if pos < length:
            count = 0
            tmp = self.head
            while tmp != None:
                count += 1
                prev_node = tmp
                tmp = tmp.nxt
                if count == pos:
                    pass
                    #print(tmp.data)
    
    def ele_pos(self, ele):
        if self.head == None:
            return None
        tmp = self.head
        count = 0
        while tmp != None:
            count += 1
            prev_node = tmp
            tmp = tmp.nxt
            if ele == prev_node.data:
                #print(count-1)
                pass
    def rotate(self, k):
        length = len(self)
        #print("length", length)
        if k % length == 0:
            return
        elif k > length:
            last_ele_pos = length - (k%length)
            #print("last_ele_pos",last_ele_pos)
        else:
            last_ele_pos = length - k
        tmp = self.head
        count = 1
        while tmp is not None:
            if count == last_ele_pos:
                kth_element = tmp
                #print("kth_element_data",kth_element.data)
            if count == length:
                last_element = tmp
                #print(last_element.data)
            tmp = tmp.nxt
            #print(tmp)
            count += 1
        last_element.nxt = self.head
        #print("last",last_element.data)
        self.head = kth_element.nxt
        #print("self.head", self.head.data)
        kth_element.nxt = None
        #print("kth_elemnt", kth_element.nxt)

    def print_node(self):
        tmp = self.head
        print("HEAD",end = "")
        while tmp is not None:
            print("-->{}".format(tmp.data),end = "")
            #print(f"-->{tmp.data}",end="")
            tmp = tmp.nxt
        print("-->None")

    
    def __iter__(self):
        tmp = self.head
        while tmp != None:
            yield tmp
            tmp = tmp.nxt

    def add_two_list(self, p, q):
        ll = p.head
        ll1 = q.head
        carry = 0
        while ll != None or ll1 != None:
            prev_node = p.head
            print(ll.data, ll1.data)
            add = ll.data + ll1.data
            value = add % 10
            carry = add//10
            print("add",value, carry)
            if carry > 0:
                prev_node.data += carry
            self.insert_at_end(add)
            ll = ll.nxt
            ll1 = ll1.nxt

    def merge(self, p, q):
        ll = p.head
        ll1 = q.head
        while ll != None or ll1 != None:
            print(ll.data, ll1.data)
            self.insert_at_end(ll.data)
            self.insert_at_end(ll1.data)
            ll = ll.nxt
            ll1 = ll1.nxt
             
    def swap(self):
        '''count = 1
        tmp = self.head
        prev = None
        current = self.head
        nxt = self.head.nxt
        print("first", prev, current.data, nxt.data)
        while tmp != None and tmp.nxt != None:
            adj = current.nxt
            if prev:
                prev.next = adj
            current.nxt = adj.nxt
            adj.nxt = current
            prev, current = current, current.nxt
            tmp = tmp.nxt
            if tmp == None:
                break
        print("y",prev.data, current.data, adj.data)'''

        dummy = Node(self.head)
        prev, cur = dummy, self.head
        while cur and cur.nxt:
            prev.nxt = cur.nxt
            cur.nxt = cur.nxt.nxt
            prev.nxt.nxt = cur
            prev, cur = cur, cur.nxt
        return dummy.nxt
ll = Linked_List()
#ll.beginning(6)
ll.insert_at_end(1)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at_end(6)
#length = len(ll)
#print(length)
#ll.insert_in_middle(5, 0)
#ll.delete()
#ll.delete_last_node()
#ll.delete_in_middle(2)
#ll.element_pos_element(None, 10)
#ll.rotate(20)
ll.print_node()
#ll1 = Linked_List()
#ll1.insert_at_end(2)
#ll1.insert_at_end(1)
#ll1.insert_at_end(5)
#ll1.print_node()
#ll2 = Linked_List()
#ll2.add_two_list(ll,ll1)
#ll2.merge(ll, ll1)
#ll2.print_node()
print(ll.swap())
ll.print_node()
