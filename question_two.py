# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 

# SOLUTION
def calculate_bmi(weight, height):
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        print(" You are underweight")
    elif 18.5 == bmi <= 24.9:
        print("You have a normal Weight")
    elif 25 == bmi <= 29.9:
        print("You are overweight")
    else:
        print("You are obese")
        
calculate_bmi("weight", "height")
    





# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. 
# Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)

# SOLUTION
def cylinder_volume(radius, height):
    import math
    radius = float(input("Enter the radius value: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = (math. pi) * (radius ** 2) * height
    print(f"The volume of the cylinder of raius {radius} and height {height} is {volume:.2f}")
    
cylinder_volume("radius", "height")