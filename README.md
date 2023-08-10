# Avl Map

Program AVLMap je implementáciou mapy s vyvážením AVL v programovacom jazyku Python. Mapa je dátová štruktúra, ktorá zobrazuje kľúče na hodnoty, podobne ako slovník v Pythone. Vyváženie AVL stromu zabezpečuje efektívne vyhľadávanie, vkladanie a odstraňovanie prvkov.

Účel programu:
Program umožňuje vkladať kľúče a hodnoty do mapy.
Získava hodnotu na základe zadaného kľúča.
Kontroluje, či je daný kľúč obsiahnutý v mape.
Odstraňuje prvok na základe zadaného kľúča.
Vypisuje obsah celej mapy.

Fungovanie programu:
Program spustí hlavnú funkciu main().
Vytvorí sa inštancia AVLMap, ktorá reprezentuje prázdny AVL strom.
Používateľovi sa zobrazí menu s viacerými akciami na výber.

Trieda AVLMap:
Metódy:
__init__(): Inicializuje prázdnu mapu.
height(node): Vráti výšku daného uzla.
update_height(node): Aktualizuje výšku uzla na základe jeho potomkov.
balance_factor(node): Vráti rozdiel výšky medzi ľavým a pravým podstromom.
left_rotate(z): Vykoná rotáciu uzla doprava.
right_rotate(y): Vykoná rotáciu uzla doľava.
insert(key, value): Vloží nový uzol s daným kľúčom a hodnotou do stromu.
_insert(node, key, value): Rekurzívne vloží nový uzol do podstromu daného uzla.
get(key): Získa hodnotu pre zadaný kľúč.
_get(node, key): Rekurzívne získa hodnotu pre zadaný kľúč v podstrome daného uzla.
contains(key): Skontroluje, či je zadaný kľúč obsiahnutý v strome.
remove(key): Odstráni uzol s daným kľúčom zo stromu.
_remove(node, key): Rekurzívne odstráni uzol s daným kľúčom v podstrome daného uzla.
_min_value_node(node): Vráti uzol s najmenším kľúčom v podstrome daného uzla.
__getitem__(key): Získa hodnotu pre zadaný kľúč pomocou operátora [].
__setitem__(key, value): Vloží nový uzol pomocou operátora [].
__delitem__(key): Odstráni uzol pomocou operátora del.
__contains__(key): Overí, či je zadaný kľúč obsiahnutý v strome.
__iter__(): Iteruje cez kľúče v strome (inorder prehľadávanie).
_inorder_traversal(node): Rekurzívne prehľadáva strom inorder a vracia kľúče.
contains_value(value): Skontroluje, či je daná hodnota obsiahnutá v strome.
_contains_value(node, value): Rekurzívne skontroluje, či je daná hodnota obsiahnutá v podstrome daného uzla.


Funkcia display_menu():
Táto funkcia zobrazí na konzolu menu pre používateľa.

Funkcia main():
Hlavná funkcia programu, ktorá interaguje s používateľom a vykonáva operácie.
Postupne spracováva vstupy od používateľa a vykonáva príslušné operácie v závislosti od výberu.
