import VanityClass
CRITERIA = ["Are the first two characters letters?",
            "Is the plate length a minimum of two and maximum of six characters?",
            "Are the digits at the end?",
            "Is the starting digit not a zero?",
            "No punctuation marks?"]
def main():
    plate = input("Plate: ").upper()
    vanity = VanityClass.VanityPlate(plate)
    print(vanity)
    print()
    check = True
    count = 0
    while check and count < len(CRITERIA):
        print(CRITERIA[count])
        if vanity.StartCriteria():
            print("Valid")
        else:
            print("Invalid")
            check = False
        count += 1
        print(CRITERIA[count])
        if vanity.PlateLength():
            print("Valid")
        else:
            print("Invalid")
            check = False
        count += 1
        print(CRITERIA[count])
        if vanity.PlateMiddle():
            print("Valid")
        else:
            print("Invalid")
            check = False
        count += 1
        print(CRITERIA[count])
        if vanity.PlateDigitStart():
            print("Valid")
        else:
            print("Invalid")
            check = False
        count += 1
        print(CRITERIA[count])
        if vanity.PlatePunctuation():
            print("Valid")
        else:
            print("Invalid")
            check = False
        count += 1
    if not check:
        print("Select new Characters")
main()