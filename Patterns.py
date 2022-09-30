# n = 5

# print(" * " * n)

'''
-----------------------------------
Square Star Pattern

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *

n = 5
for i in range(n):
    for j in range(n):
        print("*", end = " ")
        
    print()

-----------------------------------
'''

'''
-----------------------------------
#Decreasing Triangle

* * * * * 
* * * * 
* * * 
* * 
* 

n = 5

for i in range(n):
    for j in range(n - i):
        print("*", end = " ")
        
    print()
    
-----------------------------------
'''


'''
-----------------------------------
Increasing Triangle

* 
* * 
* * * 
* * * * 
* * * * * 

n = 5                                   

for i in range(n):
    for j in range(i + 1):
        print("*", end = " ")
        
    print()
    
-----------------------------------
'''


'''
-----------------------------------
Right Sided Triangle

          * 
        * * 
      * * * 
    * * * * 
  * * * * * 

n = 5

for i in range(n):
    
    for j in range(i, n):
        print(" ", end = " ")  
    
    for j in range(i + 1):
        print("*", end = " ")
        
        
    print()

-----------------------------------
'''

'''
-----------------------------------
Left Sided Triangle

#   * * * * * 
#     * * * * 
#       * * * 
#         * * 
#           *  

n = 5

for i in range(n):
    
    for j in range(i + 1):
        print(" ", end = " ")  
    
    for j in range(i , n):
        print("*", end = " ")
        
        
    print()

-----------------------------------
'''

'''
-----------------------------------
Hill


#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 


n = 5

for i in range(n):
    
    for j in range(i, n):
        print(" ", end = " ")  
    
    for j in range(i):
        print("*", end = " ")
        
    for j in range(i + 1):
        print("*", end = " ")
        
        
    print()

-----------------------------------
'''


'''
-----------------------------------
Hill Inverse

# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 


n = 5

for i in range(n):
    
    for j in range(i):
        print(" ", end = " ")  
    
    for j in range(i, n):         #range(i, n - 1)
        print("*", end = " ")
        
    for j in range(i + 1, n):
        print("*", end = " ")
        
        
    print()

-----------------------------------
'''



'''
-----------------------------------

# * 
#   * * 
#     * * * 
#       * * * * 
#         * * * * * 


n = 5

for i in range(n):
    
    for j in range(i):
        print(" ", end = " ")  
    
    for j in range(i + 1):
        print("*", end = " ")
                
    
    print()

-----------------------------------
'''


'''
-----------------------------------

# * * * * * * 
#   * * * * * * 
#     * * * * * * 
#       * * * * * * 
#         * * * * * * 

n = 5

for i in range(n):
    
    for j in range(i):
        print(" ", end = " ")  
    
    for j in range(i, n):
        print("*", end = " ")
        
    for j in range(i + 1):
        print("*", end = " ")
        
        
    print()

-----------------------------------
'''


# '''
# -----------------------------------
# Diamond Pattern

#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 

n = 5

for i in range(n - 1):
    
    for j in range(i, n):
        print(" ", end = " ")  
    
    for j in range(i):         #range(i, n - 1)
        print("*", end = " ")
        
    for j in range(i + 1):
        print("*", end = " ")
        
    print()
        
for i in range(n):
    
    for j in range(i + 1):            #range(i + 2)
        print(" ", end = " ")  
    
    for j in range(i, n - 1):         #range(i, n - 1)
        print("*", end = " ")
        
    for j in range(i , n):       #range(i, n - 2)
        print("*", end = " ")
        
        
    print()


# -----------------------------------
# '''