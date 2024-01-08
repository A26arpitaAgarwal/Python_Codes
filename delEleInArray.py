def delete_elements(arr, positions):
    new_arr = [arr[i] for i in range(len(arr)) if i not in positions]
    return new_arr

arr = [0, 1, 2, 3, 4]
positions = [2, 4]
result = delete_elements(arr, positions)
print(result)
