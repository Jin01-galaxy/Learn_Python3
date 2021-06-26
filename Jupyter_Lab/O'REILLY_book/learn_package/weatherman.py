from sources import daily, weekly

print('Daily forcast:', daily.forcast())
print('Weekly forcast:')
for number, outlook in enumerate(weekly.forcast(), 1):
  print(number, outlook)