class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None 
        self.prv = None      
        


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
MAX_32_BITS = 0xFFFFFFFF
MAX_64_BITS = 0xFFFFFFFFFFFFFFFF


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here       
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY  
        self.hash_table = [None] * self.capacity
        self.total_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        #return self.total_items
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.total_items/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_OFFSET = 0xcbf29ce484222325
        FNV_PRIME = 0x00000100000001B3
        encoded_key = key.encode()

        index = FNV_OFFSET
        for val in encoded_key:
            index = index * FNV_PRIME
            index = index ^ val

        return index & MAX_64_BITS
       


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
          hash = (( hash << 5) + hash) + ord(x)
        return hash & MAX_32_BITS

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


        # self.hash_table[index] = value
    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)
        index = self.hash_index(key)
        #print(f"==={key}===={index}===={value}==\n")
        
        # check if list is empty
        if self.hash_table[index] is None:
            # create a node to add
            new_node = HashTableEntry(key, value)
            self.hash_table[index] = new_node
            self.total_items += 1
        else:
            node = self.findNodeByKey(key)
            if node is None:
                # create a node to add
                new_node = HashTableEntry(key, value)
                # new_node should point to current head
                new_node.next = self.hash_table[index]
                # move head to new node
                self.hash_table[index] = new_node
                self.total_items += 1
            else:
                node.value = value
    
    def findNodeByKey(self, key):

        index = self.hash_index(key)
        current_node = self.hash_table[index]
        while current_node is not None:
            if current_node.key == key:
                return current_node
            current_node = current_node.next    
        return None


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        # if self.get_load_factor() < 0.2:
        #     self.resize(int(self.capacity / 2))
        index = self.hash_index(key)
        prev_node = current_node = self.hash_table[index]
        key_found = False
        if current_node:
            # check first node key.
            if current_node.key == key:
                self.hash_table[index] = None
                self.total_items -= 1
                key_found = True
            else:
                current_node = current_node.next
                while current_node is not None:
                    if current_node.key == key:
                        prev_node.next = current_node.next
                        self.total_items -= 1
                        key_found = True
                        current_node = None
                        break
                    else:
                        prev_node = current_node
                        current_node = current_node.next    
        if not key_found:
            print(f"{key} does not exist")


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        node = self.findNodeByKey(key)
        if node is not None:
            return node.value
        return node
     

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here  
        old_capacity = self.capacity
        self.capacity = new_capacity     
        self.hash_table.extend([None for x in range(len(self.hash_table), self.capacity)]) 
        #print(len(self.hash_table))   
        for i in range(old_capacity):
            current_node = self.hash_table[i]
            while current_node is not None:
                self.put(current_node.key, current_node.value)                
                current_node = current_node.next
            





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    #print(ht.get_num_slots())
    #print(ht.get_load_factor())

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
        

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    #Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
