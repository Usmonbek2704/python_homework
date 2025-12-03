#1.Create a list containing five different fruits and print the third fruit.
a=["olma", "banan", "mandarin", "behi", "nok"]
print(a[2])
32.Create two lists of numbers and concatenate them into a single list.


a=[1,2,3,4]
b=[5, 6, 7, 8, 9]
a.extend(b)
print(a)
#3.Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
nums=[10, 2423, 4643, 6468, 865]
first=nums[0]
middle=nums[len(nums)//2]
last=nums[-1]
new_list=[first, middle,last]
print(new_list)
#4.Create a list of your five favorite movies and convert it into a tuple.
movie=["thor", "batman","spider man", "bee"]
l=tuple(movie)
print(l)
#5.Given a list of cities, check if "Paris" is in the list and print the result.
cities=["london", "rome", "paris", "barcelona","madrid"]
for city in cities:
    if city=="paris":
        print(cities)
  
#6.Create a list of numbers and duplicate it without using loops.
a=[1,2,3,4,5,6,7,8,9]
b=a.copy()
print(b, a)
#7.Given a list of numbers, swap the first and last elements.
a=[1,2,3,4,5,6,7,8,9]
a[0], a[-1]=a[-1], a[0]
print(a)
#8.Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
a=(1,2,3,4,5,6,7,8,9, 10)
print(a[3:7])

#9.Create a list of colors and count how many times "blue" appears in the list.


a=["blue", "white", "green","black", "blue"]
print(a.count("blue"))
#10.Given a tuple of animals, find the index of "lion".
animals=("elephant", "wolf", "lion")
print(animals.index("lion"))
#11Create two tuples of numbers and merge them into a single tuple.
animals=("elephant", "wolf", "lion")
a=("blue", "white", "green","black", "blue")
for animal, asd in zip(animals, a):
 print(animal, asd)
#12Given a list and a tuple, find and print their lengths.
animals=("elephant", "wolf", "lion")
a=["blue", "white", "green","black", "blue"]
print(len(a))
print(len(animals))
#13.Create a tuple of five numbers and convert it into a list.
a=(1,2,3,4,5)
b=list(a)
print(b)
#14.Given a tuple of numbers, find and print the maximum and minimum values.
a=(1,2,3,4,5,6,7,8,9, 10)
print(max(a),  min(a))
#15.Create a tuple of words and print it in reverse order.
a=("men", "sen", "u", "biz")
b=a[::-1]
print(b)
