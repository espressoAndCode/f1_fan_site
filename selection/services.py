# import requests

# F1PATH='localhost:8080/'

# def get_data(year):



# def get_data(year):
#   data = {
#     'seasonData': None,
#     'raceData': None
#   }
#   races = []

#   url = F1PATH + 'races?year=' + year
#   r = requests.get( url).json()
#   seasonData = r['MRData']['RaceTable']
#   data['seasonData'] = seasonData
#   print ("Sanity check - ",seasonData)

#   numraces = len(seasonData['Races'])
#   for idx in range(numraces):
#     print("race # - ", idx)
#     url = F1PATH + year +'/' + str(idx + 1) + '/results.json'
#     r = requests.get( url).json()
#     raceData = r['MRData']['RaceTable']['Races'][0]['Results']
#     races.append(raceData)
#     data['raceData'] = races

#   return data
