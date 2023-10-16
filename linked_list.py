class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node =Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty") 
            return

        itr=self.head
        llstr=''

        while itr:
            llstr += str(itr.data) + '-->'
            itr=itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data, None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)  

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count     

    def remove_at(self,index):
        if index <0 or index >=self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr =self.head
        while itr:
            if count == index -1:
                itr.next =itr.next.next
                break

            itr=itr.next 
            count +=1

    def insert_at(self, index ,data):
          if index <0 or index > self.get_length():
              raise Exception("invalid index")      

          if index ==0:
            self.insert_at_begining(data) 
            return

          count = 0
          itr =self.head
          while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break


            itr = itr.next
            count +=1   

    def insert_after_value(self, data_after,data_to_insert):  
        for data in data_after:
            if data==data_after:
                self.insert_at(3,data_to_insert)
                return





if __name__=='__main__':
    ll=Linked_list()
    ll.insert_values(["sai","murthy","uppada"])
    print("length:",ll.get_length())
    ll.insert_at(2,"moon")
    ll.print()
    ll.insert_after_value("moom","vineela")
    ll.print()      