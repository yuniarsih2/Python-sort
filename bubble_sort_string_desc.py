# Mengurutkan daftar string secara descending (terbesar ke terkecil)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = ["z", "b", "a", "f", "c"]
bubble_sort(arr)
print("Hasil Pengurutan:", arr)

# Outpu Hasil Pengurutan: ['z', 'f', 'c', 'b', 'a'] diurutkan dari huruf terakhir hingga huruf pertama
