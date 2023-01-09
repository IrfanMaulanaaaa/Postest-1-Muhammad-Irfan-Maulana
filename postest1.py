import os
os.system("cls")

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
# slicing pada bagian kanan dan kiri array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    result = []
# membandingkan elemen kiri dan kanan agar dapat diurutkan
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if left:
        result += left
    elif right:
        result += right
    return result

def urai(a):
# fungsi ini untuk menguraikan list
    for i in range(len(a)):
        if type(a[i])==list:
            for j in range(len(a[i])):
                if type(a[i][j])==list:
                    for k in range(len(a[i][j])):
                        hasil.append(a[i][j][k])
                else:
                    hasil.append(a[i][j])
        else:
            hasil.append(a[i])
a=[ 12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
hasil = []
print("list awal :",a)

urai(a)
print("setelah diuraikan :",hasil)

hasil = mergeSort(hasil)

print("setelah diurutkan :",hasil)

# output:
# list awal : [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]  
# setelah diuraikan : [12, 1, 22, 3, 8, 14, 2, 6, 11, 90]
# setelah diurutkan : [1, 2, 3, 6, 8, 11, 12, 14, 22, 90]