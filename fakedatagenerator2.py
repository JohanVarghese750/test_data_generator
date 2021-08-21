import random
import csv
import configparser
from mimesis import Datetime

d=Datetime()
config = configparser.ConfigParser()
config.read('config.ini')
prop = []

name = []
coldata = []
num = input("enter the number of records to be printed")

prop = config.sections()
#print(prop)


def datatyp(type1, lower_limit, upper_limit):
    if type1 == 'integer':
      #  print(type(lower_limit),type(upper_limit))
        x = random.randint(int(lower_limit), int(upper_limit))
      #  print(type(x))
        return str(x)
    elif type1 == 'float':
        x = random.uniform(float(lower_limit), float(upper_limit))
     #   print(type(x))
        return str(x)
    elif type1 == 'date':
        x = d.datetime(int(lower_limit),int(upper_limit))
      #  print(type(x))
        return str(x)
def datatyp1(range):
        x=datatyp(config[j]['range'])
        x.split(",")
        print(x)


with open('/readfromconfig.csv', "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in prop:
        name.append(config[i]['name'])

    writer.writerow(name)

    for i in range(0, int(num)):
        str1=[]
        for j in prop:
            #print(str(datatyp(config[j]['datatype'],config[j]['lower_limit'],config[j]['upper_limit'])))
            if config[j]['datatype'] == 'int' or config[j]['datatype'] == 'float' or config[j]['datatype'] == 'date' :
                str1.append(str(datatyp(config[j]['datatype'],config[j]['lower_limit'],config[j]['upper_limit'])))
            elif config[j]['datatype'] == 'enum' :
                str1.append(str(datatyp(config[j]['range'])))




        writer.writerow(str1)
