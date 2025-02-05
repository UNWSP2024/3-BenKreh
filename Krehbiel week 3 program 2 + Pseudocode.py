#Ben Krehbiel
#2/4/2025
#CYS3065 Systems of Analysis and Design

#Pseudocode for program 2, age identifier 


#Take an age that must be a number with no decimals
#If the age Is lower or equal to one tell them they are an infant
#If the age is above one but lower than 13 tell them they are a child
#If the age is equal to or above 13 but lower than 20 tell them they are teenagers.
#If the age is equal to or above 20 tell them they are an adult
#If the age is above or equal to 100 tell them they are lying, retry

#Ben Krehbiel
#02/04/2025
#CYS3065 Systems of Analysis and Design
#half way in the grave

age = int(input("input age here: "))

if age <=1:
    print("you are", age, "an infant")
elif 1 < age < 13:
    print("you are", age, "a child")
elif 13 <= age < 20:
    print("you are", age, "a teenager")
elif 20 <= age < 100:
    print("you are", age, "an adult")
elif age >= 100:
    print("you are lying, retry")
