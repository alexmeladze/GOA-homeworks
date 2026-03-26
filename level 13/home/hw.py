def nums(n):
    result = 0
    for i in range(1,n,1):
        result += i 
    return result




def nums1(n):
    count = 0
    for i in range(1,n,1):
        if i % 2 != 0:
            count+= 1
    return count



def num(num1):
    sum= 0
    while num1 != 0:
        sum = sum + num1
        num2 = int(input("enter a new number!: "))
        if num1 == 0 or num2 == 0:
            break

num(int(input("Enter a number: ")))







def lst_sum(lst):
    sum = 0 
    for i in lst:
        sum += i
    return sum

lst = [67,12,10,5,8]

print(lst_sum(lst))




def lst_sort(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i)
        elif new_lst == []:
            return []
    return new_lst





def nums_sort(lst,num):
    return lst.count(num)

print(nums_sort([6,3,67,2,3,5,8,2,2,3,5,2],2))





def count_odd_sum_even(lst):
    count = 0
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum += i
        else:
            count+=1
    return count,sum

print(count_odd_sum_even([12,67,69,61,41,21,19,80,79]))






def sort(num1,num2):
    return min(num1,num2)