from os import system
class Node:
    #Constructor
   def __init__(self, data = None, next = None):
      self.data = data
      self.next = next
   
class LinkedList:
   def __init__(self):
      #Contructor
      self.head = None
      #self.head adalah pointer ke awal stack
   def push(self, data):
      if self.head is None:
        self.head = Node(data, None)
        return
      
      temp = self.head
      while temp.next:
           temp = temp.next
      temp.next = Node(data, None)
        
        
    
   def print(self):
      if self.head is None:
         print("Queue Kosong")
      temp = self.head
      llstr =''
      while temp:
         llstr += '->'+str(temp.data) 
         temp = temp.next
      print(llstr)

   def get_length(self):
         count = 0
         temp = self.head
         while temp:
            count += 1
            temp = temp.next

         return count
   
   def pop(self):
      if self.head is None:
         print("Queue Kosong")
         input('')
         return
      
      data = self.head.data
      self.head = self.head.next
      print("data yang di pop adalah  " + data)
      input('')
          

      
   def swap(self,index1,index2):
        length = self.get_length()

        if index1 < 0 or index1 >= length or index2 < 0 or index2 >= length:
            print("Indeks tidak valid")
            return

        if index1 == index2:
            print("Indeks sama, tidak ada yang perlu ditukar")
            return

        prev_node1 = None
        node1 = self.head
        for _ in range(index1):
            prev_node1 = node1
            node1 = node1.next

        prev_node2 = None
        node2 = self.head
        for _ in range(index2):
            prev_node2 = node2
            node2 = node2.next

        if prev_node1:
            prev_node1.next = node2
        else:
            self.head = node2

        if prev_node2:
            prev_node2.next = node1
        else:
            self.head = node1

        node1.next, node2.next = node2.next, node1.next

ll = LinkedList()
while(1):
   system('cls')
   ll.print()
   print('\n\n')
   print("1. push data to list")
   print("2. pop data from list")
   print("3. swap data around")
   print("4. exit")
   choice = input("Masukan Pilihan\n")
   print ("\n\n")
       
   if choice == "1":
         sem= str(input("masukan variabel yang akan di push\n"))
         ll.push(sem)

   if choice == "2":
           ll.pop()

   if choice == "3":
         index1=int(input("masukan data yang akan diswap\n"))
         index2=int(input("dan\n"))
         ll.swap(index1,index2)

   if choice == "4":
           break
