# Mengurutkan angka secara ascending menggunakan selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Daftar angka yang ingin diurutkan
arr = [9, 5, 3, 8, 2]

# Memanggil fungsi selection_sort untuk mengurutkan daftar angka
selection_sort(arr)

# Menampilkan daftar angka setelah diurutkan
print("Hasil pengurutan:", arr)
for num in arr:
    print(num)

# Outputnya hasil angka dari yang terkecil ke yang terbesar [2, 3, 5, 8, 9]
