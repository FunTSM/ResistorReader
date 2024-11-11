#this code was oringinally built to be used with GPIO buttons on a raspberry pi, so it is a bit janky to use standalone.
#if you are reading this and other versions are available, go check if they will fit your use case better than this one will.
#feel free to re-build this code to fit whatever you want it to.

import os
from decimal import Decimal, getcontext

getcontext().prec = 4

color1 = {0: ["none", 0],1: ["black", 0],2: ["brown", 1],3: ["red", 2], 4: ["orange", 3],5: ["yellow", 4],6: ["green", 5],7: ["blue", 6],8: ["violet", 7],9: ["grey", 8], 10: ["white", 9]}


color2 = {0: ["black", 1],1: ["brown", 10],2: ["red", 100], 3: ["orange", 1000],4: ["yellow", 10000],5: ["green", 100000],6: ["blue", 1000000],7: ["violet", 10000000],8: ["grey", 100000000], 9: ["white", 1000000000], 10: ["silver", 0.01], 11: ["gold", 0.1]}

color3 = {0: ["brown", 1],1: ["red", 2], 2: ["green", 0.5],3: ["blue", 0.25],4: ["violet", 0.1],5: ["grey", 0.05], 6: ["silver", 10], 7: ["gold", 5]}

color4 = {0: ["black", 0],1: ["brown", 1],2: ["red", 2], 3: ["orange", 3],4: ["yellow", 4],5: ["green", 5],6: ["blue", 6],7: ["violet", 7],8: ["grey", 8], 9: ["white", 9]}

firstPin = 0
secondPin = 0
thirdPin = 0
fourthPin = 0
fifthPin = 0


def adjust():
  global firstPin
  global secondPin
  global thirdPin
  global fourthPin
  global fifthPin
  global color1
  global color2
  global color3

  print(color1[firstPin][0], color4[secondPin][0], color4[thirdPin][0], color2[fourthPin][0], color3[fifthPin][0])
  
  choice = input("pin to adjust:")
  os.system('clear')
  try:
    choice = int(choice)
  except:
    choice = choice
  
  if choice == 1:
    firstPin = firstPin+1
    if firstPin == 10:
      firstPin = 0
  elif choice == 2:
    secondPin = secondPin+1
    if secondPin == 9:
      secondPin = 0
  elif choice == 3:
    thirdPin = thirdPin+1
    if thirdPin == 9:
      thirdPin = 0
  elif choice == 4:
    fourthPin = fourthPin+1
    if fourthPin == 12:
      fourthPin = 0
  elif choice == 5:
    fifthPin = fifthPin+1
    if fifthPin == 8:
      fifthPin = 0

  mult = color2[fourthPin][1]
  num = str(color1[firstPin][1]) + str(color4[secondPin][1]) + str(color4[thirdPin][1])
  num = int(num)
  
  ohmage = Decimal(num)* Decimal(mult)
  
  if ohmage >= 1000000000:
    ohms = "GΩ"
    div = Decimal(1000000000)
  elif ohmage >= 1000000:
    ohms = "MΩ"
    div = Decimal(1000000)
  elif ohmage >= 1000:
    ohms = "KΩ"
    div = Decimal(1000)
  elif ohmage < 1000:
    ohms = "Ω"
    div = Decimal(1)

  
  result = Decimal(ohmage) / div
  result = float(result)
  
  print(result, ohms,"±", str(color3[fifthPin][1]), "%" )
  
while True:
  adjust()
