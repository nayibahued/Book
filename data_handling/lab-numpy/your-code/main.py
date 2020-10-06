#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a=np.random.random((2,3,5)) #floats random positivos entre 0 y 1
a2=np.random.randint(0,100,(2,3,5)) #numeros rand enteros con el rango def de 0 a 100 y tamaño de array (2,3,5)
a3=np.random.randn(2,3,5) #floats rand que van de negativo a positivo 

#Generally, we use randint() function when we need random integer values but the randn() function on the other hand is used when we want floating-point random numbers that are both positive and negative. Finally, the rand() function unlike randn() is used when we want random floating-point numbers that are only positive and in the range [0,1).

a2=np.random.randint((2,3,5))

#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b=np.full((5,2,3),1)

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?


a.ndim==b.ndim

#8. Are you able to add a and b? Why or why not?

#No se puede, deben de tener el mimso shape.

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c=b.T

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d=a+c
#funciona porque tienen la misma dimensión


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)
#Entre los dos arreglos existe 1 de diferencia, porque le agregamos el arreglo con solo las unidades 


#12. Multiply a and c. Assign the result to e.

e=a*c

#13. Does e equal to a? Why or why not?

a==e
#porque c es el arreglo que contiene nada mas que unidades, se multiplica por uno todo


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max=np.amax(d)
d_min=np.amin(d)
d_mean=np.mean(d)

print(d_max)
print(d_min)
print(d_mean)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f=np.zeros_like(d)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for a in range(0,2):
    for b in range(0,3):
        for c in range(0,5):
            if d[a,b,c] > d_min and d[a,b,c] < d_mean:
                f[a,b,c] = 25
            elif d[a,b,c] >d_mean and d[a,b,c] <d_max:
                f[a,b,c] = 75
            elif d[a,b,c] == d_mean:
                f[a,b,c] = 50
            elif d[a,b,c] == d_min:
                f[a,b,c] = 0
            elif d[a,b,c] == d_max:
                f[a,b,c] = 100
                
print(f)



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],
       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])
Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],
       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

f2=f.astype(str)
for a in range(0,2):
    for b in range(0,3):
        for c in range(0,5):
            if d[a,b,c] > d_min and d[a,b,c] < d_mean:
                f[a,b,c] = 'B'
            elif d[a,b,c] >d_mean and d[a,b,c] <d_max:
                f[a,b,c] = 'D'
            elif d[a,b,c] == d_mean:
                f[a,b,c] = 'C'
            elif d[a,b,c] == d_min:
                f[a,b,c] = 'A'
            elif d[a,b,c] == d_max:
                f[a,b,c] = 'E'
                
print(f2)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],
       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

f2=f.astype(str)
for a in range(0,2):
    for b in range(0,3):
        for c in range(0,5):
            if d[a,b,c] > d_min and d[a,b,c] < d_mean:
                f2[a,b,c] = "B"
            elif d[a,b,c] >d_mean and d[a,b,c] <d_max:
                f2[a,b,c] = "D"
            elif d[a,b,c] == d_mean:
                f2[a,b,c] = 'C'
            elif d[a,b,c] == d_min:
                f2[a,b,c] = 'A'
            elif d[a,b,c] == d_max:
                f2[a,b,c] = 'E'
                
print(f2)
