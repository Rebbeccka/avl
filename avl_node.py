# -*- coding: utf-8 -*-

class AVLNode:
    """Definícia triedy AVLNode, reprezentuje uzol v AVL strome"""

    def __init__(self, key, value):
        """Konstruktor"""
        self.key = key  # Kľúč uzla
        self.value = value  # Hodnota uzla
        self.height = 1  # Výška uzla (počiatočná hodnota 1)
        self.left = None  # Odkaz na ľavého potomka
        self.right = None  # Odkaz na pravého potomka
