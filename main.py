# -*- coding: utf-8 -*-
from avl_map import AVLMap
from zobraz_menu import display_menu


def main():
    avl_map = AVLMap()

    running: bool = True

    while running:
        display_menu()
        choice = input("Vyberte číslo akcie: ")

        if choice == "1":
            key = input("Zadajte kľúč: ")
            value = input("Zadajte hodnotu: ")

            try:
                value = int(value)
                if avl_map.contains_value(value):
                    print(f"Hodnota {value} už existuje v mape.")
                else:
                    avl_map.insert(key, value)
                    print("Kľúč a hodnota boli vložené do mapy.")
            except ValueError:
                print("Hodnota musí byť číslo")

        elif choice == "2":
            key = input("Zadajte kľúč, pre ktorý chcete získať hodnotu: ")
            try:
                value = avl_map.get(key)
                print(f"Hodnota pre kľúč '{key}': {value}")
            except KeyError:
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
            running = False

        else:
            print("Neplatná voľba. Zadajte číslo od 1 do 6.")


if __name__ == "__main__":
    main()
