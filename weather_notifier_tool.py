import requests
import datetime as dt
from twilio.rest import Client

#Required Credentials for Twilio
account_sid = "[AccountSid]" #34-digit unique account sid provided by Twilio
auth_token = "[AuthToken]"    #34-digit unique auth token provided by Twilio
client = Client(account_sid, auth_token)


#Get local time and date using datetime module and datetime class with now() method
time_data = dt.datetime.now()

#Credentials for OpenWeather API Parameters
API_KEY = MY_API_KEY
MY_LAT =  MY_LAT
MY_LONG = MY_LONG

#User Specific Weather parameters for API request to OpenWeather
weather_parameters = {

    "lat": MY_LAT,
    "lon": MY_LONG, 
    "appid": API_KEY, #API_KEY provided by OpenWeather
    "cnt": ["3HourForecastCount"],  #e.g. cnt=4 gives 12-hour forecast since forecast is updated every 3 hours (4x3-hour forecast blocks) 

}
#OpenWeather endpoint without specified parameters, set to 3-hour 5-day forecast
OWE_URL = "https://api.openweathermap.org/data/2.5/forecast"
#gets response from OpenWeather with user specific parameters
response = requests.get(url=OWE_URL, params=weather_parameters)
#Store Weather JSON Forecast Data into OWE_data
OWE_data = response.json()

#weather condition flags
will_it_rain = False
will_it_snow = False

#weather condition hour list
rain_hour_list = []
other_weather_hour_list = []
snow_hour_list =[]
#weather condition amounts
rain_amounts = []
snow_amounts = []

rain_time_counter = 0
snow_time_counter = 0
other_weather_time_counter = 0


#loop through each 3-hour forecast in OWE Response 
for hours in OWE_data["list"]:
   #'weather' list of weather condition objects
   #tap into condition (first entry) of weather list, and check 'main category' e.g. Rain
    condition = hours["weather"][0]["main"]
    if condition == "Rain":
        will_it_rain = True
       
        #update rain flag since it will rain in at least one 3 hour interval
        
       
        #get rain amount 
        rain_amounts.append(hours["rain"]["3h"])
        #get time of rain fall
        rain_hour_list.append(hours["dt_txt"])
        rain_time_OWE = OWE_data["city"]["timezone"]
        
        #convert UTC time of weather conditions to local time
        rain_utc_dt = dt.datetime.strptime(rain_hour_list[rain_time_counter], "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)
        OWE_UTC_SECS = OWE_data["city"]["timezone"]
        rain_local_tz = dt.timezone(dt.timedelta(seconds=OWE_UTC_SECS))
        rain_local_dt = rain_utc_dt.astimezone(rain_local_tz)
        print(f"{will_it_rain} it will {hours["weather"][0]["main"]} {hours["rain"]["3h"]}mm at {rain_local_dt.strftime("%Y-%m-%d %I:%M:%S %p")}  ")
       

        #set up SMS Client and create message
    
        message = client.messages.create(
        messaging_service_sid="[MessageServiceSid]",
        body=f"Bring an ☔️! It will {hours["weather"][0]["main"]} " \
        f"({hours["rain"]["3h"]}mm) at {rain_local_dt.strftime("%Y-%m-%d %I:%M:%S %p")} 🌧️",
        to="[UserRecepientPhoneNumber]"
        )
        #increment to get to next rain time each time rain is expected
        rain_time_counter +=1

    #check other targeted weather condition: Snow by tapping into weather list
    elif condition == "Snow":
        #update weather flags
       
        will_it_snow = True
        #get snow time, and add to snow hour list
        snow_hour_list.append(hours["dt_txt"])
        snow_amounts.append(hours["snow"]["3h"])
        #convert UTC time of weather conditions to local time
        snow_utc_dt = dt.datetime.strptime(snow_hour_list[snow_time_counter], "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)
        OWE_UTC_SECS = OWE_data["city"]["timezone"]
        snow_local_tz = dt.timezone(dt.timedelta(seconds=OWE_UTC_SECS))
        snow_local_dt = snow_utc_dt.astimezone(snow_local_tz)
       
        print(f"{will_it_snow} it will {hours["weather"][0]["main"]} {hours["snow"]["3h"]}mm  at {snow_local_dt.strftime("%Y-%m-%d %I:%M:%S %p")} ")
      
        message = client.messages.create(
        messaging_service_sid="[MessageServiceSid]",
        body=f"❄️ Be careful! It will {hours["weather"][0]["main"]} " \
        f"({hours["snow"]["3h"]}mm) at {snow_local_dt.strftime("%Y-%m-%d %I:%M:%S %p")} ❄️",
        to="[UserRecepientPhoneNumber]"
        )
     
        snow_time_counter+=1
    #check for other possible weather conditions
    else:
  
        #convert UTC time of weather conditions to local time
        other_weather_hour_list.append(hours["dt_txt"])
        utc_dt = dt.datetime.strptime(other_weather_hour_list[other_weather_time_counter], "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)
        OWE_UTC_SECS = OWE_data["city"]["timezone"]
        local_tz = dt.timezone(dt.timedelta(seconds=OWE_UTC_SECS))
        local_dt = utc_dt.astimezone(local_tz)
      
        print(f"{will_it_rain} it will {hours["weather"][0]["main"]} at {local_dt.strftime("%Y-%m-%d %I:%M:%S %p")} ")
        
    
        other_weather_time_counter+=1

