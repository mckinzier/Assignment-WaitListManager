# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name):
        self.name = name  # Store the customer's name
        self.next = None  # Pointer to the next node in the list    
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    def add_front(self, name):
        new_node = Node(name)  # Create a new node with the customer's name
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to be the new node

    def add_end(self, name):
        new_node = Node(name)  # Create a new node with the customer's name
        if not self.head:  # If the list is empty, set the new node as head
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node  # Link the last node to the new node

    def remove(self, name):
        current = self.head
        previous = None
        while current:
            if current.name == name:  # If the customer is found
                if previous:  # If it's not the head node
                    previous.next = current.next  # Bypass the current node
                else:  # If it's the head node
                    self.head = current.next  # Update head to next node
                return True  # Indicate successful removal
            previous = current
            current = current.next
        return False  # Indicate customer not found

    def print_list(self):
        current = self.head
        if not current:
            print("The waitlist is empty.")
            return
        while current:
            print(current.name)  # Print each customer's name
            current = current.next  


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
