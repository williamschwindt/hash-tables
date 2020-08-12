class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        """Print entire linked list."""

        if self.head is None:
            return "[Empty List]"

        cur = self.head
        s = ""

        while cur != None:
            s += f'({cur.value})'

            if cur.next is not None:
                s += '-->'

            cur = cur.next

        return s

    def find(self, value):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur

            cur = cur.next

        return None

    def find_key(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur

            cur = cur.next

        return None

    def delete(self, key):
        cur = self.head

        # Special case of deleting head

        if cur.key == key:
            self.head = cur.next
            return cur

        # General case of deleting internal node

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:  # Found it!
                prev.next = cur.next   # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next

        return None  # If we got here, nothing found

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_or_overwrite_value(self, key, value):
        node = self.find(value)

        if node is None:
            # Make a new node
            self.insert_at_head(HashTableEntry(key, value))

        else:
            # Overwrite old value
            node.value = value


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        count = 0
        for item in self.table:
            if item != None:
                count += 1
        
        load_factor = count / self.capacity

        if load_factor >= .7:
            self.resize(self.capacity * 2)
        
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (((hash << 5) + hash) + ord(x)) % self.capacity
        return hash & 0xffffffff


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        #find index
        hash_index = self.djb2(key)
        
        #check if something is there
        if self.table[hash_index]:
            #check if the key already exists
            if self.table[hash_index].find_key(key):
                #if key exists replace value
                old_thing = self.table[hash_index].find_key(key)
                old_thing.value = value
            else:
                #if key does not exist add new node
                self.table[hash_index].insert_at_head(HashTableEntry(key, value))

        #if the slot is empty       
        else:
            #create a new linked list and add key:value pair to head
            self.table[hash_index] = LinkedList()
            self.table[hash_index].insert_at_head(HashTableEntry(key, value))

    def delete(self, key):
        #find index
        hash_index = self.djb2(key)

        if self.table[hash_index] == None:
            return None
        else:
            self.table[hash_index].delete(key)
        

    def get(self, key):
        #find index
        hash_index = self.djb2(key)

        if self.table[hash_index] == None:
            return None
        else:
            #search the linked list
            found_value = self.table[hash_index].find_key(key)
            
            #if None return None
            if found_value == None:
                return None
            else:
                #otherwise return the value
                return found_value.value



    def resize(self, new_capacity):
        #store the old table
        old_table = self.table

        #set capacity to new capacity and make new table
        self.capacity = new_capacity
        self.table = [None] * new_capacity

        #loop through every spot in array
        for item in old_table:
            #if the current spot has a ll rehash it
            if item != None:
                cur = item.head

                while cur is not None:
                    next_item = cur.next
                    #rehash
                    self.put(cur.key, cur.value)
                    cur = next_item


ht = HashTable(8)
ht.put('key0', 'value0')
print(ht.get('key0'))
print(ht.get_load_factor())



# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
