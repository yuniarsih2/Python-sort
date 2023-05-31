# Mengurutkan daftar dengan penggunaan flag

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        is_sorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
            break


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Hasil pengurutan:", arr)

#Output Hasil pengurutan: [11, 12, 22, 25, 34, 64, 90] tampilan dari angka yang terkecil ke yang terbesar
