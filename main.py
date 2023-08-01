from avl_map import AVLMap
from zobraz_menu import zobraz_menu



if __name__ == "__main__":
    avl_mapa = AVLMap()

    while True:
        zobraz_menu()
        volba = input("Vyberte číslo akcie: ")

        if volba == "1":
            kluc = input("Zadajte kľúč: ")
            hodnota = input("Zadajte hodnotu: ")
            avl_mapa.vloz(kluc, hodnota)
            print("Kľúč a hodnota boli vložené do mapy.")
        elif volba == "2":
            kluc = input("Zadajte kľúč, pre ktorý chcete získať hodnotu: ")
            if kluc in avl_mapa:
                hodnota = avl_mapa.ziskaj(kluc)
                print(f"Hodnota pre kľúč '{kluc}': {hodnota}")
            else:
                print(f"Kľúč '{kluc}' nebol nájdený v mape.")
        elif volba == "3":
            kluc = input("Zadajte kľúč, ktorý chcete skontrolovať: ")
            if kluc in avl_mapa:
                print(f"Kľúč '{kluc}' je obsiahnutý v mape.")
            else:
                print(f"Kľúč '{kluc}' nie je obsiahnutý v mape.")
        elif volba == "4":
            kluc = input("Zadajte kľúč, ktorý chcete odstrániť: ")
            try:
                del avl_mapa[kluc]
                print(f"Kľúč '{kluc}' bol úspešne odstránený z mapy.")
            except KeyError:
                print(f"Kľúč '{kluc}' nebol nájdený v mape.")
        elif volba == "5":
            print("Obsah mapy:")
            for kluc in avl_mapa:
                print(f"{kluc}: {avl_mapa[kluc]}")
        elif volba == "6":
            print("Ukončujem program.")
            break
        else:
            print("Neplatná voľba. Zadajte číslo od 1 do 6.")

