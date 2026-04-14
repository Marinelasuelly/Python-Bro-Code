# Exercise 1 Rectangle Area Calculat

#Strategy: 
#Varible to store the result of the area;
#variable to store the length
#variable to store the width
#Formula to store the area => A(area) = w (width) * l (length)
#
# SHOW the solution of the area
"""
  -----  CALC -----
"""

area = 0  
length = float(input("What is the length: "))
width  = float(input("What is the width: ")) 

area = width * length 

 
print(f"\nLength: {length}\n")
print(f"Width: {width} \n")
print(f"The area of the RETANGLE is:{area:.3f}cm^2")
# or you could just type:

#print(area)