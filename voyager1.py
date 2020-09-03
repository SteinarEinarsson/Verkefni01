
days = int(input('Number of days after 9/25/09: '))
orig_miles = 16637000000
Dist_miles = orig_miles + (days*24*38241)
print("Miles from the sun:" ,Dist_miles)

Dist_km = int(round(1.609344*Dist_miles))
print("Kilometers from the sun:" ,Dist_km)

AU_dist = int(round(Dist_miles/92955887.6))
print("AU from the sun:", AU_dist)
