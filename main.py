# -*- coding: utf-8 -*-
from avl_map import AVLMap
from zobraz_menu import display_menu

def main():
    avl_map = AVLMap()

    while True:
        display_menu()
        choice = input("Vyberte číslo akcie: ")

        if choice == "1":
            key = input("Zadajte kľúč: ")
            value = input("Zadajte hodnotu: ")
            avl_map.insert(key, value)
            print("Kľúč a value boli vložené do mapy.")
        elif choice == "2":
            key = input("Zadajte kľúč, pre ktorý chcete získať hodnotu: ")
            if key in avl_map:
                value = avl_map.get(key)
                print(f"Hodnota pre kľúč '{key}': {value}")
            else:
                print(f"Kľúč '{key}' nebol nájdený v mape.")
        elif choice == "3":
            key = input("Zadajte kľúč, ktorý chcete skontrolovať: ")
            if key in avl_map:
                print(f"Kľúč '{key}' je obsiahnutý v mape.")
            else:
                print(f"Kľúč '{key}' nie je obsiahnutý v mape.")
        elif choice == "4":
            key = input("Zadajte kľúč, ktorý chcete odstrániť: ")
            try:
                del avl_map[key]
                print(f"Kľúč '{key}' bol úspešne odstránený z mapy.")
            except KeyError:
                print(f"Kľúč '{key}' nebol nájdený v mape.")
        elif choice == "5":
            print("Obsah mapy:")
            for key in avl_map:
                print(f"{key}: {avl_map[key]}")
        elif choice == "6":
            print("Ukončujem program.")
            break
        else:
            print("Neplatná voľba. Zadajte číslo od 1 do 6.")


if __name__ == "__main__":
    main()

