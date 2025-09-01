# 1 Design  Class
# Base Class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def info(self):
        print(f"📖 '{self.title}' by {self.author}, {self.pages} pages.")

    def read(self):
        print(f"You start reading '{self.title}'... Enjoy! ✨")

# Child Class: EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Call parent constructor
        self.file_size = file_size  # in MB

    # Overriding info() 
    def info(self):
        print(f"💻 '{self.title}' by {self.author}, {self.pages} pages, File size: {self.file_size}MB.")

    def download(self):
        print(f"Downloading '{self.title}'... ({self.file_size}MB)")
        

# Example usage
f1 = Book("Atomic Habits", "James Clear", 320)
f1.info()
f1.read()

b2 = EBook("Python Crash Course", "Eric Matthes", 540, 25)
b2.info()
b2.download()




# 2 Polymorphism Challenge
# Base Class
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Subclasses
class Dog(Animal):
    def move(self):
        print("🐕 The dog runs on land.")

class Bird(Animal):
    def move(self):
        print("🐦 The bird flies in the sky.")

class Fish(Animal):
    def move(self):
        print("🐠 The fish swims in water.")

# Example usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()  
