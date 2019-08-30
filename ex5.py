name = 'Glenn Aranas'
age = 35 # Not a lie
height = 78 * 2.54 # inches to cm
weight = 150 # lbs
eye_color = 'Brown'
teeth_color = 'White'
hair_color = 'Black'
# Convertion chart
inch_to_cm = 2.54
lbs_to_kg = 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches or {round(height * inch_to_cm)} centimeters tall")
print(f"He's {weight} pounds or {round(weight * lbs_to_kg)} kilograms heavy.")
print("Actually, that's not too heavy but bulky in the mid-section.")
print(f"He's got {eye_color} eyes and {hair_color} hair.")
print(f"His teeth are usually {teeth_color} depending on the coffee.")

# this line is tricky, try not to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")
