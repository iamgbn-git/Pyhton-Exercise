'''Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
>Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
'''


lst = input().split(',')   #splits in comma position and set up in list 
seq = []
lst = [int(i) for i in lst] #converts string to integer
for i in lst:
    if i % 2 != 0:
        i = i*i
        seq.append(i)

seq = [str(i) for i in seq]
print(",".join(seq))
