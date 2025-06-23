# == strict equality
# != strict inequality
# <= less than or equal to
# >= greater than or equal to
# < strictly less than
# > strictly greater than


print ('a' > 'Z') #uses ASCII value for comparison
print(ord('Z')) 
print(True or False) #evaluates to True

#order of execution: not → and → or
print(True or False and not False)

#not False → True
#False and True → False
#True or False → True