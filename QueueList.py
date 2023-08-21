from os import system
class Node:
    #Constructor
   def __init__(self, data = None, next = None):
      self.data = data
      self.next = next
   
class LinkedList:
   def __init__(self):
      #Contructor
      self.head =None
      #self.head adalah pointer ke awal stack
   def push(self, data):
      if self.head is None:
        self.head = Node(data, None)
        return
      
      temp =self.head
      while temp.next:
           temp = temp.next
      temp.next = Node(data,None)
        
        
    
   def print(self):
      if self.head is None:
         print("Stack Kosong")
      temp = self.head
      llstr =''
      while temp:
         llstr += str(temp.data) + '->'
         temp = temp.next
      print(llstr)

   def get_length(self):
         count =0
         temp = self.head
         while temp:
            count += 1
            temp = temp.next

         return count
   
   def pop(self):
      if self.head is None:
         print("Stack Kosong")
         return
      
      data = self.head.data
      self.head = self.head.next
          

      
   def swap(self,key1,key2):
       #key = keyword
       if key1 == key2:
         return

       PrevNode_Key1 =None
       CurrNode_Key1 = self.head
       while CurrNode_Key1 and CurrNode_Key1.data != key1:
           PrevNode_Key1 = CurrNode_Key1
           CurrNode_Key1 = CurrNode_Key1.next

       PrevNode_Key2 = None
       CurrNode_Key2 = self.head
       while CurrNode_Key2 and CurrNode_Key2.data != key2:
           PrevNode_Key2 = CurrNode_Key2
           CurrNode_Key2 = CurrNode_Key2.next

       if not CurrNode_Key1 or not CurrNode_Key2:
           return
       
       if PrevNode_Key1:
           PrevNode_Key1.next = CurrNode_Key2
       else:
           self.head = CurrNode_Key2
       if PrevNode_Key2:
           PrevNode_Key2.next = CurrNode_Key1
       else:
           self.head = CurrNode_Key1

       CurrNode_Key1.next, CurrNode_Key2.next = CurrNode_Key2.next , CurrNode_Key1.next


ll = LinkedList()
while(1):
   system('cls')
   ll.print()
   print('\n\n')
   print("1. push data to list")
   print("2. pop data from list")
   print("3. swap data around")
   print("4. display list")
   print("5. exit")
   choice = input("Masukan Pilihan\n")
   print ("\n\n")
       
   if choice == "1":
         sem= str(input("masukan variabel yang akan di push\n"))
         ll.push(sem)

   if choice == "2":
           ll.pop()

   if choice == "3":
         temp1=str(input("masukan data yang akan diswap\n"))
         temp2=str(input("dan\n"))
         ll.swap(temp1,temp2)

   if choice == "5":
           break
       
   if choice == "4":
       ll.print()