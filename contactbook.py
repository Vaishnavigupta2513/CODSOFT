contacts = []
def add_contact():
    Name=input("Enter The Name:")
    Phone=input("Enter The PhoneNumber:")
    Email=input("Enter The Email:")
    Address=input("Enter The Address:")
    contact = {"Name":Name,"Phone":Phone,"Email":Email,"Address":Address}
    contacts.append(contacts)
    print(f"Contact {Name} Added Successfully")
def view_contacts():
    if not contacts:
        print("No Contacts Saved")
    else:
        for id, contact in enumerate(contacts,start=1):
            print(f"{id}.{contact['Name']}|{contact['Phone']}|{contact['Email']}|{contact['Address']}")
def search_contact():
    search_term = input("Enter your phone number to search").lower()
    found = False
    for contact in contacts:
        if search_term in contact['Name'].lower() or search_term in contact['Phone']:
             print(f"{contact['Name']}|{contact['Phone']}|{contact['Email']}|{contact['Address']}")
             found = True
             if not found:
                 print("No Contact found with that name or phone number.")
def update_contact():
    view_contacts()
    try:
        index=int(input("Enter Contact Number To Update"))-1
        if 0<= index < len (contacts):
            Name=input("Enter The Name:")
            Phone=input("Enter The PhoneNumber:")
            Email=input("Enter The Email:")
            Address=input("Enter The Address:")
            contacts[index]={"Name":Name,"Phone":Phone,"Email":Email,"Address":Address}
            print("Contact Updated Successfully")
        else:
            ("Invalid Contact Number")
    except ValueError:
        print("Invalid Input")                    
def delete_contact():
    view_contacts()
    try:
        index=int(input("Enter Contact Number To Delete"))-1
        if 0<= index < len (contacts):
            delete_contact == contacts.pop(index)
            print(f"Contact{delete_contact['Name']} deleted successfully")
        else:
            ("Invalid Contact Number")
    except ValueError:
        print("Invalid Input")
def main():
    while True:
        print("CONTACT BOOK")
        print("1.Add Contact")
        print("2.View Contact")
        print("3.Search Contact")
        print("4.Update Contact")
        print("5.Delete Contact")
        print("6.Exit")
        choice=input("Choose An Option : ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice =='5':
            delete_contact()
        elif choice == '6':
            print("Thanks")
            break
        else:
            print("Invalid Option ")
if __name__ == "__main__":
    main()
            
            
            
        
                