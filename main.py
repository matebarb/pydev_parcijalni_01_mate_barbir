import json, os


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    os.system('cls')
    
    # Varijable
    # Rjecnik ponude
    offer = {}
    # Redni broj kupca
    counter = 1
    # Lista proizvoda za izbor
    items = []
    
    CHARS = 40 * '-'
    
    print("Lista kupaca: ")
    for customer in customers:
        print(f"{counter}. {customer['name']}")
        counter += 1 
    
    print()
    customer_choice = int(input("Selektirajte kupca: ")) - 1
    customer = customers[customer_choice]
    os.system('cls')
    print("Kreirajte datum ponude.")
    print()
    year = input("Unesite godinu: ")
    month = input("Unesite mjesec: ")
    day = input("Unesite dan: ")
    date = f'{year}-{month}-{day}'
    
    # Dodavanje proizvoda u ponude
    while True:
        os.system('cls')
        print()
        print("Lista proizvoda:")
        print(CHARS)
        counter = 1
        for product in products:
            print(f"{counter}. {product['name']} \nOpis proizvoda: {product['description']} \nCijena: {product['price']:.2f}")
            print(CHARS)
            counter += 1
        
        product_choice = int(input("Odaberite proizvod: ")) - 1
        product = products[product_choice]
        
         # Unos kolicine
        quantity = int(input(f"Unesite kolicinu za {product['name']}: "))
        
        # Racunanje ukupne cijene za taj proizvod
        item_total = quantity * product['price']
        
        # Dodavanje proizvoda u items listu 
        item = {
            'product_name': product['name'],
            'product_id': product['id'],
            'description': product['description'],
            'quantity': quantity,
            'price': product['price'],
            'item_total': item_total
        }
        
        items.append(item)
        
        more_items = input("Zelite li dodati još proizvoda? (da/ne): ").lower()
        if more_items != "da":
            break
    # Izračunajte sub_total, tax i total
    sub_total = sum(item['item_total'] for item in items)
    tax = sub_total * 0.10
    total = sub_total + tax
    
    # Generirani broj ponude
    offer_number = len(offers) + 1
    # Dodajte novu ponudu u listu offers
    offer['offer_number'] = offer_number
    offer['customer'] = customer
    offer['date'] = date
    offer['items'] = items
    offer['sub_total'] = sub_total
    offer['tax'] = tax
    offer['total'] = total
    
    offers.append(offer)
    # Pomocna funkcija
    os.system('cls')
    print_offer(offer)

# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    os.system('cls')
    
    while True:
        print("Izaberite opciju:")
        print()
        print("1. Dodajte novi proizvod")
        print("2. Izmjenite proizvod")
        print("3. Izadjite natrag na glavni izbornik")
        print()
        choice = input("Odabrana opcija: ")
        
        # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
        if choice == '1':
            id = len(products) + 1
            name = input('Unesite ime proizvoda: ')
            description = input('Ukratko opisite proizvod: ')
            price = float(input('Unesite cijenu proizvoda: '))
            
            new_product = {}
            new_product['id'] = id
            new_product['name'] = name
            new_product['description'] = description
            new_product['price'] = price
            
            products.append(new_product)
            os.system('cls')
            print(f"Proizvod {name} je uspjesno dodan.")
        # Za izmjenu: selektirajte proizvod i ažurirajte podatke
        elif choice == '2':
            counter = 1
            print("Lista proizvoda:")
            print()
            
            for product in products:
                print(f"{counter}. {product['name']}")
                counter += 1 
                
            product_choice = int(input('Izaberite proizvod koji zelite promijeniti: ')) - 1
            
            if 0 <= product_choice < len(products):
                product = products[product_choice]
                os.system('cls')
                print(f"Izmjena proizvoda: {product['name']}")
                name = input(f"Ime novog proizvoda: ")
                description = input(f"Opis novog proizvoda: ")
                price = float(input(f"Cijena novog proizvoda: "))
                
                product['name'] = name
                product['description'] = description
                product['price'] = price
                
                os.system('cls')
                print(f"Proizvod {product['name']} je uspjesno promijenjen.")
            else:
                print("Neispravan odabir proizvoda.")
            
        elif choice == "3":
            os.system('cls')
            return
        else:
            print("Krivi izbor. Pokušajte ponovo.")
                
# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    os.system('cls')
    while True:
        print()
        print("Izaberite opciju:")
        print()
        print("1. Unesite novog kupca")
        print("2. Ispisi sve kupce")
        print("3. Izadjite natrag na glavni izbornik")
        print()
        
        choice = input("Odabrana opcija: ")
        
        # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
        if choice == '1':
            print('Unesite podatke o novom kupcu:')
            
            name = input('Ime kupca: ')
            email = input('Email kupca: ')
            vat_id = input('VAT ID kupca: ')
            
            new_customer = {}
            new_customer['name'] = name
            new_customer['email'] = email
            new_customer['vat_id'] = vat_id
            
            customers.append(new_customer)
            os.system('cls')
            print(f"Kupac {name} je uspješno dodan.")
        
        # Za pregled: prikaži listu svih kupaca    
        elif choice == "2":
            os.system('cls')
            counter = 1
            print('Lista kupaca:')
            for customer in customers:
                print(f"{counter}. {customer['name']} \n{customer['email']} \n{customer['vat_id']}")
                counter += 1 
            
        elif choice == "3":
            os.system('cls')
            return
        else:
            print('Krivi izbor. Pokusajte ponovo.')
            


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    while True:
        print("Izaberite opciju:")
        print()
        print("1. Prikaz relevantnih ponuda")
        print("2. Prikaz ponud po ID-u")
        print("3. Izadjite natrag na glavni izbornik")
        print()
        
        choice = input("Odabrana opcija: ")
    # Prikaz relevantnih ponuda na temelju izbora


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        print()
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
