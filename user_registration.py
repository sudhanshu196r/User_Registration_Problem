'''
    @Author: Sudhanshu Kumar
    @Date: 04-11-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-11-2024
    @Title : Enter valid first name

'''

import re
import logger

log = logger.logger_init('first_name')

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


def main():
    try:
        while True:
            f_name = input("Enter First name: ")
            result = check_firstname(f_name)
            if result:
                break
            else:
                log.info("Error! Invalid First name")
    except Exception as e:
        log.exception(f"Raised Exception: {e}")

if __name__=="__main__":
    main()


    