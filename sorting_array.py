## SELECTION SORT

arr = []
no_of_elements = int(input("Enter no of elements in the array you need to sort: "))
for i in range(no_of_elements):
    element = int(input("Enter the element: "))
    arr.append(element)

for i in range(0, no_of_elements-1):
    for j in range(i+1, no_of_elements):
        if arr[j] < arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

print(arr)
