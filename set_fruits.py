 #Create a set of 10 fruits
fruits = {"Apple", "Banana", "Orange", "Mango", "Guava",
          "Pineapple", "Papaya", "Litchi", "Grapes", "Watermelon"}

# Create a set of 5 summer fruits
summer = {"Mango", "Litchi", "Watermelon", "Papaya", "Pineapple"}

# Create a set of 5 winter fruits
winter = {"Apple", "Orange", "Grapes", "Guava", "Papaya"}

# i) Print all fruits in the three sets
print("All Fruits:", fruits)
print("Summer Fruits:", summer)
print("Winter Fruits:", winter)

# ii) Print the fruits present in both summer and winter
common = summer & winter
print("\nCommon fruits in Summer and Winter:", common)

# iii) Print the fruits only in summer but not in fruits
only_summer = summer - fruits
print("\nOnly in Summer but not in Fruits:", only_summer)

# iv) Print the fruits present in summer and winter but not in fruits
summer_winter_not_fruits = (summer | winter) - fruits
print("\nPresent in Summer and Winter but not in Fruits:", summer_winter_not_fruits)

# v) Check whether Orange is present in Fruits or not
if "Orange" in fruits:
    print("\nOrange is present in Fruits.")
else:
    print("\nOrange is not present in Fruits.")

# vi) Find in which set Pineapple is present
print("\nPineapple is present in:")
if "Pineapple" in fruits:
    print("- Fruits Set")
if "Pineapple" in summer:
    print("- Summer Set")
if "Pineapple" in winter:
    print("- Winter Set")
# vii) Find in which set Pineapple is present

fruit = "Pineapple"

print("Pineapple is present in:")

if fruit in fruits:
    print("Fruits Set")

if fruit in summer:
    print("Summer Fruits Set")

if fruit in winter:
    print("Winter Fruits Set")

if fruit not in fruits and fruit not in summer and fruit not in winter:
    print("Pineapple is not present in any set.")
