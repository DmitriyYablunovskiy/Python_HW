
ceny_potravin = {
    'máslo': 30,
    'chleba': 20,
    'sýr': 30,
    'jablko': 5
}


ceny_potravin['mléko'] = 25

nejlevnejsi_produkt = min(ceny_potravin, key=ceny_potravin.get)
nejlevnejsi_cena = ceny_potravin[nejlevnejsi_produkt]

celkova_cena = 4 * ceny_potravin['jablko'] + 1 * ceny_potravin['máslo'] + 2 * ceny_potravin['sýr']


print("Aktualizovaný slovník cen potravin:", ceny_potravin)
print(f"Nejlevnější produkt je {nejlevnejsi_produkt} s cenou {nejlevnejsi_cena} Kč.")
print(f"Celková cena za 4x jablka, 1x máslo a 2x sýr je {celkova_cena} Kč.")

#Práce 2

friends_set1 = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"}
friends_set2 = {"Charlie", "Eve", "Bob", "Frank", "Mallory", "Oscar", "Peggy", "Trent", "Victor", "Walter"}

spolecni_pratele = friends_set1.intersection(friends_set2)

celkem_pratel = friends_set1.union(friends_set2)

print("Společní přátelé:", spolecni_pratele)
print(f"Počet společných přátel: {len(spolecni_pratele)}")
print("Celkový počet unikátních přátel:", len(celkem_pratel))
