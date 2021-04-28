from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    LinkLists = []
    for element in range(size):
      LinkLists.append(LinkedList())
    return LinkLists


  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    w_length = len(key)
    w_length = ord(key[-1])
    index = w_length % self.size

    return index



  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    updated_data = (key, value)
    arr_i = self.hash_func(key)
    arr_i = self.hash_func(updated_data[0])
    LinkedList = self.arr[arr_i]
    list_index = LinkedList.find(updated_data[0])
    print(f'Looking for... {updated_data[0]} in the List[{arr_i}]')
    if list_index == -1:
      LinkedList.append(updated_data)
    else:
      print(f' A duplicate has been found... #{updated_data[0]}')
      LinkedList.update_node(key)
    LinkedList.append(updated_data)
    return f"{key} was inserted: {value} at index {arr_i}."


  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for LinkedList in self.arr:
      LinkedList.print_nodes()



