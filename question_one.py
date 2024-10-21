# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as
# input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 

# SOLUTION
def classify_temperature():
    temperature_value = float(input("Enter the temperature value in °C:  "))
    
    if temperature_value < 0:
        print("The temperature is freezing")
    elif 0 == temperature_value <= 10:
        print("The temperature is cold")
    elif 11 == temperature_value <= 20:
        print("The temperature is moderate")
    elif 21 == temperature_value <= 30:
        print("The temperature is warm")
    else:
        print("The temperature is hot.")
        
classify_temperature()






# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. 
# What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard
# and provide the answer in 1 decimal place
def sphere_volume():
    radius = float(input("Enter the radius value: "))
    import math
    pie = math.pi   
    volume = (4/3) * pie * radius**2
    print(f"The volume of the sphere with radius {radius} is {volume:.1f}")
    
sphere_volume() 