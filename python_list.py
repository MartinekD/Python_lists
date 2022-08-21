#python - lists
#seznamy pythonu

#definice seznamu
ovoce = ["jablko", "banán", "třešeň", "meloun", "jahoda"]
print(ovoce)

#definice seznamu - umožňuje duplicitu
ovoce = ["jablko", "banán", "třešeň", "meloun", "jahoda", "třešeň", "meloun"]
print(ovoce)

#délka seznamu
print("Délka seznamu:", len(ovoce))

#seznam může obsahovat různé datové typy
typy = ["abc", 34, True, 40, "male"]
print(typy)

print(type(typy))

#vytiskne druhou položku seznamu
print("Druhá položka seznamu je: ", ovoce[1])

#vytiskne poslední a předposlední položku seznamu
print("Poslední položka seznamu je: ", ovoce[-1],"Předposlední položka seznamu je: ", ovoce[-2])

#vytiskne třetí, čtvrtou a pátou položku seznamu
#Vyhledávání bude začínat na indexu 2 (zahrnuto) a končit na indexu 5 (není zahrnuto).
print("Třetí až pátá položka seznamu je: ", ovoce[2:5])

#vytiskne první až čtvrtou položku seznamu
print("První až čtvrtá položka seznamu je: ", ovoce[:4])

#vytiskne položky od třetí pozice do konce seznamu
print("Třetí až poslední položka seznamu je: ", ovoce[2:])

#vytiskne položky od druhé pozice do konce seznamu
print("Druhá až předposlední položka seznamu je: ", ovoce[-4:-1])

#zkontroluje, zda existuje položka jahoda
if "jahoda" in ovoce:
  print("Ano, jahoda je v seznamu")
