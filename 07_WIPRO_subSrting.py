# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# CODILITY IDE 


def solution(S):
    # Implement your solution here
    result = []
    current_substring = ""
    seen_chars = set()

    for char in S:
        if char in seen_chars:
            # If the character is already in the current substring, finalize the substring
            result.append(current_substring)
            current_substring = ""
            seen_chars.clear()
        
        # Add the character to the current substring and update the set
        current_substring += char
        seen_chars.add(char)
    
    # Add the last substring
    if current_substring:
        result.append(current_substring)
    print(result)
    return len(result)

print(solution("abacdec"))
print(solution("world"))
print(solution("dddd"))
print(solution("cycle"))