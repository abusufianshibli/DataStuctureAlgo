# Data Structure (Code Camp)

Table Of Content-

*[What Is Data Structure?](#what-is-data-structure)

*[Categorys of Data Structure](#categorys-of-data-stuecture)

*[Type of Data](#type-of-data)

*[Basic Oparations](#basic-oparations)

*[Static & dynamic Array](#static-&-dynamic-array)


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

### Complexity
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
