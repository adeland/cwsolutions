import string
def alphanumeric(password):
    count = 0
    nums = ["0", "1" , "2", "3", "4" , "5" , "6" , "7" , "8" , "9"]
    letter1 = list(string.ascii_lowercase)
    letter = list(string.ascii_uppercase)
    all = nums + letter1 + letter
    password = list(password)
    if password == []:
        return False
    for i in password:
        if i not in all:
            count += 1
    if count != 0:
        return False
    else:
        return True
