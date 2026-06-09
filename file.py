class Book:
    def __init__(self, title, author, year, price, available):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.available = available

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Price:", self.price)
        print("Available:", self.available)
        print()


def max_price_book(book1, book2):
    if book1.price > book2.price:
        print("Book with Maximum Price:")
        book1.display_details()
    else:
        print("Book with Maximum Price:")
        book2.display_details()


book1 = Book("MEMORY STRAND", "Logan Fell", 2020, 500, True)
book2 = Book("MEMORY STRAND 2", "Logan Fell", 2022, 750, False)

max_price_book(book1, book2)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create 5 nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Store head
head = node1

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Display Linked List
temp = head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")