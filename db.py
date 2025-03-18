import mysql.connector as mysql

conn = mysql.connect(host="localhost", user="root", password="28092008")
curs = conn.cursor()
curs.execute("CREATE DATABASE IF NOT EXISTS task_manager")
curs.execute("USE task_manager")
curs.execute("""
    CREATE TABLE IF NOT EXISTS items (
        item_id INT AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(100) NOT NULL,
        state ENUM('pending', 'done') DEFAULT 'pending'
    )
""")

def create_item():
    desc = input("Enter item description: ")
    curs.execute("INSERT INTO items (description) VALUES (%s)", (desc,))
    conn.commit()
    print("Item added.")

def list_items():
    curs.execute("SELECT * FROM items")
    results = curs.fetchall()
    if not results:
        print("No items found.")
    else:
        for row in results:
            print(f"[ID: {row[0]}, Description: {row[1]}, State: {row[2]}]")

def modify_item():
    list_items()
    item_id = input("Enter item ID to modify: ")
    new_desc = input("Enter new description: ")
    curs.execute("UPDATE items SET description = %s WHERE item_id = %s", (new_desc, item_id))
    conn.commit()
    print("Item modified.")

def complete_item():
    list_items()
    item_id = input("Enter item ID to mark as done: ")
    curs.execute("UPDATE items SET state = 'done' WHERE item_id = %s", (item_id,))
    conn.commit()
    print("Item marked as done.")

def remove_item():
    list_items()
    item_id = input("Enter item ID to remove: ")
    curs.execute("DELETE FROM items WHERE item_id = %s", (item_id,))
    conn.commit()
    print("Item removed.")

while True:
    print("\nTask Manager")
    print("1) Add Item")
    print("2) List Items")
    print("3) Modify Item")
    print("4) Complete Item")
    print("5) Remove Item")
    print("6) Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        create_item()
    elif choice == 2:
        list_items()
    elif choice == 3:
        modify_item()
    elif choice == 4:
        complete_item()
    elif choice == 5:
        remove_item()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

curs.close()
conn.close()
