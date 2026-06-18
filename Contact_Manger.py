#took customer contact list from gemini
customer_contacts = {
    "c1": {"name": "Ram", "contact": 9876543210},
    "c2": {"name": "Rahul", "contact": 9812345678},
    "c3": {"name": "Rohit", "contact": 9765432109},
    "c4": {"name": "Aarav", "contact": 9654321098},
    "c5": {"name": "Ananya", "contact": 9543210987},
    "c6": {"name": "Aditya", "contact": 9432109876},
    "c7": {"name": "Diya", "contact": 9321098765},
    "c8": {"name": "Arjun", "contact": 9210987654},
    "c9": {"name": "Isha", "contact": 9109876543},
    "c10": {"name": "Vivaan", "contact": 9019876542},
    "c11": {"name": "Kavya", "contact": 8908765431},
    "c12": {"name": "Sai", "contact": 8897654320},
    "c13": {"name": "Riya", "contact": 8786543219},
    "c14": {"name": "Aaryan", "contact": 8675432108},
    "c15": {"name": "Sanya", "contact": 8564321097},
    "c16": {"name": "Krishna", "contact": 8453210986},
    "c17": {"name": "Pranav", "contact": 8342109875},
    "c18": {"name": "Sneha", "contact": 8231098764},
    "c19": {"name": "Dev", "contact": 8120987653},
    "c20": {"name": "Tanvi", "contact": 8010987652},
    "c21": {"name": "Kabir", "contact": 7909876541},
    "c22": {"name": "Meera", "contact": 7898765430},
    "c23": {"name": "Shray", "contact": 7787654319},
    "c24": {"name": "Tara", "contact": 7676543208},
    "c25": {"name": "Ishaan", "contact": 7565432107},
    "c26": {"name": "Neha", "contact": 7454321096},
    "c27": {"name": "Rohan", "contact": 7343210985},
    "c28": {"name": "Kiara", "contact": 7232109874},
    "c29": {"name": "Amit", "contact": 7121098763},
    "c30": {"name": "Pooja", "contact": 7010987652},
    "c31": {"name": "Vikram", "contact": 9988776655},
    "c32": {"name": "Shruti", "contact": 8877665544},
    "c33": {"name": "Sameer", "contact": 7766554433},
    "c34": {"name": "Payal", "contact": 6655443322},
    "c35": {"name": "Kunal", "contact": 9554433221},
    "c36": {"name": "Divya", "contact": 8443322110},
    "c37": {"name": "Akash", "contact": 7332211009},
    "c38": {"name": "Mitali", "contact": 6221100998},
    "c39": {"name": "Gaurav", "contact": 9110099887},
    "c40": {"name": "Shreya", "contact": 8009988776},
    "c41": {"name": "Mayank", "contact": 7998877665},
    "c42": {"name": "Nisha", "contact": 6887766554},
    "c43": {"name": "Siddharth", "contact": 9776655443},
    "c44": {"name": "Kriti", "contact": 8665544332},
    "c45": {"name": "Abhishek", "contact": 7554433221},
    "c46": {"name": "Riddhi", "contact": 6443322110},
    "c47": {"name": "Deepak", "contact": 9332211009},
    "c48": {"name": "Swati", "contact": 8221100998},
    "c49": {"name": "Varun", "contact": 7110099887},
    "c50": {"name": "Anjali", "contact": 6009988776}
}
while True:
  print("""
  ---- CONTACT MANAGER ----
  PRESS 1 TO ADD NEW CONTACT
  PRESS 2 TO SEARCH CONTACT
  PRESS 3 TO SHOW CONTACTS
  PRESS 4 TO EXIT
  """)

  choice=int(input("Enter your choice: "))

 
  if choice==1:
    name=str(input("Enter name you want to add :"))
    contact=int(input("enter their contact : "))

    try:
      if len(str(contact))!=10 or not contact.isdigit():
          raise ValueError("Enter a valid 10 digit number.")
       
    except ValueError:
         print("Enter a valid 10 digit number.")
 
    
    else:
        next_contact = f"c{len(customer_contacts) + 1}"
        customer_contacts[next_contact]={"name":name, "contact":contact}
        print("Contact added successfully.")

  elif choice==2:
      #search contact
      search_name = input("\nEnter a name to search for: ").lower()

      for contact_id, info in customer_contacts.items():
        if info["name"].lower() == search_name:
              print(f"\nContact Found!")
              print(f"ID: {contact_id}")
              print(f"Name: {info['name']}")
              print(f"Phone: {info['contact']}")
              break
      else:
          print(f"\nNo contact found with the name '{search_name}'.")
  elif choice==3:
    print(customer_contacts)
  
  elif choice==4:
    print("Exiting Contact Manager.")
    break
  else:
      print("Enter valid choice.\nChoose from 1,2,3,4.")
