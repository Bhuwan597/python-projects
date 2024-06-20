import pyautogui
import time
time.sleep(3)
import datetime,os

for i in range(1,1001):
    pyautogui.typewrite(f'Ankush')
    pyautogui.press('enter',interval=1)
    time.sleep

# day,hour,min = input('day/hour/min : ').split('/')
# day_from_now = int(day) - int(datetime.datetime.now().day)

# d = int(day_from_now)+ (int(hour)-int(datetime.datetime.now().hour))/24 + (int(min) - int(datetime.datetime.now().strftime('%M')))/(24*60)
# alarm = datetime.timedelta(days=d)
# full_time = datetime.datetime.now() + alarm
# compare_alarm_time = full_time.strftime('%d/%H/%M')
# while True:
#     minute_left = (full_time.timestamp() - datetime.datetime.now().timestamp())//60
#     if str(compare_alarm_time) == datetime.datetime.now().strftime('%d/%H/%M'):
#         music_dir = "D:\Songs"
#         songs = os.listdir(music_dir)
#         os.startfile(os.path.join(music_dir,songs[0]))
#         break
#     else:
#         print(f'time left: {int(minute_left)} minutes')
#         time.sleep(60 - int(datetime.datetime.now().strftime('%S')))


# import winsound
# # milliseconds
# count = 0
# while True:
#     count +=1
#     if count == 5:
#         break
#     time.sleep(0.4)
#     winsound.Beep(600, 1500)

# import playsound
# playsound.playsound('alarm.wav', True)

# # print(datetime.datetime.now().strftime('%H:%M %p'))
# import time
# from yaspin import yaspin

# # Context manager:
# with yaspin():
#     time.sleep(1)  # time consuming code

# # Function decorator:
# @yaspin(text="Loading...")
# def some_operations():
#     time.sleep(1)  # time consuming code

# some_operations()