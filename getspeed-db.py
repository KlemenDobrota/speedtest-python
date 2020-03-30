import speedtest
import pymongo
from pymongo import MongoClient
from datetime import datetime
from dateutil import tz

# insert in string your username and password for MongoDB Atlas account and copy link from you account
# check manual Connect to Your Cluster: https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/
cluster = MongoClient("mongodb+srv://user:password@cluster.mongodb.net")
# DB name
db = cluster["speeddb"]
# Collection name
collection = db["speedcol"]

date_now = datetime.now()

# get speed data
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
results_dict = s.results.dict()
download = round(results_dict["download"]/1000000, 2)
upload = round(results_dict["upload"]/1000000, 2)
ping = round(results_dict["ping"], 2)
server_name = results_dict["server"]["sponsor"]
server_loc = results_dict["server"]["name"]
server_dist = round(results_dict["server"]["d"], 2)
myip = results_dict["client"]["ip"]
isp = results_dict["client"]["isp"]

timestamp_date = date_now.astimezone(tz.tzlocal()).strftime("%d.%m.%Y")
timestamp_time = date_now.astimezone(tz.tzlocal()).strftime("%H:%M:%S")

# write speed data to post and write post to collection - customized data
post = {"timestamp_date": timestamp_date, "timestamp_time": timestamp_time, "myip": myip, "isp": isp, "server_name": server_name, "server_loc": server_loc, "server_dist": server_dist, "ping": ping, "download": download, "upload": upload}
collection.insert_one(post)

# write all the data from speedtest to collection
#collection.insert_one(results_dict)

