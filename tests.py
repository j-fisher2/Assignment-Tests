import time
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        self.head=None
        
    def append(self,val):
        if not self.head:
            self.head=Node(val)
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=Node(val)
    
    def find(self,target):
        cur=self.head
        while cur:
            if cur.value==target:
                return True
            cur=cur.next
        return False

class BST:
    def __init__(self,value):
        self.value=value
        self.left=self.right=None
    
    def insert(self,node):
        if not node:
            return
        if node.value<self.value:
            if not self.left:
                self.left=node
            else:
                self.left.insert(node)
        else:
            if not self.right:
                self.right=node
            else:
                self.right.insert(node)
    
    def find(self,target):
        if self.value==target:
            return True
        if target>=self.value:
            return self.right.find(target)
        else:
            return self.left.find(target)
    

def make_balanced_tree(vals):
    return _make_tree(vals,0,len(vals)-1)

def _make_tree(vals,left,right):
    if left>right:
        return None
    mid=(left+right)//2
    root=BST(vals[mid])
    root.insert(_make_tree(vals,left,mid-1))
    root.insert(_make_tree(vals,mid+1,right))
    return root
    
    
    
tree_vals=[i for i in range(50000)]
bst=make_balanced_tree(tree_vals)


m=dict()
for i in range(50000):
    m[i]=True


list=List()
for i in range(50000):
    list.append(i)

def search_list(head,target):
    start=time.time()
    head.find(target)
    end=time.time()
    print(end-start)

def search_bst(root,target):
    start=time.time()
    root.find(target)
    end=time.time()
    print(end-start)

def search_map(m,target):
    start=time.time()
    found=False
    if target in m:
        found=True
    end=time.time()
    print(end-start)

search_list(list,45600)
search_bst(bst,45600)
search_map(m,45600)
