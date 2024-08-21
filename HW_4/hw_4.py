
import math

def obsah_kruhu(polomer):
    return math.pi * polomer ** 2


def obvod_kruhu(polomer):
    return 2 * math.pi * polomer


polomer = 5  # Zadej poloměr pro testování

obsah = obsah_kruhu(polomer)
obvod = obvod_kruhu(polomer)

print(f"Pro kruh s poloměrem {polomer}:")
print(f"Obsah kruhu je: {obsah:.2f}")
print(f"Obvod kruhu je: {obvod:.2f}")
