"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
str_numbers = (['zero', 'one','two', 'three', 'four', 'five'])
ops = (['plus', 'minus'])

##make a dictionary to match the string with their respective int.
numbers = ([0,1,2,3,4,5,])
dict_numbers =dict(zip(str_numbers,numbers))

####################  REFACTORIZATION CODE  ####################


###functions where we make the calculus.
import funcs1 as f1 


###request of inputs
a = f1.request_a(str_numbers)
b = f1.request_b(ops)
c = f1.request_c(str_numbers)

###make the computation
result = f1.calculation(a,b,c,dict_numbers)

###transform the int into a string
result_int_to_str = f1.convert_int(dict_numbers,result)

###make the declaration of values
f1.declaration(a,b,c,result_int_to_str,result)
