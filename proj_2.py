# Using BSTs and AVL trees

from dsap.searchtree.binary_search_tree import TreeMap
from dsap.searchtree.avl_tree import AVLTreeMap
import numpy as np
import random
import matplotlib.pyplot as plt

avl = AVLTreeMap()
bst = TreeMap()
avl_h = {}
bst_h = {}


for number_of_elements in [1024, 2048, 3036, 4096]:
  avl_h[number_of_elements] = 0
  bst_h[number_of_elements] = 0
  elements = np.zeros(number_of_elements,dtype=int)
  for _ in range(10):
    for i in range(number_of_elements):
      elements[i] = random.randint(0,number_of_elements*number_of_elements)

      bst.__setitem__(elements[i],elements[i])
      avl.__setitem__(elements[i],elements[i])

    print("The height of the BST is: ",bst.height())
    bst_h[number_of_elements] += bst.height()
    print("The height of the AVL is: ",avl.height())
    avl_h[number_of_elements] += avl.height()
    
bst_avg = [h/10 for h in bst_h.values()]
avl_avg = [h/10 for h in avl_h.values()]

plt.plot(list(avl_h.keys()),list(avl_avg),label="AVL")
plt.plot(list(bst_h.keys()),list(bst_avg),label="BST")
plt.xlabel("Number of Elements")
plt.ylabel("Average Height")
plt.title("Average Height of BST and AVL as # of elements increase")
plt.legend()
plt.show()
