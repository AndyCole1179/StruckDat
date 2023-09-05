import random
from os import system
global data
data = []
def select_sort():
    n = data
    for i in range (len(n)):
        min_idx = i
        for j in range(i+1,len(n)):
            if n[min_idx] > n[j]:
                min_idx = j
        system('cls')
        #print(data,'\n')
        #print('data',data[i],'ditukar dengan data',data[min_idx])
        n[i], n[min_idx] =  n[min_idx], n[i]
        #input('')

    print('\n\n\n\n' , data)


def random_data(n):
   for i in range(n):
      data.append(random.randint(0,n))

def reverse_data(n):
   for i in range(n):
      data.insert(0,i)

def nearly_sorted_numbers(n):
    if n >= 100:
        x = (int)(n/10)
    elif n >= 10:
        x = 9
    else:
        x = 4 
    for i in range(1,n):
        if i%x==0: 
            data.append(random.randint(0,n))
        else:
            data.append(i)
        

# def inputt():
#     # global data
#     # data = []
#     while True:
#         system('cls')
#         print(data,'\n\n')
#         print('ketik exit untuk keluar dari loop\n')
#         temp_data = input('Masukan data : ')
#         if temp_data == 'exit':
#             break
#         try:
#             data.append(int(temp_data))
#         except:
#             print("Tolong Masukan Angka Atau exit")


while (1):
  print(data, '\n\n')
  print("1. input data yang terbalik ke array")
  print("2. input data yang hampir ter-sort ke array")
  print("3. input data random ke array")
  print("4. sort data dalam array")
  print("5. exit")
  choice = input("Masukan Pilihan\n")
  match choice:
    case "1":
      n=int(input("masukan banyak data\n"))
      nearly_sorted_numbers(n)
    case "2":
      n=int(input("masukan banyak data\n"))
      reverse_data(n)
    case "3":
      n=int(input("masukan banyak data\n"))
      random_data(n)
    case "4":
      select_sort()
    case "5":
      break

