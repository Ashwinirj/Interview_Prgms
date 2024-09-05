# l1 = [2,7,3,6,5,4,6,3,7,2]
# sum1 = 9
# pair =[]
# j = 0

# for i in range(len(l1)-1):
#     for j in range(i+1):
#     # j = i+1 
#         print(f"({l1[i]},{l1[j]})")
#     # print(type(l1[i]))
#         if (l1[i] + l1[j]) == sum :
#             pair.append(f"({l1[i]},{l1[j]})")
#     print(pair)


def find_pairs(nums, target):
    seen = set()  # Set to keep track of numbers we have seen
    pairs = set()  # Set to keep track of unique pairs

    for num in nums:
        complement = target - num
        if complement in seen:
            # Use a tuple with sorted numbers to ensure unique pairs
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return pairs

# Example usage
nums = [2, 7, 4, 5, 3, 6, 8, 1, 0, 9]
target_sum = 9

unique_pairs = find_pairs(nums, target_sum)
print("Unique pairs that sum up to", target_sum, "are:", unique_pairs)


