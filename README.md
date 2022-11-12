Blackjack: 
Zmienne: 
1.	Zmienna przetrzymująca ilość zakładu: user_cash 
2.	Zmienna przetrzymująca ilość postawionego zakładu: user_bet
3.	Lista przetrzymująca wartość kart: cards 
4.	Lista przetrzymująca wartość kart użytkownika: user_hand
5.	Lista  przetrzymująca wartość kart dilera: deler_hand 
6.	Funkcja wybierająca randomową kartę do listy, jako argument do parametru przyjmuje int 1 lub 2, która wybiera ilość kart: chose_card(cards_amount)
7.	Funkcja, która sumuje ilość kart w liście i sprawdza czy jest większa od danej liczby, funkcja przyjmuje jako argument listę jaka ma zostać zsumowania oraz liczbę do porównania: sum_and_check(list_name, numer_to_check)
8.	O co chodzi ze split? 
9.	Co zrobić jak równe wartość obu list dilera i usera? 
Plan na grę:
-The deck is unlimited in size.
-There are no jokers.
-The Jack/Queen/King all count as 10.
-The the Ace can count as 11 or 1.
-Use the following list as the deck of cards:
-cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
-The cards in the list have equal probability of being drawn.
-Cards are not removed from the deck as they are drawn.
-The computer is the dealer.

