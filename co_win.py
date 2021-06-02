import requests
import json
import smtplib
import pyautogui

arr=[]
while True:
    r=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=474003&date=03-06-2021')
    
    for i in r.json()['sessions']:
        if i['center_id']==571140:
            pass
        else:
            arr.append(i)
            print(i)
    try:
        a=str(arr[-1])

        if arr[-1]!=0:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("amn.j1998@gmail.com", "1AK@jha123")
  
            message ="Please wake up and register for vaccination "+a 
            s.sendmail("amn.j1998@gmail.com","amanjyo5318@gmail.com", message)
            print(a)
            s.quit()
            break

        else:
            pass
            print('Not Available')
            #print('Availability',arr[-5])
    except:
        print('cool')
        pass
    pyautogui.hotkey("ctrlleft","f5")
