from binarytrees import *

root = binary_tree(50)
elements = {20, 56, 3, 4, 7, 10, 17, 20}

for i in elements:
    root.add(i)

root.search(10)