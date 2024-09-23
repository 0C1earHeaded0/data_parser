import pandas as pn
import requests as req

pages = req.get('https://rickandmortyapi.com/api/character').json()['info']['pages']
frames = []

for i in range(1, pages+1):
    temp = pn.DataFrame(req.get(f'https://rickandmortyapi.com/api/character/?page={i}').json()['results'])
    tempOrigin = pn.DataFrame([origin['origin']['name'] for origin in req.get(f'https://rickandmortyapi.com/api/character/?page={i}').json()['results']])
    tempLocation = pn.DataFrame([location['location']['name'] for location in req.get(f'https://rickandmortyapi.com/api/character/?page={i}').json()['results']])
    temp.insert(len(temp.columns), "origin_name", tempOrigin)
    temp.insert(len(temp.columns), "location_name", tempLocation)
    temp = temp.drop('origin', axis=1).drop('location', axis=1).drop('episode', axis=1)
    frames.append(temp)
    print(str(round((len(frames)/pages)*100)) + '%')

df = pn.concat(frames)
df.to_csv('char.csv', index=False)

# temp = pn.DataFrame(req.get(f'https://rickandmortyapi.com/api/character/?page={1}').json()['results'])
# tempOrigin = pn.DataFrame([origin['origin']['name'] for origin in req.get(f'https://rickandmortyapi.com/api/character/?page={1}').json()['results']])
# tempLocation = pn.DataFrame([location['location']['name'] for location in req.get(f'https://rickandmortyapi.com/api/character/?page={1}').json()['results']])

# temp.insert(len(temp.columns), "origin_name", tempOrigin)
# temp.insert(len(temp.columns), "location_name", tempLocation)

# print(temp)

# pn.concat(frames).to_csv('char.csv', index=False, sep=';')

