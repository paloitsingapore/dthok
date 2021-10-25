import csv
import json
import string
from random import choice
from string import *
import random
from faker import Faker
from datetime import datetime
from phone_gen import PhoneNumber

def flattenjson(b):
    val = {}
    if isinstance(b, list):
        b = b[0]
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flattenjson(b[i])
            for j in get.keys():
                val[j] = get[j]
        else:
            val[i] = b[i]

    return val


def datagenerator(data_file, records):
    with open(data_file, 'rb') as f:
        data = json.load(f)
        datadict = flattenjson(data)
        columns = ['id']
        columns = columns.__add__(list(datadict.keys()))
        output = []
        for i in range(records):
            row = []
            for x in columns:
                if x == 'id':
                    val = i+1
                else:
                    n = datadict[x].split("|")
                    if (len(n) == 2):
                        n.append(None)
                    val = getFakerDetails(n[2], n[0], n[1])
                # elif "alphabet" in datadict[x]:
                #     n = datadict[x].split("|")
                #     val = "".join(choice(ascii_lowercase) for i in range(int(n[1])))
                # elif "numeric" in datadict[x]:
                #     n = datadict[x].split("|")
                #     val = "".join(choice(digits) for i in range(int(n[1])))
                # elif "alphanum" in datadict[x]:
                #     n = datadict[x].split("|")
                #     source = string.digits + string.ascii_letters
                #     val = ''.join((random.choice(source) for i in range(int(n[1]))))
                row.append(val)
            output.append(row)

    return output, columns

def jsonGenerator(obj, reqdict):
    #fake = Faker()
    if isinstance(obj, (dict,list)):
        if isinstance(obj, list):
            obj = obj[0]
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                reqdict[k] = jsonGenerator(v, {})
            else:
                n = v.split("|")
                if(len(n)==2):
                    n.append(None)
                reqdict[k] = getFakerDetails(n[2], n[0], n[1])
    return reqdict

def getFakerDetails(type,dataType,length):
    fake = Faker()
    value=''
    if dataType == 'alphabet':
            while True:
                if type == 'firstName':
                    value = fake.first_name()
                    #if len(value) < int(length):
                    break
                elif type == 'lastName':
                    value = fake.last_name()
                    #if len(value) < int(length):
                    break
                elif type == 'streetName':
                    value = fake.street_name()
                    #if len(value) < int(length):
                    break
                elif type == 'country':
                    value = fake.country()
                    break
                elif type == 'company':
                    value = fake.company()
                    break
                elif type == 'city':
                    value = fake.city()
                    break
                elif type == 'title':
                    value = fake.prefix()
                    break
                else:
                    value = "".join(choice(ascii_lowercase) for i in range(int(length)))
                    break
    elif dataType == 'numeric':
        while True:
            if type == 'postcode':
                value = fake.postcode()
               # if len(value) < int(length):
                break
            else:
                value = "".join(choice(digits) for i in range(int(length)))
                break
    elif dataType == 'alphanum':
        while True:
            if type == 'streetName':
                value = fake.street_address()
                #if len(value) < int(length):
                break
            elif type == 'email':
                value = fake.email()
                break
            elif type == 'accountNumber':
                if length == "NONE":
                    value = fake.bban()
                else:
                    value = fake.iban()
                break
            else:
                source = string.digits + string.ascii_letters
                value = ''.join((random.choice(source) for i in range(int(length))))
                break
    elif dataType == 'date_of_birth':
        age = length.split(",")
        minage = age[0].split("=")
        maxage = age[1].split("=")
        while True:
            value = fake.date_of_birth(minimum_age=int(minage[1]), maximum_age=int(maxage[1]))
            value = value.strftime(type)
            break
    elif dataType == 'date':
        if(length == 'NONE'):
            value = fake.date_between()
            value = value.strftime(type)
        else:
            date = length.split(",")
            startDate = datetime.strptime(date[0].split("=")[1], '%Y%m%d')
            endDate = datetime.strptime(date[1].split("=")[1], '%Y%m%d')
            value = fake.date_between(start_date=startDate,end_date=endDate)
            value = value.strftime(type)
    elif dataType == 'choices':
        length =tuple(eval(length))
        value = random.choice(length)
    elif dataType == 'code':
        value = fake.numerify(text=type)
    elif dataType == 'boolean':
        value = fake.pybool()
    elif dataType == 'PhoneNumber':
        phonenum = PhoneNumber(type)
        value = phonenum.get_number()
    elif dataType == 'constant':
        value = length
    return value

#n[2], n[0], n[1]
#type,dataType,length