import utils

keys, values = utils.getPopulation()
print(keys, values)

data = [
    {
        'country': 'Colombia',
        'population': 300
    },
    {
        'country': 'Bolivia',
        'population': 500
    }
]

res = utils.populationByCountry(data, 'Colombia')
print(res)