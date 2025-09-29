from dto.connexion import Connexion
from pprint import pprint

def main():
    Connexion.connect()

    print("All fruits:")
    fruits = Connexion.get_all_fruits()

    for fruit in fruits:
        pprint(fruit)
    
    print("\nFruit by ID:")
    pprint(Connexion.get_fruit_by_id("68d5178c49770a4f56ce5f47"))
    
    print("\nAdd new fruit")
    new_fruit_id = Connexion.add_fruit({"name": "Banana", "origin": "Greenland", "price": 1.5})

    print("\nUpdate fruit")
    Connexion.update_fruit(new_fruit_id, {"quantity": 100})
    pprint(Connexion.get_fruit_by_id(new_fruit_id))

    print("\nDelete fruit")
    Connexion.delete_fruit(new_fruit_id)
    print("\nAll fruits after deletion:")
    fruits = Connexion.get_all_fruits()
    for fruit in fruits:
        pprint(fruit)
 
    Connexion.disconnect()

if __name__ == "__main__":
    main()