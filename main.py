AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan"]

print("********************************")
print("AutoCountry Vehicle Finder v0.1")
print("********************************")
print("Pleas Enter the following number below from the following menu: ")
print("")
print("1. PRINT all Authorized Vehicles")
print("2. Exit")

number = int(input())
if number == 1:
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
  for truck in AllowedVehiclesList:
    print(truck)
  
elif number == 2:
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")