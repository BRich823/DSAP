from dsap.mapping.chain_hash_map import ChainHashMap
from dsap.searchtree.avl_tree import AVLTreeMap

import matplotlib.pyplot as plt
import numpy as np
import random
import time

def insert_in_avl(avl_map,elements):
  for i in range(number_of_elements):
    avl_map.__setitem__(elements[i],elements[i])

def insert_in_hash(hash_map,elements):
  for i in range(number_of_elements):
    hash_map.__setitem__(elements[i],elements[i])

def plot(data, newLabel, new_color, ls='-'):
    plt.plot(map_sizes, totals[data], label=newLabel, color=new_color, linestyle=ls)
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
  # Generate the random numbers to insert
  map_sizes = [1024, 2048, 3036, 4096]
  temp = [0, 0, 0, 0]
  totals = {'avlI': temp, 'avlL': temp, 'hashI': temp, 'hashL': temp}
  for n, number_of_elements in enumerate(map_sizes):
    elements = np.zeros(number_of_elements,dtype=int)
    for i in range(10):
      for j in range(number_of_elements):
        elements[j] = random.randint(0,number_of_elements*number_of_elements)

      # Insert the elements in the AVLTreeMap and in the hashmap
      avl_map = AVLTreeMap()
      hash_map = ChainHashMap()
      start_time = time.time()
      insert_in_avl(avl_map,elements)
      end_time = time.time()
      execution_time = end_time - start_time
      totals['avlI'][n] += execution_time / 10

      start_time = time.time()
      insert_in_hash(hash_map,elements)
      end_time = time.time()
      execution_time = end_time - start_time
      totals['hashI'][n] += execution_time / 10

    # Now compare the times required to look up for the elements
      start_time = time.time()
      for i in range(number_of_elements):
        avl_map.__getitem__(elements[i])
      end_time = time.time()
      execution_time = end_time - start_time
      totals['avlL'][n] += execution_time / 10

      start_time = time.time()
      for i in range(number_of_elements):
        hash_map.__getitem__(elements[i])
      end_time = time.time()
      execution_time = end_time - start_time
      totals['hashL'][n] += execution_time / 10


  print(totals)
  plot('avlI', 'AVL Insert', 'red') 
  plot('hashI', 'Hash Insert', 'blue') 
  plot('avlL', 'AVL Lookup', 'red', '--') 
  plot('hashL', 'Hash Lookup', 'blue', '--')

