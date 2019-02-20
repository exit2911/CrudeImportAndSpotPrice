import pandas as pd
from urllib import request
from pandas.io.json import json_normalize
import csv
import json

locu_api = '108274707d17c603dec0b94c1e4f78f1' # api key here



api_key = locu_api

url = "http://api.eia.gov/series/?api_key=" + locu_api + "&series_id=PET_IMPORTS.WORLD-US-LSW.M"

json_obj = request.urlopen(url)
data = json.load(json_obj)

df = pd.DataFrame.from_dict(json_normalize(data),orient = 'columns')

df_list = data['series'] #get the crude import data using the key series

#copy and paste the import data as a list

import_list = [['201811', 10134],
   ['201810', 11202],
   ['201809', 8256],
   ['201808', 14764],
   ['201807', 12434],
   ['201806', 19621],
   ['201805', 13030],
   ['201804', 15564],
   ['201803', 15770],
   ['201802', 15334],
   ['201801', 17402],
   ['201712', 13294],
   ['201711', 16812],
   ['201710', 22312],
   ['201709', 14778],
   ['201708', 25461],
   ['201707', 16918],
   ['201706', 21047],
   ['201705', 18670],
   ['201704', 13582],
   ['201703', 14018],
   ['201702', 11437],
   ['201701', 19523],
   ['201612', 14968],
   ['201611', 16350],
   ['201610', 17003],
   ['201609', 15695],
   ['201608', 16196],
   ['201607', 18173],
   ['201606', 14612],
   ['201605', 13335],
   ['201604', 14423],
   ['201603', 14665],
   ['201602', 13887],
   ['201601', 7503],
   ['201512', 9593],
   ['201511', 8340],
   ['201510', 11763],
   ['201509', 8192],
   ['201508', 10314],
   ['201507', 11770],
   ['201506', 8806],
   ['201505', 9754],
   ['201504', 7986],
   ['201503', 9915],
   ['201502', 8653],
   ['201501', 8453],
   ['201412', 10213],
   ['201411', 8830],
   ['201410', 12204],
   ['201409', 8092],
   ['201408', 6920],
   ['201407', 12875],
   ['201406', 13824],
   ['201405', 12639],
   ['201404', 12469],
   ['201403', 11467],
   ['201402', 6964],
   ['201401', 11139],
   ['201312', 15407],
   ['201311', 13539],
   ['201310', 13502],
   ['201309', 19124],
   ['201308', 19114],
   ['201307', 23207],
   ['201306', 21028],
   ['201305', 22644],
   ['201304', 19459],
   ['201303', 16297],
   ['201302', 14140],
   ['201301', 18684],
   ['201212', 20293],
   ['201211', 18910],
   ['201210', 21442],
   ['201209', 23130],
   ['201208', 29920],
   ['201207', 25251],
   ['201206', 30805],
   ['201205', 26269],
   ['201204', 26724],
   ['201203', 29605],
   ['201202', 24163],
   ['201201', 24809],
   ['201112', 25853],
   ['201111', 29494],
   ['201110', 29218],
   ['201109', 29464],
   ['201108', 33447],
   ['201107', 34293],
   ['201106', 34401],
   ['201105', 44490],
   ['201104', 31576],
   ['201103', 42950],
   ['201102', 29823],
   ['201101', 48640],
   ['201012', 41904],
   ['201011', 40672],
   ['201010', 43143],
   ['201009', 51937],
   ['201008', 54700],
   ['201007', 47734],
   ['201006', 51797],
   ['201005', 49882],
   ['201004', 52170],
   ['201003', 52394],
   ['201002', 50896],
   ['201001', 54755],
   ['200912', 53770],
   ['200911', 51103],
   ['200910', 57255],
   ['200909', 53527],
   ['200908', 53014],
   ['200907', 44480],
   ['200906', 46781],
   ['200905', 38445],
   ['200904', 50660],
   ['200903', 46216],
   ['200902', 31246],
   ['200901', 44580]]


#write the list to a csv file


with open("import.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(import_list)
    
#clean the csv file using text to column, and replace feature
    
#import the csv file as dataframe for analysis
    
import_data = pd.read_csv('/Users/VyHo/Desktop/new.csv',names = ['period','unit'])

# the current order of periods is most recent to least recent. must sort

sorted_data = import_data.sort_values('period', ascending = True)

sorted_data['unit'].plot.bar(figsize=(20,18),x = sorted_data['period'], y = import_data['unit'])

sorted_data.describe()

#find the beginning & ending periods

sorted_data.head() # starts 01.2009
sorted_data.tail() # ends   11.2018


#load 	Europe_Brent_Spot_Price_FOB.csv (source eia.gov)

   
spot_price = pd.read_csv('/Users/VyHo/Desktop/Europe_Brent_Spot_Price_FOB.csv',names = ['period','price'])

# filter prices from periods that match import periods
#weight > 70 and weight < 74

spot_price.filter(spot_price['period'] < 1/1/2009) #date format is M/D/YYYY

# making sure date data types have the desired format

