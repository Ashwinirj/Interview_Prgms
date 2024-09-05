def generate_subarrays(arr):
    subarrays = []
    # Loop through the array to get subarrays
    for start in range(len(arr)):
        for end in range(start + 1, len(arr) + 1):
            subarrays.append(arr[start:end])
    return subarrays

# Example usage:
arr = [1, 2, 3, 4]
subarrays = generate_subarrays(arr)
print("Subarrays:")
for subarray in subarrays:
    print(subarray)