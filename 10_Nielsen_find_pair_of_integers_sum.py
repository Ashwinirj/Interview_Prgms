l1 = [21,3,4,11]
l2 = [1,12,0,1]

def find_pair_of_sum(l1,l2):
    l3 = []
    sum1 =42
    for i in range(len(l1)):
        for j in  range(len(l2)):
            if l1[i]+l2[j] == sum1:
                # print(f"({l1[i]},{l2[j]})")
                l3.append(f"({l1[i]},{l2[j]})")
    return l3
l4 = find_pair_of_sum(l1,l2)


if len(l4) != 0:
    print(l4)
else: 
    print("No such numbers exists to form sum of 42")
        

        