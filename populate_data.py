import os
from faker import Faker
from random import *
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','FVB_CRUD_operations.settings')
django.setup()

from testapp.models import Employee
fake=Faker()

def PhoneNumber():
    s=str(randint(6,9))
    for i in range(9):
        s=s+str(randint(0,9))
    return int(s)
 
def populate_data(n):
    
    for i in range(n):
        FENO=fake.random_int(1,999)
        FENAME=fake.name()
        FESAL=fake.random_int(35000,70000)
        FADDRESS=fake.city()
        Employee.objects.get_or_create(eno=FENO,ename=FENAME,esal=FESAL,eaddr=FADDRESS)

n=int(input('Enter the no of records to insert '))
populate_data(n)
print(n,'records inerted successfully')