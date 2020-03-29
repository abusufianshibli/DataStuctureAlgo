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