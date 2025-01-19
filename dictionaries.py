#Unordered collections of associated pairs of items where each pair consists of a key and a value. 
#This key-value pair is typically written as key:value

capitals = {'Iowa':'DesMoines', 'Wisconsin':'Madison'}

#Adding elements
capitals['Utah'] = 'SaltLakeCity'
capitals['California'] = 'Sacramento'

#Length
print(f"Length: {capitals}")

for k in capitals:
    print(capitals[k]," is the capital of ", k)

#Operators

#my_dict[k] - returns the value associated with k, otherwise its an error
print(f"{capitals['Iowa']}")

#in operator
y = 'Wisconsin' in capitals
print(f"Is Wisconsin in the dictionary: {y}")

#del operator
del capitals['California']
print(capitals)

#Methods

#keys - Returns the keys of the dictionary in a dict_keys object
print(capitals.keys())

#values - Returns the values of the dictionary in a dict_values object
print(capitals.values())

#items - Returns the key-value pairs in a dict_items object
print(capitals.items())

#get - Returns the value associated with k, None otherwise
print(capitals.get('Utah'))

print(capitals.get('Illinois',all))


