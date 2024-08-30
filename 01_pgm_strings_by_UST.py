# Input-> a1b2c3
# output -> abbccc

# **********************************************************
# def decompress_str(com):
#     ls = []
#     for i in range(0,len(com),2):
#         times = int(com[i+1])
#         while times:
#             ls.append(com[i])
#             times -= 1
#     print("".join(ls))

# input = "a1b2c3"
# decompress_str(input) # output aabbbcccc

# *******************************************************************

input1 = "a2b3c6"
output1 = []
for i in range(0,len(input1),2):
    #print(input1[i])
    repeat_count = int(input1[i+1])
    # print(repeat_count)
    while repeat_count:
        output1.append(input1[i])
        repeat_count -= 1

output= "".join(output1)
print(output)

