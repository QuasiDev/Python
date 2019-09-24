formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "All purpose",
    "Acrylic Latex",
    "Caulk Plus Silicone",
    "that can last for 40 years!"
))
