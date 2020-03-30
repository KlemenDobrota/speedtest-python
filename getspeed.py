import speedtest
from datetime import datetime
from dateutil import tz

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

print("Timestamp: " + timestamp_date + " - " + timestamp_time)
print("Download: " + str(download) + " Mbit/s")
print("Upload  : " + str(upload) + " Mbit/s")
print("Ping    : " + str(ping) + " ms")
print("Test server: " + server_name + " (" + server_loc + ") - " + str(server_dist) + " km")
print("Testing from (my IP address): " + myip + " (" + isp +")")
