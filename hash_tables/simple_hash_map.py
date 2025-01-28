class SimpleHashMap:
    def __init__(self, size = 100):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
    def hash_function(self, key):
        numeric = sum(int(num) for num in key if num.isdigit())%10
        return numeric
    
    def add(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key,value))
        
    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
    
    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        
        for k,v in bucket:
            if k == key:
                return v
        return None
    
    def print_map(self):
        print("Hash map contents:")
        [print(f'Bucket {index} : {bucket}') for index, bucket in enumerate(self.buckets)]
        
# Creating the Hash Map from the simulation
hash_map = SimpleHashMap(size=10)

# Adding some entries
hash_map.add("123-4567", "Charlotte")
hash_map.add("123-4568", "Thomas")
hash_map.add("123-4569", "Jens")
hash_map.add("123-4570", "Peter")
hash_map.add("123-4571", "Lisa")
hash_map.add("123-4672", "Adele")
hash_map.add("123-4573", "Michaela")
hash_map.add("123-6574", "Bob")

hash_map.print_map()

# Demonstrating retrieval
print("\nName associated with '123-4570':", hash_map.get("123-4570"))

print("Updating the name for '123-4570' to 'James'")
hash_map.add("123-4570","James")

# Checking if Peter is still there
print("Name associated with '123-4570':", hash_map.get("123-4570"))