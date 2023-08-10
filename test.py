from avl_map import AVLMap


def main():
    avl_map = AVLMap()

    # Testovacie príklady - vkladanie hodnôt do mapy
    avl_map.insert(5, )
    avl_map.insert(3, )
    avl_map.insert(7, )
    avl_map.insert(2, )
    avl_map.insert(4, )
    avl_map.insert(6, )
    avl_map.insert(8, )
    avl_map.insert(1, )

    # Vypíšeme obsah mapy pomocou iterácie cez kľúče
    print("Obsah mapy:")
    for key in avl_map:
        print(f"Kľúč: {key}, Hodnota: {avl_map[key]}")

    # Testovacie príklady - odstránenie hodnôt z mapy
    key_to_remove = 4
    if key_to_remove in avl_map:
        print(f"Odstraňujem kľúč '{key_to_remove}' z mapy.")
        del avl_map[key_to_remove]
    else:
        print(f"Kľúč '{key_to_remove}' nebol nájdený v mape.")

    key_to_remove = 10
    if key_to_remove in avl_map:
        print(f"Odstraňujem kľúč '{key_to_remove}' z mapy.")
        del avl_map[key_to_remove]
    else:
        print(f"Kľúč '{key_to_remove}' nebol nájdený v mape.")

    # Vypíšeme obsah mapy po odstránení hodnôt
    print("\nObsah mapy po odstránení hodnôt:")
    for key in avl_map:
        print(f"Kľúč: {key}, Hodnota: {avl_map[key]}")

    # Testovacie príklady - vyhľadávanie hodnôt v mape
    key_to_find = 5
    if key_to_find in avl_map:
        print(f"Hodnota pre kľúč '{key_to_find}': {avl_map.get(key_to_find)}")
    else:
        print(f"Kľúč '{key_to_find}' nebol nájdený v mape.")

    key_to_find = 10
    if key_to_find in avl_map:
        print(f"Hodnota pre kľúč '{key_to_find}': {avl_map.get(key_to_find)}")
    else:
        print(f"Kľúč '{key_to_find}' nebol nájdený v mape.")


if __name__ == "__main__":
    main()
