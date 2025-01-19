my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

# Find the charCode at value and create a key (Hash Code)
def hash_function(val):
    return sum(ord(char) for char in val) % 10

# Add a name to the hash Table

def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    
    if value not in bucket:
        bucket.append(value)
        

# Check if the value is in the bucket

def contain(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    
    return value in bucket


add('Stuart')

print(my_hash_set)
print('Contains Stuart:',contain('Stuart'))

