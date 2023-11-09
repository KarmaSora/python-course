
"""
allowance = int(input("What is your allowance?"))
cost_of_candy = int(input("What does the candy cost?"))

remaining_money = allowance - cost_of_candy
print( "you have " + str(remaining_money) + "kr left")
"""
# alternitive solutions
"""
None
""" 
#
""" 

#Tid räknare, insert sec, convert to hours and min


total_secounds =  int(input("insert the ammount of secounds"))
time_in_minutes = total_secounds % 60
time_in_hours = time_in_minutes % 60



LÖSNING!!!

secs = int(input("Enter Secs"))
hours = secs //(3600)
sec_left = secs % (3600)

print(f"There are {hours}, hours, {min} min ,and {sec_left}") #Kolla bilder på mobilen




"""




"""
#skriv ett program som omvandlar sek till yen samt  visa summan som är 10x och 100x

tar emot inmatning fråm användare
tar emot antal sek 
gör om dessa till japanska ye
1 SEK = 10.81 YEN

skriva ut hur många YEN det blir samt vad 10 och 100 gånger.

"""
sek = int(input("skriv antalet sek att konvertera: "))
exchange_rate = 10.81

yen = sek * exchange_rate
yen_10 = sek * exchange_rate*10
yen_100 = sek * exchange_rate*100
print(sek, "svenska kronor är", yen, "japanska yen") 
print(sek, "svenska kronor gånger 10 är", yen_10, "japanska yen") 
print(sek, "svenska kronor gånger 100 är", yen_100, "japanska yen") 

