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