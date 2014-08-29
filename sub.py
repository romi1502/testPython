import copy

#######################

def allSubset(st):
  l = [];
  return allSubsetAux(st,l);
  
def allSubsetAux(st,l):
  if len(st)==0:
    return [[]]
  else:
    l = allSubsetAux(st[0:-1],l)
    lk = []
    for k in range(len(l)):
      lk.append(l[k]+[st[-1]])
    return l + lk
    
    
#######################
    
def groupAna(st):
  ht = {};
  count = 0;
  
  l = [];
  for k in range(len(st)):
    key = ''.join(sorted(st[k]))
    if not (key in ht):
      ht[key] = count;
      count+=1;
      l.append([]);
    l[ht[key]].append(st[k])
    
  return l


#######################

def findMostSegPoint(segSt):

  inf = [(element[0],-1) for element in segSt]
  sup = [(element[1],1) for element in segSt]
  st = sorted(inf+sup);
  count = 0;
  mxCount = 0;
  mxIndex = 0;
  for k in range(0,len(st)):
    count -= st[k][1];      
    if mxCount<count:
      mxCount = count
      mxIndex = st[k][0]
      
  return mxIndex
  
  
#######################
class Node:
  data = None;    
  next = None;
  
  def __init__(self,value = None):
    self.data = value;
    self.next = None;
  
class Stack:
  node = Node();    
  size = 0;
  
  def push(self,value):
    n = Node(value);
    n.next = self.node;
    self.node = n;
    self.size += 1
    
  def pop(self):
    if self.node.data is None:
      return None
    value = self.node.data
    self.node = self.node.next;
    self.size -=1
    return value
    
  def isEmpty(self):
    return (self.node.data is None)

  def peek(self):
    if self.node.data is None:
      return None
    return self.node.data

    
#######################    
class SetOfStack:
  maxSize = 3;
  sizeOfCurrentStack = 0;
  stackOfStack = Stack();  
  
  def push(self,value):
    if self.sizeOfCurrentStack<self.maxSize:
      st = self.stackOfStack.pop()
      if st is None:
        st = Stack()
      st.push(value)
      self.stackOfStack.push(st)
      self.sizeOfCurrentStack += 1
    else:
      st = Stack()
      st.push(value)
      self.stackOfStack.push(st)
      self.sizeOfCurrentStack = 1
    
  def pop(self):
    if self.sizeOfCurrentStack == 0:
      return None
    
    if self.sizeOfCurrentStack == 1:
      st = self.stackOfStack.pop()
      st2 = self.stackOfStack.pop()
      if st2 is None:
        self.sizeOfCurrentStack = 0
        return st.pop()
      else:
        self.sizeOfCurrentStack = self.maxSize
        self.stackOfStack.push(st2)
        return st.pop()
      
    st = self.stackOfStack.pop()        
    n = st.pop();
    self.sizeOfCurrentStack -= 1
    self.stackOfStack.push(st)
    return n



#####################

def moveFrom1to3(st1,st2,st3,k):
  print 'none'  
  
  
#####################
def sort(st):
  n = st.pop()
  if not(n is None):
    sort(st)
    insert(n,st)


ct = count()

def insert(n,st):
  print ct.next()
  nn = st.pop()
  if nn is None:
    st.push(n)
  elif nn < n:
    st.push(nn)
    st.push(n)
  else:
    insert(n,st)
    st.push(nn)
    
    
def count():
  num = 0;
  while True:
    num+=1
    yield num
    
   
def sort2(st):
  stc = copy.deepcopy(st)
  st2 = Stack()
  while not(stc.isEmpty()):  
    n = stc.pop()
    n2 = st2.peek()
    while not(st2.isEmpty()) and n2>n:
      st2.pop()
      stc.push(n2)
      n2 = st2.peek()
    st2.push(n)
  return st2
