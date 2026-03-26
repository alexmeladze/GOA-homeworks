def grow(arr):
    res = 1
    for i in arr:
         res *= i
    return res
    

def array_plus_array(arr1,arr2):
    count = sum(arr1)
    notcount = sum(arr2)
    return count + notcount

def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else:
        return 2 * (1 + w)
    



    def positive_sum(arr):
        sum = 0 
    for i in arr:
        if i > 0:
            sum+=i
    return sum