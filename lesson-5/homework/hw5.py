year=int(input("yilni kirit"))
if year%400==0:
    print(f"{year} kabisa yili")
elif year%100==0 and year%400!=0:
    print(f"{year} kabisa emas")
elif year%4==0 and year%100!=0:
    print(f"{year} kabisa yili")
else:
    print(f"{year} kabisa emas") 
n=int(input("son kirit"))
if n%2==1:
    print("weird")
elif n%2==0 and 2<=n<=5:
    print("not weird")
elif n%2==0 and 5<n<21:
    print("weird")
elif n%2==0 and n>20:
    print("not weird")

a=int(input("son kirit"))
b=int(input("son kirit"))
even_numbers=[x for x in range(a, b+1) if x%2==0]
print(even_numbers)
