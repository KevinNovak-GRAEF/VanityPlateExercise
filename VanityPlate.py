import VanityClass
def main():
    criteria = ["Are the first two characters letters?",
            "Is the plate length a minimum of two and maximum of six characters?",
            "Are the digits (if any) at the end?",
            "Is the starting digit not a zero?",
            "No punctuation marks?"]

    plate = input("Plate: ").upper()
    plateLogo = input("Enter your choice of logo: ")
    plateCollector = input('If and old vehicle, enter "Collector": ')
    print()
    vanity = VanityClass.VanityPlate(plate,plateLogo,plateCollector)
    check = True
    count = 0
    while count < len(criteria):
        print(criteria[count])
        if vanity.StartCriteria():
            print("Valid")
        else:
            print("Invalid")
            check = False
            break
        count += 1
        print(criteria[count])
        if vanity.PlateLength():
            print("Valid")
        else:
            print("Invalid")
            check = False
            break
        count += 1
        print(criteria[count])
        if vanity.PlateMiddle():
            print("Valid")
        else:
            print("Invalid")
            check = False
            break
        count += 1
        print(criteria[count])
        if vanity.PlateDigitStart():
            print("Valid")
        else:
            print("Invalid")
            check = False
            break
        count += 1
        print(criteria[count])
        if vanity.PlatePunctuation():
            print("Valid")
        else:
            print("Invalid")
            check = False
        count += 1
    if check:
        print(f"Congratulations, your proposed plate {vanity.get_plate()} meets the criteria")
    else:
        print("Select new Characters")
    print()
    print("Other plate information:")
    print(vanity.get_logo())
    print(vanity.get_collector())

main()