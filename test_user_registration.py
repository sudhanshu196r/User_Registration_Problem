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

def test_check_email():
    assert user_registration.check_email('abc+100@gmail.com')
    assert user_registration.check_email('abc@yahoo.com')
    assert user_registration.check_email('abc-100@yahoo.com')
    assert user_registration.check_email('abc.100@yahoo.com')
    assert user_registration.check_email('abc.100@yahoo.com')
    assert user_registration.check_email('abc111@abc.com')
    assert user_registration.check_email('abc111@abc.net')
    assert user_registration.check_email('abc.100@abc.com.au')
    assert user_registration.check_email('abc@1.com')
    assert user_registration.check_email('abc@gmail.com.com')
    assert not user_registration.check_lastname(' abc')
    assert not user_registration.check_lastname('abc@.com.my')
    assert not user_registration.check_lastname('abc123@gmail.a')
    assert not user_registration.check_lastname('abc123@.com')
    assert not user_registration.check_lastname('abc123@.com')
    assert not user_registration.check_lastname('abc123@.com.com')
    assert not user_registration.check_lastname('.abc@abc.com')
    assert not user_registration.check_lastname('abc()*@gmail.com')
    assert not user_registration.check_lastname('abc@%*.com')
    assert not user_registration.check_lastname('abc..2002@gmail.com')
    assert not user_registration.check_lastname('abc@abc@gmail.com')
    assert not user_registration.check_lastname('abc@gmail.com.1a')
    assert not user_registration.check_lastname('abc@gmail.com.aa.au')

def test_check_mobileno():
    assert user_registration.check_mobileno('91 3838746267')
    assert not user_registration.check_mobileno('392 83992')

def test_check_password():
    assert user_registration.check_password('Abcd@1sd')
    assert not user_registration.check_mobileno('jdjdj')

def main():
    test_check_firstname()
    test_check_lastname()
    test_check_email()
    test_check_mobileno()

if __name__=="__main__":
    main()
    