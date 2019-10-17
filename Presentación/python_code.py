import serial 
import time

import requests as req

device = 'COM6' #this will have to be changed to the serial port you are using
try:
  print ("Trying...",device)
  arduino = serial.Serial(device, 9600) 
except: 
  print ("Failed to connect on",device)
while True:
    time.sleep(1)
    data=arduino.readline()
    aux = data.split()
    id_conductor = str(aux[0]).translate({ord(i): None for i in "b'"})
    
    url = "http://157.245.175.97/api/Conductor/"+id_conductor+"/get_route"
    headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY5OWY2MWZkOGE2MmEyNjE2YTQ0YzU0ZmQ1OWI0YjYwZDY2YTIzYTU0NTU0NjQzZTI0NTYyMDEzZTQ4OGZjNGE5Nzk0OGI1MDlmZWYyNGY0In0.eyJhdWQiOiIxIiwianRpIjoiZjk5ZjYxZmQ4YTYyYTI2MTZhNDRjNTRmZDU5YjRiNjBkNjZhMjNhNTQ1NTQ2NDNlMjQ1NjIwMTNlNDg4ZmM0YTk3OTQ4YjUwOWZlZjI0ZjQiLCJpYXQiOjE1NzEyNzI5MDIsIm5iZiI6MTU3MTI3MjkwMiwiZXhwIjoxNjAyODk1MzAyLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.dNN5qN5HtRFm41cTgiziUDQMKmGm43v29kMMhE1H5B1DzTDAuAZAHxoUlnY-Mq7OGQRX0UaI0uzT0p5z6hvp1914wiiDsKOHUy_Mu8SC0kV6qNivKH1b-f4Q0WVZdM1TqJjF3m5KaseqQ6vlDbh6l-Ht0Fx_SqDkbi9KQMtrf29dhjNktA_IL9GkoK0mivjYP4gzVw8nTp0nhDbyFQ6JUMATToErDzImg377VExuRvhse8RVgS1i-zLpmiOW4ERU29cNEhRD_sKifhkiS4TnO-G4U9JbduR10ibReWpxux0aoDD3lIr5PS7u-1z8w1eREeQ5spXye07WiEjsagHtzN5IADBJP5zjnd3cckbyacKsthob5spJ-IrPZiUVZOi8F7Uoshc_2SwjnN6ki0CVBZle_9O7saawJJ_16_ebAsGL0L-jGuTOPY2M21VwxvxxnoWLMWTTPo7XGZyW5X8L3JoUnY77Q0pnsv4Rc1S9IN1iBEcZUDyh8d1vd6uD5kHfoZQG4ykgkSHGiQsey-GWIK1lCpmY5wEaAF_ZAzUzuhx2IP2d3pV8Hi9gcCOWBQ6BfxtIPXQfmhdYc9iLqtiUqAI7YyEPGtERlsKCp7B2OU_5WtMVjKmh01FExNvKTcSeuJEEJFHT6-M19ROhRb1n2mEEvnQNONMT5hfMN0PZUF8'}

    resp = req.get(url, headers=headers)
    print(resp.text)
