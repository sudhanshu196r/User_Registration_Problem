'''
    @Author: Sudhanshu Kumar
    @Date: 04-11-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-11-2024
    @Title : User Registration problem

'''

import re
import logger

log = logger.logger_init('user_registration')

def check_firstname(f_name):
    """
    Description:
        This function checks if user entered valid first name
    Parameter:
        f_name: the name to be checked
    Returns:
        None
    """

    pattern = r'^[A-Z][a-z]{2,}$'
    return bool(re.match(pattern, f_name))


def check_lastname(l_name):
    """
    Description:
        This function checks if user entered valid last name
    Parameter:
        l_name: the name to be checked
    Returns:
        None
    """

    pattern = r'^[A-Z][a-z]{2,}$'
    return bool(re.match(pattern, l_name))


def check_email(email):
    """
    Description:
        This function checks if user entered valid email
    Parameter:
        email: the email to be checked
    Returns:
        None
    """

    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@([a-zA-Z0-9]+\.)[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?'
    return bool(re.match(pattern, email))



def main():
    try:
        while True:
            f_name = input("Enter First name: ")
            result = check_firstname(f_name)
            if result:
                break
            else:
                log.error("Error! Invalid First name")
    except Exception as e:
        log.exception(f"Raised Exception: {e}")

    try:
        while True:
            l_name = input("Enter last name: ")
            result = check_lastname(l_name)
            if result:
                break
            else:
                log.error("Error! Invalid last name")
    except Exception as e:
        log.exception(f"Raised Exception: {e}")

    try:
        while True:
            email = input("Enter email: ")
            result = check_email(email)
            if result:
                break
            else:
                log.error("Error! Invalid email")
    except Exception as e:
        log.exception(f"Raised Exception: {e}")


if __name__=="__main__":
    main()



    