unsorted_list=[12,9,67,45,90]
def bubble_sort(unsorted_list):
   n= len(unsorted_list)
   for i in range(n-1):
        for j in range(n-1-i):
            if unsorted_list[j]>unsorted_list[j+1]:
                unsorted_list[j],unsorted_list[j+1]=unsorted_list[j+1],unsorted_list[j]

   return unsorted_list

print("Sorted List:",bubble_sort(unsorted_list))








