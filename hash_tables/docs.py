'''
HASH SETS
A hash code is a unique key generated to determine which bucket an element belongs to

Buckets are containers that store the elements to be accessed

A hash set has a constant time of O(1) unlike the arrays which have O(n) but in the worst case hash sets have a time complexity of o(n)
This is when the element to be accessed is the last element in the set

To use sets, Python has it's own set data type to assist with the implementation

'''

'''
HASH MAP

Helps in fast searching, deletion, adding and modifying data

The entry consists of key value pairs
The key is a unique identifier for each entry in the map
The hash code is the number generated for the key
bucket store the entries

Having a lot of buckets than hash map entries is a waste of memory and having a lot less buckets than the entries is a waste of time
'''