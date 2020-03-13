# Write a function search that accepts 2 arguments: A collection of values and a value to find in the collection

def search(people_arr, x):
    people_arr = sorted(people_arr)
    start = 0
    arr_len = len(people_arr) - 1
    while start <= arr_len:
        mid = start + int((arr_len - start)/2)
        if people_arr[mid] == x:
            return mid
        elif people_arr[mid] < x:
            start = mid + 1
        else:
            arr_len = mid - 1
    return -1

sample_arr = [2, 4, 6, 3, 8]
value = 4
res = search(sample_arr, value)
print(res)