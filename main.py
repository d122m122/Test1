#TASK1
def nums(lst):
    lst_musbat = []
    lst_manfiy = []
    for x in lst:
        if x > 0:
            kop.append(x)
        elif x < 0:
            hop.append(x)
    if kop > hop:
        return len(kop)
    elif hop > kop:
        return len(hop)

print(nums([-3,-2,-1,1,2,3]))
print(nums([-3,-2,-1,0,0,2,3]))
print(nums([5,26,130,1325]))


#TASK2
def dublikat(nums):
    lst = []
    for x in nums:
        lst.append(nums.count(x) > 1)
    return any(lst)
print(dublikat([1,2,3,1]))
print(dublikat([1,2,3,4]))
print(dublikat([1,1,1,2,2,3,3,3,4,4,4,5,6,7]))