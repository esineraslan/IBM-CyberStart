import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7,8)]
distances = []

# Öklid mesafesini hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
# Mesafelerin hesaplanması ve distances listesine eklenmesi
for a in range(len(points)):
    for b in range(a + 1, len(points)):
        distances.append(euclideanDistance(points[a], points[b]))

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonucun yazdırılması
print("Minimum mesafe: ", min_distance)