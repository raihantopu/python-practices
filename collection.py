# List = [] ordered and changeable, duplicats OK
# Set = {} unordered and immutable, but add/remove ok. no duplicates
# Tuple = () ordered and unchangeable. duplicates ok. faster.
# Dictionary = {key: value} → Unordered (as of Python 3.7+, insertion order is preserved), mutable, no duplicate keys

print("List = [] ordered and changeable, duplicats OK")
fruits = ["apple", "orange", "banna", "coconut"]
print(fruits[0:1])
print(fruits[:1])
print(fruits[-1])
print(fruits[::2])

for fruit in fruits:
    print(fruit)

fruits[0] = "mango"
print(fruits)

fruits.append("apple")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.insert(0, "pineapple")
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.index("mango"))
fruits.clear()
print(fruits)

# Set = {} → Unordered, mutable (can add/remove), NO duplicates
print("Set = {} → Unordered, mutable (can add/remove), NO duplicates")
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)  # Order not guaranteed

# Add an item
fruits.add("mango")
print(fruits)

# Try adding duplicate
fruits.add("apple")  # No effect
print(fruits)

# Remove an item
fruits.remove("orange")
print(fruits)

# Safe remove (no error if not found)
fruits.discard("papaya")
print(fruits)

# Loop through set
for fruit in fruits:
    print(fruit)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}

# Clear all
fruits.clear()
print(fruits)

# Tuple = () → Ordered, Immutable (can't change), allows duplicates, faster than lists
print("Tuple = () → Ordered, Immutable (can't change), allows duplicates, faster than lists")
colors = ("red", "green", "blue", "red")
print(colors)

# Accessing
print(colors[0])
print(colors[-1])
print(colors[1:3])

# Looping
for color in colors:
    print(color)

# Count and index
print(colors.count("red"))     # 2
print(colors.index("blue"))    # 2

# Single-item tuple
one_item = ("hello",)
print(type(one_item))  # <class 'tuple'>

# Tuples can contain any data
mixed = ("text", 123, True)
print(mixed)

# Dictionary = {key: value} → Unordered (as of Python 3.7+, insertion order is preserved), mutable, no duplicate keys
print("Dictionary = {key: value} → Unordered (as of Python 3.7+, insertion order is preserved), mutable, no duplicate keys")
person = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
print(person)

# Access
print(person["name"])
print(person.get("email"))        # Safe access

# Add/update
person["city"] = "Dhaka"
person["age"] = 31
print(person)

# Remove
person.pop("email")
print(person)

# Loop through
for key in person:
    print(key, ":", person[key])

for key, value in person.items():
    print(f"{key} = {value}")

# Keys and values
print(person.keys())
print(person.values())

# Check existence
print("name" in person)  # True

# Clear all
person.clear()
print(person)


#print(dir(fruits)) #this will show all the methods of the collection fruits
#Type | Syntax | Ordered | Changeable | Duplicates | Notes
#List | [] | ✅ | ✅ | ✅ | Use when you need order
#Set | {} | ❌* | ✅ | ❌ | Fast membership check
#Tuple | () | ✅ | ❌ | ✅ | Immutable, lightweight
#Dict | {k: v} | ✅* | ✅ | ❌ (keys) | Key-value pairs
