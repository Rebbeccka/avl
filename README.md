# Avl Map

Program AVLMap je implementáciou mapy s vyvážením AVL stromom v programovacom jazyku Python. Mapa je dátová štruktúra, ktorá zobrazuje kľúče na hodnoty, podobne ako slovník v Pythone. 
Vyváženie AVL stromu zabezpečuje efektívne vyhľadávanie, vkladanie a odstraňovanie prvkov.

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
Postupne spracováva vstupy od používateľa a vykonáva príslušné operácie v závislosti od výberu.


## Trieda AVLMap:
### Metódy:
- Konštruktor: Inicializuje prázdnu mapu.
- height: Vráti výšku daného uzla.
- update_height: Aktualizuje výšku uzla na základe jeho potomkov.
- balance_factor: Vráti rozdiel výšky medzi ľavým a pravým podstromom.
- left_rotate: Vykoná rotáciu uzla doprava.
- right_rotate: Vykoná rotáciu uzla doľava.
- insert: Vloží nový uzol s daným kľúčom a hodnotou do stromu.
- insert: Rekurzívne vloží nový uzol do podstromu daného uzla.
- get: Získa hodnotu pre zadaný kľúč.
- get: Rekurzívne získa hodnotu pre zadaný kľúč v podstrome daného uzla.
- contains: Skontroluje, či je zadaný kľúč obsiahnutý v strome.
- remove: Odstráni uzol s daným kľúčom zo stromu.
- remove: Rekurzívne odstráni uzol s daným kľúčom v podstrome daného uzla.
- min_value_node: Vráti uzol s najmenším kľúčom v podstrome daného uzla.
- getitem: Získa hodnotu pre zadaný kľúč pomocou operátora [].
- setitem: Vloží nový uzol pomocou operátora [].
- delitem: Odstráni uzol pomocou operátora del.
- contains: Overí, či je zadaný kľúč obsiahnutý v strome.
- iter: Iteruje cez kľúče v strome (inorder prehľadávanie).
- inorder_traversal: Rekurzívne prehľadáva strom inorder a vracia kľúče.
- contains_value: Skontroluje, či je daná hodnota obsiahnutá v strome.
- contains_value: Rekurzívne skontroluje, či je daná hodnota obsiahnutá v podstrome daného uzla.


## Funkcia display_menu:
Táto funkcia zobrazí na konzolu menu pre používateľa.
