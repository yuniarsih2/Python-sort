# Mengurutkan daftar angka secara descending (dari yang terbesar ke terkecil)

def bubble_sort(arr) :
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Hasil pengurutan:", arr)

#Otput Hasil pengurutan: [90, 64, 34, 25, 22, 12, 11] terurut dari yang terbesar ke terkecil pada elemen