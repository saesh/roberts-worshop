from icecream import ic

zahlen_liste = [1, 2, 3, 5, 6, 7, 8, 9]
wort_liste = ['Name', 'benennen', 'Auto', 'kochen', 'Film']

doubled_list = [num*2 for num in zahlen_liste if num % 2 == 0]
ic(doubled_list)

summed_list = sum([item for item in zahlen_liste ])
ic(summed_list)

first_letter_list = [word for word in wort_liste if word[0] == word[0].upper()]
ic(first_letter_list)

qudrat_bis_zehn_liste = [i**2 for i in range(11)]
ic(qudrat_bis_zehn_liste)

gerade_zahlen = [zahl for zahl in zahlen_liste if zahl %2 == 0]
ic(gerade_zahlen)

#3. Verschachtelte Schleifen: Erstelle eine Liste der Paare (i, j) für i von 1 bis 3 und j von 1 bis 3.
boxed_zahlen = [[i,j] for i in range(1,4) for j in range(1,4)]
ic(boxed_zahlen)

# 5. Wörter filtern: Erstelle eine Liste der Wörter in einem Satz, die mehr als 3 Buchstaben haben.
satz = "Dies ist ein Beispiel eines Satzes mit verschiedenen Wortlaengen"
more_than_three_chars = [wort for wort in satz.split() if len(wort) > 3]
ic(satz) 
ic(more_than_three_chars) 

# 6. Summenbildung: Berechne die Summe der Quadrate der Zahlen von 1 bis 5.
summierte_quadrate_bis5 = [i**2 for i in range(1,6)]
ic(summierte_quadrate_bis5)

# 7. Doppelte Schleifen mit Bedingungen: Erstelle eine Liste der Quadrate der Zahlen von 1 bis 10, wenn die Zahl größer als 5 ist.
qudrate_summiert_ab5 = [i**2 for i in range(1,11) if i > 5]
ic(qudrate_summiert_ab5)

# 8. Setzen von Bedingungen mit else: Erstelle eine Liste der Quadrate der Zahlen von 1 bis 10, `wenn die Zahl gerade ist, andernfalls verdopple die Zahl.
aufgabe_8liste = [i**2 if i % 2 == 0 else  i * 2  for i in range(1,11)]
ic(aufgabe_8liste)