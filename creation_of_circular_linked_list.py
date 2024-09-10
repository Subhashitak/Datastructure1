class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self,head,temp):
        self.head=None
        self.temp=None
    def display(self):
        if self.head is None:
            print("Empty list")
        else:
            self.temp=self.head
            while self.temp.next!=self.head:
                self.temp=self.temp.next
                print(self.temp.data,"-->",end=" ")
ll=cll(None,None)
ll.display()
