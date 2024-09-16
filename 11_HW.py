
import matplotlib.pyplot as plt

data = {
    'Praha': 1_384_732,
    'Brno': 400_566,
    'Ostrava': 284_765,
    'Plzeň': 185_599,
}

mesta = list(data.keys())
populace = list(data.values())

plt.bar(mesta, populace, color='skyblue')

plt.title('Populace českých měst')
plt.xlabel('Města')
plt.ylabel('Počet obyvatel')


plt.show()
