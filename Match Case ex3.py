#MatchCaseEx3.py
wkd=input("Enter week name:")
match(wkd):
    case "MONDAY":
        print("{} is Working Day:".format(wkd))
    case "TUESDAY":
        print("{} is Working Day:".format(wkd))
    case "WEDNESDAY":
        print("{} is Working Day:".format(wkd))
    case "THURSDAY":
        print("{} is Working Day:".format(wkd))
    case "FRIDAY":
        print("{} is Working Day:".format(wkd))
    case "SATURDAY":
        print("{} is Week End---UGA:".format(wkd))
    case "SUNDAY":
        print("{} is HoliDay".format(wkd))
    case _:
        print("{} is not a week day".format(wkd))