from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt,  QCoreApplication
from PyQt5.QtGui import QIcon
import sys
from design import Ui_weather_form
import requests as req

import time
import datetime

#----- {Создание приложения} -----
app = QtWidgets.QApplication(sys.argv)

#----- {Создание формы} ----
weather_form = QtWidgets.QWidget()
ui = Ui_weather_form()
ui.setupUi(weather_form)
weather_form.show()

#----- {Код всего приложения} ----

ui.text_weather_in_city.setText("Введите город выше")
ui.text_temp.hide()
ui.text_description.hide()
ui.text_temp_likes.hide()
ui.text_pressure.hide()
ui.text_humidity.hide()
ui.text_speed_wind.hide()
ui.text_direction_wind.hide()
ui.block_snow.hide()
ui.text_snow_hour.hide()
ui.text_snow_3_hour.hide()
ui.groupBox_2.hide()
ui.text_rain_hour.hide()
ui.text_rain_3_hour.hide()
ui.block_sunrise_and_sunset.hide()
ui.text_sunrise.hide()
ui.text_sunset.hide()

def pressedGet():
    city = ui.inputCity.text()

    response = req.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'q': city, 'lang': 'ru', 'units': 'metric', 'APPID': "9d0864cfefebb1ec3592e7379f7776af"})
    weather = response.json()

    if "message" in weather.keys():
        try:
            if weather["cod"] == "404":
                ui.text_weather_in_city.setText("Вы ввели неверный город")

            elif weather["cod"] == "400":
                ui.text_weather_in_city.setText("Вы не ввели город")

            elif weather["cod"] == "429":
                ui.text_weather_in_city.setText("Ошибка приложения")

            else:
                ui.text_weather_in_city.setText("Глобальная ошибка сервера")

            ui.text_temp.setText("--° C")
            ui.text_temp.show()
            ui.text_temp_likes.setText("По ощущениям --° C")
            ui.text_temp_likes.show()
            ui.text_description.setText("------------")
            ui.text_description.show()
            ui.text_pressure.setText("Атмосферное давление --- мм.рт.ст")
            ui.text_pressure.show()
            ui.text_humidity.setText("Влажность --- %")
            ui.text_humidity.show()
            ui.text_speed_wind.setText("Скорость ветра --- м/с")
            ui.text_speed_wind.show()
            ui.text_direction_wind.setText("Направление ветра ---")
            ui.text_direction_wind.show()
            ui.block_snow.show()
            ui.text_snow_hour.setText("----")
            ui.text_snow_hour.show()
            ui.text_snow_3_hour.setText("----")
            ui.text_snow_3_hour.show()
            ui.groupBox_2.show()
            ui.text_rain_hour.setText("----")
            ui.text_rain_hour.show()
            ui.text_rain_3_hour.setText("----")
            ui.text_rain_3_hour.show()
            ui.block_sunrise_and_sunset.show()
            ui.text_sunrise.setText("Восход в ----")
            ui.text_sunrise.show()
            ui.text_sunset.setText("Закат в ----")
            ui.text_sunset.show()

        except KeyError:
            ui.text_weather_in_city.setText("Ошибка приложения")
            ui.text_temp.hide()
            ui.text_description.hide()
            ui.text_temp_likes.hide()
            ui.text_pressure.hide()
            ui.text_humidity.hide()
            ui.text_speed_wind.hide()
            ui.text_direction_wind.hide()
            ui.block_snow.hide()
            ui.text_snow_hour.hide()
            ui.text_snow_3_hour.hide()
            ui.groupBox_2.hide()
            ui.text_rain_hour.hide()
            ui.text_rain_3_hour.hide()
            ui.block_sunrise_and_sunset.hide()
            ui.text_sunrise.hide()
            ui.text_sunset.hide()


    else:
        try:
            ui.text_weather_in_city.setText("Погода " + str(weather["name"]))
        except KeyError:
            ui.text_weather_in_city.setText("Погода неизвестна")
        finally:
            ui.text_weather_in_city.show()
        
        try:
            ui.text_temp.setText(str(weather["main"]["temp"]) + "° C")
        except KeyError:
            ui.text_temp.setText("--° C") 
        finally:
            ui.text_temp.show()  
        
        try:
            ui.text_temp_likes.setText("По ощущениям " + str(weather["main"]["feels_like"]) + "° C")
        except KeyError:
            ui.text_temp_likes.setText("По ощущениям --° C")
        finally:
            ui.text_temp_likes.show()
        
        try:
            ui.text_description.setText(weather["weather"][0]["description"])
        except KeyError:
            ui.text_description.setText("------------")
        finally:
            ui.text_description.show()
        
        try:
            ui.text_pressure.setText("Атмосферное давление " + str(round(weather["main"]["pressure"]*0.75)) + " мм.рт.ст")
        except KeyError:
            ui.text_pressure.setText("Атмосферное давление --- мм.рт.ст")
        finally:
            ui.text_pressure.show()
        
        try:
            ui.text_humidity.setText("Влажность " + str(weather["main"]["humidity"]) + " %")
        except KeyError:
            ui.text_humidity.setText("Влажность --- %")
        finally:
            ui.text_humidity.show()
        
        try:
            ui.text_speed_wind.setText("Скорость ветра " + str(weather["wind"]["speed"]) + " м/с")
        except KeyError:
            ui.text_speed_wind.setText("Скорость ветра --- м/с")
        finally:
            ui.text_speed_wind.show()
        
        try:
            ui.text_direction_wind.setText("Направление ветра " + degToCompass(weather["wind"]["speed"]))
        except KeyError:
            ui.text_direction_wind.setText("Направление ветра ---")
        finally:
            ui.text_direction_wind.show()

        try:
            ui.text_snow_hour.setText(str(weather["snow"]["1h"]) + "мм/ч")
        except KeyError:
            ui.text_snow_hour.setText("--- мм/ч")
        finally:
            ui.text_snow_hour.show()
            ui.block_snow.show()

        try:
            ui.text_snow_3_hour.setText(str(weather["snow"]["3h"]) + " мм/3ч")
        except KeyError:
            ui.text_snow_3_hour.setText("--- мм/3ч")
        finally:
            ui.text_snow_3_hour.show()
            ui.block_snow.show()


        try:
            ui.text_rain_hour.setText(str(weather["rain"]["1h"]) + "мм/ч")
        except KeyError:
            ui.text_rain_hour.setText("--- мм/ч")
        finally:
            ui.text_rain_hour.show()
            ui.groupBox_2.show()

        try:
            ui.text_rain_3_hour.setText(str(weather["rain"]["3h"]) + " мм/3ч")
        except KeyError:
            ui.text_rain_3_hour.setText("--- мм/3ч")
        finally:
            ui.text_rain_3_hour.show()
            ui.groupBox_2.show()


        val_sunrise = datetime.datetime.fromtimestamp(weather["sys"]["sunrise"])
        sunrise = val_sunrise.strftime('%H:%M')
        try:
            ui.text_sunrise.setText("Восход в " + sunrise)
        except KeyError:
            ui.text_sunrise.setText("Восход в ----")
        finally:
            ui.text_sunrise.show()
            ui.block_sunrise_and_sunset.show()

        val_sunset = datetime.datetime.fromtimestamp(weather["sys"]["sunset"])
        sunset = val_sunset.strftime('%H:%M')        
        try:
            ui.text_sunset.setText("Закат в " + sunset)
        except KeyError:
            ui.text_sunset.setText("Закат в ----")
        finally:
            ui.text_sunset.show()
            ui.block_sunrise_and_sunset.show()


        #ui.label_8.setText("Скорость ветра " + str(weather["wind"]["speed"]) + "м/с")

    
    

ui.buttonGet.clicked.connect( pressedGet )

ui.button_close.clicked.connect( QCoreApplication.instance().quit )

#ui.label.clicked.connect( pressedClose )

def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["С","ССВ","СВ","ВСВ","В","ВЮВ", "ЮВ", "ЮЮВ","Ю","ЮЮЗ","ЮЗ","ЗЮЗ","З","ЗСЗ","СЗ","ССЗ"]
    return str(arr[(val % 16)])

#----- {Запуск приложения} ----
sys.exit(app.exec_())

time.sleep(3)
pressedClose()
