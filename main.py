import requests
from datetime import datetime



MY_LAT = 21.027763
MY_LNG = 105.834160
#tọa độ Hà Nội

parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatter": 0,
    #chuyển sang hệ 12h. nếu dể mặc định là 1 là hệ 24h
}
#cung cấp input mới có thể dùng API



response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split( )[0].split(":")[0])
print(sunset.split( )[0].split(":")[0])
#cắt chỉ lấy phần giờ 
#lấy thành phần 0 trong list khi split lần 1 và tiếp tục split tiếp theo dấu :

time_now = datetime.now()
print(time_now.hour)