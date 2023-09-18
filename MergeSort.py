import random
global data
data =[]
def merge(arr,l,m,r):
    n1 = m - l + 1
    n2 = r - m
    ArrayKiri =  [0] * (n1)
    ArrayKanan = [0] * (n2)

    for i in range(0, n1):
        ArrayKiri[i]=arr [l + i]

    for j in range(0 ,n2):
        ArrayKanan[j]=arr[m + 1 + j]

    j = 0
    i = 0
    k = l

    while i <n1 and j < n2:

        if ArrayKiri[i] <= ArrayKanan[j]:
            arr[k] = ArrayKiri[i]
            i += 1
        else :
            arr[k] = ArrayKanan[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = ArrayKiri[i]
        i+=1
        k+=1


    while j <n2:
        arr[k] = ArrayKanan[j]
        j+=1
        k+=1


def merge_sort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        merge_sort(arr, l ,m)
        merge_sort(arr, m+1 ,r)
        merge(arr, l ,m ,r)

def random_data(n):
   data.clear()
   for i in range(n):
      data.append(random.randint(0,n))

def reverse_data(n):
   data.clear()
   for i in range(n):
      data.insert(0,i)

def nearly_sorted_numbers(n):
    data.clear()
    if n >= 100:
        x = int(n//10)
    elif n >= 10:
        x = 9
    else:
        x = 4 
    for i in range(0,n):
        if i%x==0: 
            data.append(random.randint(0,n))
        else:
            data.append(i)

while (1):
  print(data, '\n\n')
  print("1. input data yang terbalik ke array")
  print("2. input data yang hampir ter-sort ke array")
  print("3. input data random ke array")
  print("4. sort data dalam array")
  print("5. exit")
  choice = input("Masukan Pilihan\n")
  match choice:
    case "2":
      n=int(input("masukan banyak data\n"))
      nearly_sorted_numbers(n)
    case "1":
      n=int(input("masukan banyak data\n"))
      reverse_data(n)
    case "3":
      n=int(input("masukan banyak data\n"))
      random_data(n)
    case "4":
      merge_sort(data,0,n-1)
    case "5":
      break


