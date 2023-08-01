class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None


class AVLMap:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:  # Key already exists, update the value
            node.value = value
            return node

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            raise KeyError("Key not found")
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._remove(node.right, successor.key)

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Left Case
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, key):
        return self.contains(key)

    def __iter__(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node.key
            yield from self._inorder_traversal(node.right)

def zobraz_menu():
    print("1. Vložiť kľúč a hodnotu")
    print("2. Získať hodnotu podľa kľúča")
    print("3. Skontrolovať, či je kľúč obsiahnutý v mape")
    print("4. Odstrániť prvok podľa kľúča")
    print("5. Vypísať celú mapu")
    print("6. Ukončiť program")

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


class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None


class AVLMap:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:  # Key already exists, update the value
            node.value = value
            return node

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            raise KeyError("Key not found")
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._remove(node.right, successor.key)

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Left Case
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, key):
        return self.contains(key)

    def __iter__(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node.key
            yield from self._inorder_traversal(node.right)

def zobraz_menu():
    print("1. Vložiť kľúč a hodnotu")
    print("2. Získať hodnotu podľa kľúča")
    print("3. Skontrolovať, či je kľúč obsiahnutý v mape")
    print("4. Odstrániť prvok podľa kľúča")
    print("5. Vypísať celú mapu")
    print("6. Ukončiť program")

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

