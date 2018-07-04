# CS5 Gold, hw2pr1
# Filename: hw2pr1.py
# Name:
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]  
print(answer0)


# Problem 1: creating [7, 1]
answer1 = e[1:3]
print(answer1)


# Problem 2: creating [9,1,1]
answer2 = pi[-1:] + 2*e[-1:]
print(answer2)


# Problem 3: creating [1, 4, 1, 5, 9]
answer3 = pi[1:]
print(answer3)


# Problem 4: creating [1, 2, 3, 4, 5]
answer4 =  e[-1:] + e[0:1] + pi[0:1] + pi[2:5:2]
print(answer4)

print()
print()
print()


# Lab2 string practice



### 
# 
# 5. (The example from above)    Create hey and store this string in the variable answer5. (3 ops.) 
# 6. Create collude and store this string in the variable answer6. (Our best: 5 ops.) 
# 7. Create arveyudd and store this string in the variable answer7. (Our best: 3 ops.) 
# 8. Create hardeharharhar and store this string in the variable answer8. (Our best: 7 ops.) with (h+m)[-2:3:-4] 
# 9. Create legomyego and store this string in the variable answer9. (Our best: 8 ops.) 
# 10. Create clearcall and store this string in the variable answer10. (Our best: 8 ops.) 
# 
###

print()

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:  'hey'
answer5 = h[0] + h[4:6]
print("Answer 5 should be: hey")
print(answer5)

# Problem 6:  'collude'
answer6 = c[0:4] + m[1:3] +c[-1]
print("Answer 6 should be: collude")
print(answer6)

# Problem 7:  'arveyudd'
answer7 = h[1:] + m[1:]
print("Answer 7 should be: arveyudd")
print(answer7)

# Problem 8:  'hardeharharhar'
answer8 = h[0:3] + m[-1] + c[-1] + 3*h[0:3]
print("Answer 8 should be: hardeharharhar")
print(answer8)

# Problem 9:  'legomyego'
answer9 = c[3:6] + c[1] + m[0] + h[-1] + c[4:6] + c[1]
print("Answer 9 should be: legomyego")
print(answer9)

# Problem 10:  'clearcall'
answer10 = c[0:6:2] + h[1:3] + c[0] + h[1] + c[2:4]
print("Answer 10 should be: clearcall")
print(answer10)