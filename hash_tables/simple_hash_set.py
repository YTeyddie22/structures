class HashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
    # Our hash function
    # Create the hash according to the number of buckets
    def hash_function(self, val):
        return sum(ord(char) for char in val) % self.size
    
    
    # Adding values to the bucket
    def add(self, val):
        index = self.hash_function(val)
        bucket = self.buckets[index]
        
        if val not in bucket:
            bucket.append(val)
            
    # Check if the value is present
    
    def contains(self, val):
        index = self.hash_function(val)
        bucket = self.buckets[index]
        
        return val in bucket
    
    # Delete items in bucket
    
    def remove(self, val):
        index = self.hash_function(val)
        bucket = self.buckets[index]
        
        if val in bucket:
            bucket.remove(val)
            
            
    def print_set(self):
        print("Contents:")
        [print(f'Bucket {index}" {bucket}') for index, bucket in enumerate(self.buckets)]
    
    
    
# Creating the Hash Set from the simulation
hash_set = HashSet(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:",hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hash_function('Adele'))
    
    
    