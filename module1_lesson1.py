# Use else block to display a message “Done” after successful execution of for loop.

for num in range(1, 5):
    print(num)
else:
    print("Done")

# Write a program to display all prime numbers within a range.

lower_num = int(input("Enter lower_num: "))
higher_num = int(input("Enter higher_num: "))

for num in range(lower_num,higher_num + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
            else:
                print(num)

# Use a loop to display elements from a given list present at odd index positions.
def odd_indices(lst):
    new_lst = []
    new_lst.append(lst[0::2])
    return new_lst

print("Element of Given array present in Odd positions:")
print(odd_indices([1,7,8,4,10,13,17]))


# Calculate the cube of all numbers from 1 to a given number

c=dict()
for x in range(1,10):
    c[x]=x**3
print(c)  
