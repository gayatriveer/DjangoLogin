import random
from faker import Faker
from datetime import datetime



fake=Faker('de_DE')

def createdummydata():
    username=fake.name()
    fname= fake.name()
    lname= fake.name()
    email= fake.ascii_email()
    phone= random.randint(1000000000,9999999999)
    lastlogin= datetime.now()
    lastlogout= datetime.now()



    return username,fname,lname,email,str(phone),lastlogin,lastlogout










