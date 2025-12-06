#1.Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict={"a":10,
         "b":11,
         "c":223,
         "d":9876}
sorted_desc=dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True
                        ))
print(sorted_desc)
#2.Write a Python script to add a key to a dictionary.

my_dict={"a":10,
         "b":11,
         "c":223,
         "d":9876}
my_dict["g"]=23
print(my_dict)
#3.Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result=dic1.copy()
result.update(dic2)
result.update(dic3)
print(result)
#4.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n=int(input("son kirit:"))
squares_dict={x: x*x for x in range(1, n+1)}
print(squares_dict)
#5.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

squares_dict={x: x*x for x in range(1, 16)}
print(squares_dict)
#1.Write a Python program to create a set.
my_set={1,2,3,3}
print(my_set)
#2.Write a Python program to iterate over sets.
my_set={1,2,3,3}
for item in my_set:
    print(item)
#3.Write a Python program to add member(s) to a set.
my_set={1,2,3,3}
my_set.add(6)
print(my_set)
#4.Write a Python program to remove item(s) from a given set.
my_set={1,2,3,3}
my_set.discard(3)
print(my_set)
#5.Write a Python program to remove an item from a set if it is present in the set.
my_set={1,2,3,3}
rempove_item=int(input("son kiriting"))
if rempove_item in my_set:
    my_set.remove(rempove_item)
    
print(my_set)
