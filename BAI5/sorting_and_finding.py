def selection_sort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr 


def find_max_min_index(arr):
 
  max_index = arr.index(max(arr))
  min_index = arr.index(min(arr))
  return max_index, min_index
