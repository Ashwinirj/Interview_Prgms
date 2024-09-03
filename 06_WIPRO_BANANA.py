# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""
WAP in python where a string is Split into minimal number of 
substrings in such a way that no letter occurs more than once in the sub string

For the input string "abacbcbb", the output would be ['ab', 'ac', 'bcb', 'b']. This is because:

"""
def solution(S):
    # Implement your solution here
    s = "BANANA"
    required = {}
    for i in s:
        required[i] = s.count(i)
    
    char_count = {'B': 0, 'A': 0, 'N': 0}
    
    for char in S:
        if char in char_count:
            char_count[char] += 1
    
    min_banana = []
    for char in required:
        if required[char] > 0:
            min_banana.append(char_count[char]// required[char])
    print("Given string is: ",S)
    return min(min_banana)

print(solution("NAABXXAN"))  #output is 1
print(solution("NAANAAXNABABYNNBZ")) #output: 2
print(solution("QABAAAWOBL")) #output: 0