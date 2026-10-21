name = "Ujjwal"
age = 25
score = 0.87
is_ready = True
nothing = None

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Score: {score}")
print(f"Is Ready: {is_ready}")
print(f"Nothing: {nothing}")

if score > 0.9:
    print("Excellent score!")
elif score > 0.8:
    print("Good score!")
else:
    print("Keep trying!")

#mulitline string

print (f"""
Name: {name}
Age: {age}
Score: {score}
Is Ready: {is_ready}
Nothing: {nothing}
""")