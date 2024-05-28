import string

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username
    
    def __str__(self):
        """
        :return: a string that represents what is wrong with the username and specifies the character and its index. 
        :rtype: str
        """
        # get the illegal char in the username
        ilegal = [chr for chr in self._username if not(chr.isalpha() or chr.isdigit() or chr == "_")][0]
        return f'The username contains an illegal character "{ilegal}" at index {self._username.index(ilegal)}'

class UsernameTooShort (Exception):
    def __init__(self, username):
        self._username = username
    def __str__(self):
        return "The username is too short"

class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username
    def __str__(self):
        return "The username is too long"

# passwored exception classes
class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self._password = password
    def __str__(self):
        return "The password is missing a character"

# inherents of PasswordMissingCharacter
class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() +  " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() +  " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() +  " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() +  " (Special)"

class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password
    def __str__(self):
        return "TThe password is too short"

class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password
    def __str__(self):
        return "The password is too long"

def check_input(username, password):
    """
    function to check if the credentials a usern provided are ok according to the format,
    if the input is ok, it will print "OK", if not it will rais the appropriate Exception.

    :param username: the username
    :type username: str
    :param password: the password
    :type password: str
    """
    # checking validity of username
    # if the username contains characters other than letters, digits, or _
    if False in [chr.isalpha() or chr.isdigit() or chr == "_" for chr in username]:
        raise UsernameContainsIllegalCharacter(username)
    elif len(username) < 3:
        raise UsernameTooShort(username)
    elif len(username) > 16:
        raise UsernameTooLong(username)
    
    # checking validity of password
    if len(password) < 8:
        raise PasswordTooShort(username)
    if len(password) > 40:
        raise PasswordTooLong(username)
    
    # checking if all the types of characters are in the password
    big_letter = False
    small_letter = False
    digit = False
    punctuation = False
    
    for c in password:
        if c.isalpha() and c == c.upper():
            big_letter = True
        if c.isalpha() and c == c.lower():
            small_letter = True
        if c.isdigit():
            digit = True
        if c in string.punctuation:
            punctuation = True
    # if there was a False, meaning one of the conditions hasnt been met
    if not (big_letter and small_letter and digit and punctuation):
        # rais the apropriate exception, the exception from the list in the same index of the False condition
        index_of_error = [big_letter, small_letter, digit, punctuation].index(False)
        raise [PasswordMissingUppercase, PasswordMissingLowercase, PasswordMissingDigit, PasswordMissingSpecial][index_of_error](username)

    print("OK")

def main():
    # checks for different types of input
    try:
        check_input("1", "2")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("0123456789ABCDEFG", "2")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("A_a1.", "12345678")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("A_1", "2")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("A_1", "abcdefghijklmnop")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("A_1", "ABCDEFGHIJLKMNOP")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("A_1", "ABCDEFGhijklmnop")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("A_1", "4BCD3F6h1jk1mn0p")
    except Exception as e:
        print(f"{e}")

    try:
        check_input("A_1", "4BCD3F6.1jk1mn0p")
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()