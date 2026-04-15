contacts = { "Ali": "70123456", "Mariam": "65000000", "Paul": "78000000" }
print(f"Voici le numéro de Mariam {contacts["Mariam"]}")
contacts["Fatou"]="76000000"
contacts.__delitem__("Paul")
if "Ali" in contacts:
    print("Ali est dans les contacts") 
print(f"Voici les noms {list(contacts.keys())}")
print(f"Voici les numéros {list(contacts.values())}")
