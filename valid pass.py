#rules of a strong password
'''At least 8 characters—the more characters, the better
A mixture of both uppercase and lowercase letters
A mixture of letters and numbers
Inclusion of at least one special character, e.g., ! @ # ? ]'''

def strongpass():
    print(f"Please input a password and I'll tell if you if it's a strong password")

    exclusions = ["!","@","#","?"]
    exclusionsflag = False
    possible = input()
    possible = [x for x in possible]

    for x in possible:
        if x in exclusions:
            exclusionsflag = True
            break

    if len(possible) <= 8:
        exclusionsflag = False

    if exclusionsflag == False:
        return "No your password is weak"

    upper = 0
    lower = 0

    for x in possible:
        if upper == lower and upper != 0 and lower != 0:
            print("hi")
            return f"Yes your password is strong"
        if x.islower():
            lower += 1
        if x.isupper():
            upper += 1

    return f"No your password is weak"

print(strongpass())

