'''
    @Author: Sudhanshu Kumar
    @Date: 04-11-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-11-2024
    @Title : File to test input details

'''

import pytest
import logger
import user_registration

log = logger.logger_init('test_user_registration.py')

def test_check_firstname():
    assert user_registration.check_firstname('Sudhanshu')
    assert not user_registration.check_firstname('sam')

def test_check_lastname():
    assert user_registration.check_lastname('Kumar')
    assert not user_registration.check_lastname('kumar')

def main():
    test_check_firstname()
    test_check_lastname()

if __name__=="__main__":
    main()