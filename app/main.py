import utils

def run(): ##con esta funcion podemos evitar que ejecute todo el archivo al hacer una importacion de main desde otro lado
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

otherData = [
    {
        'country': 'Colombia',
        'population': 300
    },
    {
        'country': 'Bolivia',
        'population': 500
    }
]

if __name__ == '__main__':
    run()