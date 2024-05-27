def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
      mid = (left + right) // 2

      if arr[mid] == target:
         return mid
      elif arr[mid] < target:
         left = mid + 1
      else:
          right = mid - 1

    return -1

arr = input("Enter the sorted array elements separated by spaces: ")
arr = [int(x) for x in arr.split()]
target = int(input("Enter the target element: "))
result = binary_search(arr, target)
if result == -1:
   print("Target element not found in array")
else:
   print(f"Target element found at index {result}")