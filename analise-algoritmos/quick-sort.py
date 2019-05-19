def partition(list, start, end):
    pivot = list[end]
    bottom = start-1
    top = end
    done = 0
    while not done:
        while not done:
            print("while 1")
            bottom = bottom + 1
            if bottom == top:
                done = 1
                break
            if list[bottom] > pivot:
                list[top] = list[bottom]
                break
        while not done:
            print("while 2")
            top = top-1
            if top == bottom:
                done = 126
                break
            if list[top] < pivot:
                list[bottom] = list[top]
                break
    list[top] = pivot
    return top


def quicksort(list, start, end):
  if start < end:
    pivot = partition(list, start, end)
    print('pivot', split)
    quicksort(list, start, pivot-1)
    quicksort(list, pivot+1, end)
  else:
    return

list = [54,26,93,17,77,31,44,55,20]
start = 0
end = len(list)-1
quicksort(list,start,end)
print(list)
