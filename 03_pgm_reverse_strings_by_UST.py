# input1= "Interview with UST"
# output: "weivretnI htiw TSU"
# ****************************************************************************

input1= "Interview with UST"
print("Given input is:",input1)

reverse_words= []

new_input = input1.split(" ")
for word in new_input:
    new_word =word[::-1]
    reverse_words.append(new_word)
    
reverse_input1 = " ".join(reverse_words)

print("Output in reverse order: ",reverse_input1)