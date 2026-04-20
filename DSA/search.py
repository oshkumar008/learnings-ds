# Linear Search
from numpy import sort


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        print("Low high value for check  target is matching of not and check in which part it will be available: ",low, high)
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1   

#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            print(i, j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("Swapped: ", arr[j], arr[j+1])
        print(arr)
    return arr


#selection sort
def selection_sort(a):
    for i in range(len(a)):
        min = a[i] 
        index = i
        for j in range(i+1,len(a)):
            print(i,j)
            if min > a[j]:
                min = a[j]
                index = j
        print("Swapped: ", arr[i], arr[index])
        a[i], a[index] = a[index], a[i]
    return a

def insertion_sort(a):
    


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 8
    print("Linear Search: AT position", linear_search(arr, target), end="\n\n"  )
    
    print("Binary Search: At position", binary_search(arr, target), end="\n\n"  )

    print("Bubble Sort: ", end="\n\n")
    arr = [64, 34, 25, 12, 22, 11, 90,1,8,45,23,56,78,89,90]
    print("Bubble Sort:", bubble_sort(arr))
    print("Selection Sort: ", end="\n\n")
    print("Selection Sort:", selection_sort(arr))


    
