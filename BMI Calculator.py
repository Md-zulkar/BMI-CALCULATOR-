def calculate_bmi(weight,height):
    return weight / (height**2)
def waist_to_height(waist,height):
    return waist/height
def body_fat_percentage(bmi,age,gender):
    if gender==1:
        return (1.20+bmi)+(0.23+age)-16.5
    else:
        return (1.20+bmi)+(0.23+age)-5.2
def bmi_interpret(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.5:
        return "Normal Weight" 
    elif 24.5 <= bmi < 29.5:
        return "Overweight"
    else:
        return "Obesity"
def main():
    print("\n Welcome to BMI claculator \n ")
    
    #user input
    weight=float(input("Enter the weight(kg):"))
    height=float(input("Enter the height(m):"))
    Age=int(input("Enter the Age:"))
    Gender=int(input("Enter the Gender (1 for male, 0 for female):"))
    waist=float(input("Enter your  waist circumference (cm) :"))

    #Calculation
    bmi=calculate_bmi(weight,height)
    wth_ratio = waist_to_height(waist,height*100) # convert height to cm for ratio
    body_fat=body_fat_percentage(bmi, Age, Gender)
    category=bmi_interpret(bmi)

    #result
    print("\n ...Result... \n")
    print(f"-> BMI: {bmi:.2f}")
    print(f"-> Waist to height ratio: {wth_ratio:.2f}")
    print(f"-> Estimated body fat percentage: {body_fat:.2f}%")

    #Health interpretation
    if wth_ratio > 0.5:
        print("-> Warning: Waist to height ratio indicates higher health risks.")
    else:
        print("-> your waist to height ratio indicate within healthy range.")
if __name__=="__main__":
    main()