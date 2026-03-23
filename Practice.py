# Q1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division not possible")

print("a is Even" if a % 2 == 0 else "a is Odd")
print("b is Even" if b % 2 == 0 else "b is Odd")

a_float = float(a)
print("Float value of a:", a_float)

# Q2
sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
v_count = sum(1 for ch in sentence if ch in vowels)
c_count = sum(1 for ch in sentence if ch.isalpha() and ch not in vowels)

print("Vowels:", v_count)
print("Consonants:", c_count)

print("Reversed:", sentence[::-1])
print("With underscores:", sentence.replace(" ", "_"))
print("Capitalized:", sentence.title())

# Q3
t = (1, "hello", 3.5, 10, "world", 7)

nums = tuple(x for x in t if isinstance(x, (int, float)))
print("Numeric values:", nums)

try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)

t2 = (100, 200)
print("Concatenated tuple:", t + t2)

# Q4
students = {"A": 90, "B": 85}

students["C"] = 88

students["A"] = 95

del students["B"]

print("Keys:", students.keys())
print("Values:", students.values())
print("Items:", students.items())


# Q5
words = ["madam", "hello", "racecar", "python code"]
words.sort(key=len)
print("Sorted:", words)
pal = [w for w in words if w == w[::-1]]
print("Palindromes:", pal)
new_words = [w.replace(" ", "-") for w in words]
print("Modified:", new_words)

# Q6
t = (5, 15, "hi", 3, 20, "hello")
lst = list(t)
lst = [x for x in lst if not (isinstance(x, int) and x < 10)]
t_new = tuple(lst)
print("Updated tuple:", t_new)

# Q7
students = {}

def add_student():
    name = input("Enter name: ")
    marks = list(map(int, input("Enter marks: ").split()))
    students[name] = {"marks": marks}

def update_marks():
    name = input("Enter name: ")
    if name in students:
        students[name]["marks"] = list(map(int, input("New marks: ").split()))

def average(name):
    return sum(students[name]["marks"]) / len(students[name]["marks"])

def topper():
    top = max(students, key=lambda x: average(x))
    print("Topper:", top, "Avg:", average(top))

while True:
    print("\n1.Add 2.Update 3.Topper 4.Exit")
    ch = input("Choice: ")
    
    if ch == "1":
        add_student()
    elif ch == "2":
        update_marks()
    elif ch == "3":
        topper()
    elif ch == "4":
        break
# Q8

contacts = {}

while True:
    print("\n1.Add 2.Search 3.Delete 4.Show 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == "2":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif ch == "3":
        name = input("Delete name: ")
        contacts.pop(name, None)

    elif ch == "4":
        print(contacts)

    elif ch == "5":
        break
# Q9
employees = {}

while True:
    print("\n1.Add 2.Remove 3.Display 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Employee name: ")
        employees[name] = "Present"

    elif ch == "2":
        name = input("Remove name: ")
        employees.pop(name, None)

    elif ch == "3":
        for k, v in employees.items():
            print(k, "-", v)

    elif ch == "4":
        break
# Q10
students = []

while True:
    print("\n1.Add 2.Show Pass/Fail 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        roll = input("Roll: ")
        marks = int(input("Marks: "))
        students.append({"name": name, "roll": roll, "marks": marks})

    elif ch == "2":
        for s in students:
            if s["marks"] >= 40:
                print(s["name"], "PASS")
            else:
                print(s["name"], "FAIL")

    elif ch == "3":
        break

# Q11
menu = {
    "Burger": 100,
    "Pizza": 250,
    "Pasta": 150,
    "Coke": 50
}

total = 0

while True:
    print("\nMenu:", menu)
    item = input("Enter item (or 'done'): ")

    if item.lower() == "done":
        break

    if item in menu:
        qty = int(input("Quantity: "))
        total += menu[item] * qty
    else:
        print("Item not available")

tax = total * 0.05
final = total + tax

print("Total:", total)
print("Tax:", tax)
print("Final Bill:", final)

# Q12
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
# Q13
import string

text = input("Enter sentence: ")
clean = "".join(ch for ch in text if ch.isalnum())

unique = []

for ch in clean:
    if clean.count(ch) == 1:
        unique.append(ch)

print("Unique characters:", unique)

# Q14
def power(base, exp):
    result = 1
    for _ in range(abs(exp)):
        result *= base

    if exp < 0:
        return 1 / result
    return result

print(power(2, 3))   
print(power(2, -2))  

# Q15
s = input("Enter string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

vowels = "aeiouAEIOU"
v = c = d = sp = 0

for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special chars:", sp)

# Q16
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, self.marks)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(self.name, "teaches", self.subject)


class Admin:
    def manage(self):
        print("Managing school")

# Example
s = Student("Abinash", 90)
t = Teacher("Sir", "Math")
a = Admin()

s.show()
t.teach()
a.manage()

# Q17
class Book:
    def __init__(self, name):
        self.name = name
        print("Book added:", self.name)

    def __del__(self):
        print("Book removed:", self.name)

b1 = Book("Python")
del b1

# Q18
class Logger:
    def __init__(self, filename):
        self.file = open(filename, "a")

    def log(self, msg, level="INFO"):
        self.file.write(f"[{level}] {msg}\n")

    def __del__(self):
        self.file.close()
        print("File closed")

# Example
l = Logger("log.txt")
l.log("System started")
l.log("Warning message", "WARNING")
l.log("Error occurred", "ERROR")

# Q19
class Vehicle:
    total_rented = 0

    def __init__(self, rate):
        self.rate = rate

    def rent(self, days):
        Vehicle.total_rented += 1
        return self.rate * days


class Car(Vehicle):
    def rent(self, days):
        return super().rent(days) + 100


class Bike(Vehicle):
    def rent(self, days):
        return super().rent(days)


class Truck(Vehicle):
    def rent(self, days):
        return super().rent(days) + 200


c = Car(500)
print(c.rent(2))
print("Total rented:", Vehicle.total_rented)

# Q20
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Post:
    total_posts = 0

    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.likes = 0
        self.comments = []
        Post.total_posts += 1

    def like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        return f"{self.user}: {self.content} Likes:{self.likes}"


class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text

    def __str__(self):
        return f"{self.user} -> {self.text}"


# Example
u1 = User("Abinash")
post = Post(u1, "Hello World")

post.like()
post.add_comment(Comment(u1, "Nice post"))

print(post)
for c in post.comments:
    print(c)