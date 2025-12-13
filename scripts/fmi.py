def wait(t):
    from time import sleep
    sleep(t)

def saveData(NAME, FOREHEAD_WEIGHT, FOREHEAD_VOLUME, AGE, FMI, RATING):
    with open('fmi_database', 'a') as database:
        database.write("\n" + str(NAME) + "|" + str(FOREHEAD_WEIGHT) + "|" + str(FOREHEAD_VOLUME) + "|" + str(AGE) + "|" + str(FMI) + "|" + str(RATING))
        wait(2)
        print("Saved Sucessfully")
        database.close()
    
Calculate_FMI = lambda V, m: round(m/V**(2/3), 2)

print("Welcome to FMI (Forehead Mass Index)")
wait(2)
name = input("Enter Name: ")
wait(2)
V = float(input("Please enter the Volume of ur Forhead (m^3): "))
wait(1)
m = float(input("Enter the mass of ur forhead (kg): "))
wait(1)
a = float(input("How old r u? "))
wait(1)

FMI = Calculate_FMI(V, m)
HealthyLowerFMI = a/2 - 5
HealthyUpperFMI = a/2 + 5

print("Your FMI is: " + str(FMI))
wait(3)
Rating = ""
if FMI < a/2 - 5:
    Rating = "Underweight :["
    print("Ur forhead is " + Rating)
elif a/2 - 5<=FMI<= a/2 + 5:
    Rating = "Okay :]"
    print("Ur forhead is " + Rating)
elif FMI> a/2 + 5:
    Ratin = "NOT OKAY 0_0"
    print("Ur forhead is " + Rating)
    wait(2)
    print("U NEED MEDICAL HELP!")
    wait(2)
    print("Go to https://www.nhs.uk/")

wait(2)
print("The average FMI for someone ur age is between " + str(HealthyLowerFMI) + " to " + str(HealthyUpperFMI))
wait(3)
response = input("Would you like us to save ur data?")
if response.lower() == "yes":
    print("Saving FMI...")
    saveData(name, m, V, a, FMI, Rating)
else:
    print("Ur FMI has not been Saved/")
wait(5)