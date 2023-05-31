# Mengurutkan daftar string secara descending (dari terbesar ke terkecil)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]


arr = ["z", "b", "a", "f", "c"]
selection_sort(arr)
print("Hasil pengurutan:", arr)

#Outpunya Hasil pengurutan: ['z', 'f', 'c', 'b', 'a'] dari hufu yang terbelakang ke huruf yangh terdepan

