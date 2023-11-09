#!/usr/bin/python3
"""  plane assignment kmom01, unit converter, Karam Matar """
height_in_meters = float(input("Höjd över havet i meter: "))
speed_in_km = float(input("hastighet i km/h: "))
temp_in_cel = float(input("Temp utanför flygplanet i celcius: "))

height_in_feet = height_in_meters * 3.28084
speed_in_mph = speed_in_km * 0.621371

temp_in_fahr = (temp_in_cel * 9/5) + 32

print(" Höjd över havet i feet ",  round(height_in_feet, 2))

print("hastighet i mph " , round(speed_in_mph, 2))
print("temp in fahr " , round(temp_in_fahr, 2))
