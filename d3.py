# to get only single without any duplicates
list_1 = [3,6,4,7,6,7,3]
list_2=set(list_1)
print(list_2)

# to print single unique number
list_1 = [3,6,5,4,5,6,3]
first_sum = sum(list_1)
second_sum = sum(set(list_1))*2
res = second_sum-first_sum
print(res)

# factorial of a nnumber
n=int(input("enter number"))
fact=1
for i in range(n,1,-1):
    fact *= i
print(fact)

# sum of first 10 multiples of given number
n=int(input())
sum=0
for i in range(1,11):
    sum+=n*i 
print(sum)

# another method
n=int(input())
print(n*55)

# linear search for target indexes
list_1 = [1,7,9,7,4,6,2]
target = 7
for i in range(len(list_1)):
    if target==list_1[i]:
        print(i)
        break
 
# binary search for targeting index
list_1 = [1,2,3,4,5,6,7,8,9,10]
target = 7
start = 0
end=len(list_1)-1
index=-1
while(start<=end):
    middle=(start+end)//2
    if list_1[middle]==target:
        index = (middle)
        break
    elif list_1[middle]>target:
        end = middle-1
    elif list_1[middle]<target:
        start=middle+1
print(index)
 
# to print in increasing order       
n=int(input())
for i in range(1,n+1):
    print("* "*i)

# to print in decreasing order
n=int(input())
for i in range(n,0,-1):
   print("* "*i)

n=int(input())
for i in range(1,n+1):
    str1=""
    for j in range(1,i+1):
        str1+=str(j)+" "
    print(str1) 

# to print numbers in decreasing order
n=int(input())
for i in range(n,0,-1):
    str1=""
    for j in range(1,i+1):
        str1+=str(j)+" "
    print(str1)

# to get pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i) +"* "*i)    

# to get reverse pyramid
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i) +"* "*i)

# to get hallow triangle
n=int(input())
for i in range(1,n+1):
    if i == 1 or i == n:
        print("* "*i)
    else:
        print("*"+" "*(2*i-3)+"*")

# to get hallow pyramid
n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        print(" "*(n-i)+"* "*i)
    else:   
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")



