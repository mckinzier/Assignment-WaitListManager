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
            waitlist.add_front(name)
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?

I used a linked list to manage a waitlist of customers. It holds customer names in nodes that all link to each other. 
The entry point to the list is the first node which is called the head. The head is important because it allows us to 
access the entire list. If we lose the head, we lose access to all the nodes in the list. Each node has a name and a next 
pointer which connects each customer to the next customer in the waitlist. The add_front method adds a new 
customer to the beginning of the list and the add_end method adds a customer to the end. The remove method searches for
a customer's name and removes their node from the list. The print_list method goes through each node and prints the customers 
in the waitlist. An angineer might need a custom list like this when they need to store data that is constantly being added or 
removed. For example, a linked list could be useful for a waitlist, queue, playlist, or other collection where the order of 
items can change. Python already has built-in lists, but creating a custom linked list can give an engineer more control over how 
the data is connected and can help them understand how data structures work. Another example could be when an engineer is working 
with a large amount of data and needs to optimize memory usage. A linked list can be more efficient than a built-in list in 
certain scenarios, especially when it comes to inserting and deleting elements. Overall, this custom linked list implementation 
provides a simple yet effective way to manage a dynamic collection of customer names in a waitlist scenario.

