import numpy as np

arr = np.array((1, 2, 3, 4, 5))

#print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


#print(arr)

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#print(arr[0, 1, 2])

arr = np.array([["123","Main Street" , "Miami","Florida"],["456","Elm Avenue", "Springfield", "CA"],["789","Oak Drive", "Lakeside", "NY"],["321", "Pine Lane", "Mountain View", "TX"]])

print(arr[0:2,1:4])



