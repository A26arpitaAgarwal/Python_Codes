def update_elements(arr, positions, new_values):
    for i, pos in enumerate(positions):
        arr[pos] = new_values[i]
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

positions = list(map(int, input("Enter the positions to update separated by spaces: ").split()))

new_values = list(map(int, input("Enter the new values separated by spaces: ").split()))

update_elements(arr, positions, new_values)
print("Updated array:", arr)
