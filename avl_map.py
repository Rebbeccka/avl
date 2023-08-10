# -*- coding: utf-8 -*-
from avl_node import AVLNode


class AVLMap:
    """Definícia triedy AVLMap, reprezentuje mapu s vyvážením AVL"""

    def __init__(self):
        self.root = None

    def height(self, node) -> int:
        """Metóda height vráti výšku uzla (pokiaľ je uzol None, výška je 0)"""
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        """Metóda update_height aktualizuje výšku uzla podľa výšky jeho potomkov"""
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        """Metóda balance_factor vráti rozdiel výšky medzi ľavým a pravým podstromom"""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        """Metóda left_rotate vykoná rotáciu uzla doprava"""
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def right_rotate(self, y):
        """Metóda right_rotate vykoná rotáciu uzla doľava"""
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, key, value):
        """Metóda insert vloží nový uzol s daným kľúčom a hodnotou do AVL stromu"""
        if self.contains_value(value):
            print(f"Hodnota {value} už existuje v mape.")
            return
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        """Rekurzívna metóda _insert vloží nový uzol do podstromu daného uzla"""
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:  # Kľúč už existuje, aktualizujeme hodnotu
            node.value = value
            return node

        self.update_height(node)

        balance = self.balance_factor(node)

        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get(self, key):
        """Metóda get získa hodnotu pre zadaný kľúč z AVL stromu"""
        return self._get(self.root, key)

    def _get(self, node, key):
        """Rekurzívna metóda _get získa hodnotu pre zadaný kľúč z podstromu daného uzla"""
        if node is None:
            raise KeyError(f"Kľúč '{key}' nebol nájdený")

        if key == node.key:
            return node.value
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    def contains(self, key):
        """Metóda contains skontroluje, či je zadaný kľúč obsiahnutý v AVL strome"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        """Metóda remove odstráni uzol s daným kľúčom z AVL stromu"""
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        """Rekurzívna metóda _remove odstráni uzol s daným kľúčom z podstromu daného uzla"""
        if node is None:
            raise KeyError("Kľúč nebol nájdený")

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:

            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._remove(node.right, successor.key)

        self.update_height(node)

        balance = self.balance_factor(node)

        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _min_value_node(self, node):
        """Metóda _min_value_node vráti uzol s najmenším kľúčom v podstrome daného uzla"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __getitem__(self, key):
        """Metóda __getitem__ slúži na získanie hodnoty pre zadaný kľúč pomocou operátora []"""
        return self.get(key)

    def __setitem__(self, key, value):
        """Metóda __setitem__ slúži na vloženie nového uzla """
        self.insert(key, value)

    def __delitem__(self, key):
        """Metóda __delitem__ slúži na odstránenie uzla """
        self.remove(key)

    def __contains__(self, key):
        """Metóda __contains__ slúži na overenie, či je zadaný kľúč obsiahnutý v AVL strome"""
        return self.contains(key)

    def __iter__(self):
        """Metóda __iter__ slúži na iteráciu cez kľúče v AVL strome (inorder prehľadávanie)"""
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        """Metóda _inorder_traversal rekurzívne prehľadáva AVL strom inorder a vracia kľúče"""
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node.key
            yield from self._inorder_traversal(node.right)

    def contains_value(self, value):
        """Metóda contains_value skontroluje, či je daná hodnota obsiahnutá v AVL strome"""
        return self._contains_value(self.root, value)

    def _contains_value(self, node, value):
        """Rekurzívna metóda _contains_value skontroluje, či je daná hodnota obsiahnutá v podstrome daného uzla"""
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._contains_value(node.left, value)
        else:
            return self._contains_value(node.right, value)



