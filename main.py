#  “Looking for Fermat’s Last Theorem Near Misses”
# run  python3 main.py
# N/A
# N/A
# Rebekah Myrick, Francis Sumayop, Joe Pantaliono
# francissumayop@lewisu.edu, rebekahmyrick@lewisu.edu, josephapantaliono@lewisu.edu
# CPSC-44000-LT1: Software Engineering
# Date of submission: 02/05/2023
# Check for "near misses" of x^n + y^n = z^n

#get n and k from user
n = int(input("Enter n (power):")) # power
k = int(input("Enter k (upper limit on x/y values):")) # upper limit on values x,y
if k > 80: # limit k <= 80
    print("enter k <= 80")
    k = int(input("Enter k (upper limit on x/y values):"))
print('-'*20)
z_arr = [0, 0] # initialize array

# calulate values for 2-100^n, traverse this array
for i in range(2,101):
    z_arr.append(i**n)
# print(z_arr)

x = 10 # 10 <= x <= k
y = 10 # 10 <= y <= k
x_count = 11 # used to help increment
smallest_miss = 999999999999
smallest_relative_miss = 9999999999999
while x <= k and y <= k:
    result = (x**n + y**n) # (x^n + y^n)
    p1, p2 = 0, 1 # use two pointers to traverse z_arr
    for i in z_arr:
        if z_arr[p1] < result and z_arr[p2] > result: #  find "bracket" using pointers
            # calculate miss
            current_miss = min((result-z_arr[p1]),(z_arr[p2]-result))
            current_relative_miss = (current_miss/result)
            if current_relative_miss < smallest_relative_miss:
                smallest_relative_miss = current_relative_miss
                smallest_miss = current_miss
                print('New smallest relative miss found!: {:.8%}'.format(smallest_relative_miss))
                print('{0}^{2} + {1}^{2} = {3}'.format(x,y,n, result))
                print('lower: {0}, upper: {1}'.format(z_arr[p1],z_arr[p2]))
                print('Miss: {0}'.format(current_miss))
                print('-'*20)
            # check all combinations while incrementing x
            if x < k:
                x+=1
            else:
                # increment y and x and continue calculating combinations
                x = x_count
                x_count+=1
                y+=1
        p1+=1
        p2+=1

# final output
print('n: {0}'.format(n))
print('k: {0}'.format(k))
print('Smallest relative miss found: {:.8%}'.format(smallest_relative_miss))