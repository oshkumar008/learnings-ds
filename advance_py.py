Lat = 55.3781
Lon = -3.43597
gridLat = Lat
gridLon = Lon
if abs(Lat) <= 23.45:
    gridLon = int(round(Lon / 0.05) * 1000 * 0.05)
elif abs(Lat) >= 60.533:
    gridLon = int(round(Lon / 0.1) * 1000 * 0.1)
else:
    gridLon = int(round(Lon / 0.075) * 1000 * 0.075)
gridLat = int(round(Lat / 0.075) * 1000 * 0.075)
PostCode = str(gridLat) + ',' + str(gridLon)
print(gridLat, gridLon, PostCode)
