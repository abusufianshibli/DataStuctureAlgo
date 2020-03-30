# Data Structure (Code Camp)

Table Of Content-

*[What Is Data Structure?](#what-is-data-structure)

*[Categorys of Data Structure](#categorys-of-data-stuecture)

*[Type of Data](#type-of-data)

*[Basic Oparations](#basic-oparations)

*[Static & dynamic Array](#static-&-dynamic-array)
 
 >[Complexity of Array](#complexity-of-array)

*[Linked Lists Introduction](#linked-lists-introduction)

*[Type of Linked list](#type-of-linked-list)
 
 >[Complexity of Linked List ](#complexity-of-linked-list)

 >[Singly Linked List](#singly-linked-list)
 
 >[Doubly Linked List](#doubly-linked-list)
 
 >[Circular Linked List](#circular-linked-list)

*[Stack Introduction](#stack-introduction)

 >[Complexity of  Stack ](#complexity-of-stack)

 >[Satck Code](#stack-code)

*[Queue Introduction](#queue-introduction)

## What is Data Structure?
A data structure is a specialized format for organizing, processing, retrieving and storing data.


## Categorys-of-data-stuecture
1.Liner or Non-Liner
2.Homogeneous or Non-Homogeneous
3.Static or Dynamic

## Type of Data
1.Bulit-in:

    1.1:Integers

    1.2:Boolean

    1.3:Floating

    1.4:String

2.Derived

    2.1:List

    2.2:Array

    2.3:Stack

    2.4:Queue  
## Basic Oparations

1.Insert

2.Searching

3.Shorting

4.Deletions

5.Traversing

## Static & Dynamic Array
Static Array :It's an fixed lenght array if the array was full then any new data was come in the array it's shown array out of bound that's mean no space are avalabile in this array.
Dynamic Array:It's not an fixed array if array space full then it's create an new array which will be double from the previous array and new data and previous array data will add in the new array that's why we called it as dynamic array.

### Complexity of Array
Here, is the Complexity of the Static & dynamic array.

| Type of work | Static array | Dynamic array |
| ------------ | ------------ | ------------- |
| Access       | O(1)         | O(1)          |
| Search       | O(n)         | O(n)          |
| Insertion    | N/A          | O(n)          |
| Appending    | N/A          | O(1)          |
| Deletion     | N/A          | O(n)          |

### Code or Implementations of Dynamic Array
 Here, I am using python to Make an dynamic array.

``` python
import ctypes

class DynamicArray(object):
    def __init__(self):
        self.FirstNode=0
        self.capacity=2
        self.FirstArray=self.create_arrey(self.capacity)
        # the create_array method array take double kore felbe jkn ager array te value out of bound hobe.
        def create_array(self,new_capacity):
            return (new_capacity*ctypes.py_object)
        # data golo k abar store korbe and returen korbe.
        def _len_(self):
            return self.FirstNode

        def _getitem_(self,index):
            if not 0<=index<self.FirstNode:
                return IndexError('Index is out of bound')
            else:
                return self.FirstNode[index]
        def insert(self,element):
            if self.FirstNode==self.capacity:
                self.extendarray(2*self.capacity)
            else:
                self.FirstArray[self.FirstNode]=element
                self.FirstNode+1

        def extendarray(self,new_capacity):
            NewArray=self.create_arrey(new_capacity)
            for index in range (self.FirstNode):
             NewArray[index]=self.FirstArray[index]

             self.FirstArray=NewArray
            self.capacity=new_capacity

array=DynamicArray()
```

## Linked Lists Introduction

Linked list is a common used linere data structure which consises by group.

In linked list every nodes hold his  own data and also hold the address of the next node that's make a link in every nodes thats why its called linked list and its most use in data stroe after the Array structure .

### Complexity of Linked List

| Task               | Singly linked list | Doubly linked list |
| ------------------ | ------------------ | ------------------ |
| Search             | O(n)               | O(n)               |
| Insertion at head  | O(1)               | O(1)               |
| Insertion at tail  | O(1)               | O(1)               |
| Remove from head   | O(1)               | O(1)               |
| Remove from tail   | O(n)               | O(1)               |
| Remove from middle | O(n)               | O(n)               |


## Type of Linked list

Basically three type of linked list are had 

1.Singly Linked List

2.Doubly Linked List

3.Cricular Linked List

### Singly Linked List 

In the singly linked list as like a on way deration road we can move forward in this singly linked list,we can't travers back in the singly linked list.(Every list the first data or node is head node for the list.)
```python
class Node:
    def __init__(self,data=None):
        self.data=data
        self.nextdata=None

class LinkedList:
    def __init__(self):
        self.head=None


    def InsertInMiddel(self,new_node,newdata):
        if new_node is None:
            print("Node is Absent")
            return
        else:
          new_node = Node(newdata)
          new_node.nextdata=new_node.nextdata
          new_node.nextdata=new_node


    def ListPrint(self):
        var =self.head
        while var is not None:
            print(var.data)
            var=var.nextdata

list1=LinkedList()

list1.head=Node("Sheble")
v2 =Node("Fahad")
v4 =Node("Shunjid")
v5 =Node("Zubayer")
v6 =Node("Anindo")

list1.head.nextdata=v2
v2.nextdata=v4
v4.nextdata=v6
v6.nextdata=v5


list1.InsertInMiddel(list1.head.nextdata,"Zihadul")

list1.ListPrint()

```


### Doubly Linked List 

In doubly Linked list we can move any side of the node like tow way road we can go the forward node and can back the previous node .In doubly linked list the start node address is 0.(Its mean it's haven't any previous node)

### Circular Linked List

in circular linked list its like a loop , the end node of the list hold the address of the first node so it's move around the list.

## Stack Introduction

A stack is a Abstract data type and it's an ordered collection of item.(in the others hand the Stack follow like LIFO(Last in first out) If we have and stack and we push 4 data in the stack if you pop the data from the stack we have start from the top of the stack thats mean the last data out from the stack.)

![](images/stack.png)

### Complexity of Stack

 | Task      | Complexity |
| --------- | ---------- |
| Pushing   | O(1)       |
| Popping   | O(1)       |
| Peeking   | O(1)       |
| Searching | O(n)       |
| Size      | O(1)       |

### Stack Code

``` python
myStack=[]

myStack.append(input())
myStack.append(input())
myStack.append(input())
myStack.append(input())
myStack.append(input())

print(myStack)

myStack.pop()
print(myStack)
myStack.append(input())
print(myStack)
myStack.pop()
myStack.pop()
print(myStack)
myStack.pop()
myStack.pop()
print(myStack)
myStack.pop()
```

## Queue Introduction

Queue is an abstract data type, it's just like the stack but in this time it's follow the FIFO(First in First out) from. An queue First data is a head data or head node and the last data element is a tail data or tail node.

An Example, In the self 
