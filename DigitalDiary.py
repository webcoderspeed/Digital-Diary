import sqlite3 as db
import os

connection = db.connect('data')
cursor = connection.cursor()
query = """create table if not exists diary
(sno int(3) primary key,name varchar(20), address varchar(50), contact_number varchar(10), 
email varchar(20), birthday date);
"""
cursor.execute(query)

def insert_record():
    sno = input("Enter Serial Number: ")
    name = input("Enter the Name:")
    address = input("Enter the Address: ")
    contact_number = input("Enter the Contact Number: ")
    email = input("Enter the Email: ")
    birthday = input("Enter the Birthdate: ")
    query = f"""insert into diary values({sno}, '{name}', '{address}', '{contact_number}', '{email}','{birthday}')"""
    cursor.execute(query)
    connection.commit()
    print("Record Inserted Successfuly!")

def update_record():
    def update_name():
        sno = input("Enter the Serial Number: ")
        name = input("Enter New Name: ")
        query = f"""update diary set name = '{name}' where sno = {sno}"""
        cursor.execute(query)
        connection.commit()

    def update_address():
        name = input("Enter the Name: ")
        address = input("Enter New Address: ")
        query = f"""update diary set address = '{address}' where name = {name}
        """ 
        cursor.execute(query)
        connection.commit()

    def update_contact_number():
        name = input("Enter the Name: ")
        contact_number = input("Ënter New Contact Number: ")
        query = f"""update diary set contact_number = '{contact_number}' where name = {name} """
        cursor.execute(query)
        connection.commit()

    def update_email():
        name = input("Enter the Name: ")
        email = input("Ënter New email: ")
        query = f"""update diary set email = '{email}' where name = {name} """
        cursor.execute(query)
        connection.commit()

    def update_birthday():
        name = input("Enter the Name: ")
        birthday =  input("Enter your Birthday: ")
        query = f"""update diary set birthday = '{birthday}' where name = {name}"""
        cursor.execute(query)
        connection.commit()

    while True:
        os.system('cls')
        choice = int(input("""####### MAIN MENU ########
        1) Update Name
        2) Update Address
        3) Update Contact Number
        4) Update Email
        5) Update Birthday
        6) LogOut
        Enter your choice: """))
        if choice == 1:
            update_name()
            print("Name Updated!")
        elif choice == 2:
            update_address()
            print("Address Updated!")
        elif choice == 3:
            update_contact_number()
            print("Contact Updated!")
        elif choice == 4:
            update_email()
            print("Email Updated!")
        elif choice == 5:
            update_birthday()
            print("Birthday Updated!")
        elif choice == 6:
            print("You are logged out!")
            break
        else:
            print("Invalid Choice")
        os.system('pause')

def view_record():
    query = 'select * from diary'
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

def delete_record():
    name = input("Enter the Name: ")
    query = f'delete from diary where name = "{name}"'
    cursor.execute(query)
    connection.commit()
    print("Record Delete Successfully!")

def search_record():
    def search_by_name():
        name = input('Enter the Name: ')
        query = f'select * from diary where name = "{name}" '
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
    def search_by_birthday():
        birthday = input('Enter Birthday: ')
        query = f'select * from diary where birthday = "{birthday}" '
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)

    while True:
        os.system('cls')
        choice = int(input("""########## MAIN MENU ##############
        1) Search By Name
        2) Search By Birthday
        3) LogOut 
        Enter your choice: """))
        if choice == 1:
            search_by_name()
        elif choice == 2:
            search_by_birthday()
        elif choice == 3:
            print("You are logged out!")
            break
        else:
            print('Invalid Choice')
        os.system('pause')

    

while True:
    os.system('cls')
    choice = int(input("""########## MAIN MENU ##############
    1) Insert Record
    2) Update Record
    3) View Record
    4) Delete Record
    5) Search Record 
    6) LogOut 
    Enter your choice: """))
    if choice == 1:
        insert_record()
    elif choice == 2:
        update_record()
    elif choice == 3:
        view_record()
    elif choice == 4:
        delete_record()
    elif choice == 5:
        search_record()
    elif choice == 6:
        print("You are Logged out!")
        break
    else:
        print("Invalid Choice")
    os.system('pause')
cursor.close()
connection.close()
