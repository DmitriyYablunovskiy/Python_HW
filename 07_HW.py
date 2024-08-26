
eu_cities = [
    ['Berlín', 3669491, 891],
    ['Madrid', 3223334, 604],
    ['Řím', 2872800, 1285],
    ['Paříž', 2165423, 105],
    ['Bukurešť', 1883425, 228],
    ['Budapešť', 1746344, 525],
    ['Varšava', 1790658, 517],
    ['Vídeň', 1921153, 414],
    ['Hamburk', 1841179, 755],
    ['Barcelona', 1620343, 101]
]

total_population = 0
max_population_city = eu_cities[0] 
min_population_city = eu_cities[0]  

for city in eu_cities:
    total_population += city[1]
    if city[1] > max_population_city[1]:
        max_population_city = city
    elif city[1] < min_population_city[1]:
        min_population_city = city

print(f"Celkový počet obyvatel ve všech městech je: {total_population}")
print(f"Město s největším počtem obyvatel je: {max_population_city[0]} s {max_population_city[1]} obyvateli.")
print(f"Město s nejmenším počtem obyvatel je: {min_population_city[0]} s {min_population_city[1]} obyvateli.")
