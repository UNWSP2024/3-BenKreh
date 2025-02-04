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
