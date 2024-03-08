# filter: para filtrar elementos de una lista y retorna un nuevo array
numbers = [1, 2, 3, 4, 5]
newNumbers = list(filter(lambda x : x % 2 == 0, numbers))
print(newNumbers)


''''''
matches = [
    {
        'homeTeam': 'Bolivia',
        'awayTeam': 'Uruguay',
        'homeTeamScore': 3,
        'awayTeamScore': 1,
        'homeTeamResult': 'win'
    },
    {
        'homeTeam': 'Brazil',
        'awayTeam': 'Mexico',
        'homeTeamScore': 1,
        'awayTeamScore': 1,
        'homeTeamResult': 'Draw'
    },
    {
        'homeTeam': 'Ecuador',
        'awayTeam': 'Venezuela',
        'homeTeamScore': 5,
        'awayTeamScore': 0,
        'homeTeamResult': 'win'
    },
]

print(len(matches))
newList = list(filter(lambda item : item['homeTeamResult'] == 'win', matches))
print(newList)
print(len(newList))