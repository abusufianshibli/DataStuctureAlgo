class Queue():

    def __init__(self,size):
        self.head=1
        self.tail=1
        self.array=[0]*(size)
        self.size=size

    def empty(self):
        if self.tail == self.head:
            return True
        else:
            return False

    def full(self):

        if self.head==self.tail+1:
            return True
        else:
            return False

    def adding(self, x):
        if self.full():
            print("Overflow")
        else:
            self.array[self.tail]=x
            if self.tail==self.size:
                self.tail=1
            else:
                self.tail=self.tail+1
    def deleted(self):
        if self.empty():
            print("Underflow")

        else:
            x=self.array[self.head]
            if self.head==self.size:
                self.head=1
            else:
                self.head=self.head+1
                return x
    def display(self):
        i = self.head
        while(i<self.tail):
            print(self.array[i])
            if (i==self.size):
                i=0
            else:
                i=i+1


if __name__  =='__main__':
     q = Queue(20)

     q.adding("Sheble")
     q.adding("fahad")
     q.adding("shnjid")
     q.adding("zubayer")
     q.adding("anindo")
     q.adding("zihadul")

     q.display()

     print("")

     q.deleted()
     q.deleted()
     q.display()
     print("")

     q.adding("sheble")
     q.adding("fahad")
     q.display()