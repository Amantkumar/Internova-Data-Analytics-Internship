import numpy as np
arr=np.arange(1,13)
print("Original:",arr); print("Index 3:",arr[3]); print("Slice 2:7:",arr[2:7])
a=arr.reshape(3,4)
print("\n2D:\n",a); print("First row:",a[0]); print("Second column:",a[:,1]); print("Row 2 Col 3:",a[1,2])
print("\nReshaped 4x3:\n",arr.reshape(4,3))
