import csv
import matplotlib.pyplot as plt
from utils import obtenerPaises
from graphic import generate_pie_chart
def init(path):
    continents = [
        {
            'Continente': 'Europe',
            'Poblacion Mundial': 0
        },
        {
            'Continente': 'Africa',
            'Poblacion Mundial': 0
        },
        {
            'Continente': 'America',
            'Poblacion Mundial': 0
        },
        {
            'Continente': 'Oceania',
            'Poblacion Mundial': 0
        },
        {
            'Continente': 'Asia',
            'Poblacion Mundial': 0
        }
    ]
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        listaPaises = []
        for row in reader:
            data = dict(zip(header, row))
            listaPaises.append(obtenerPaises(data))

        for i in listaPaises:
          for j in continents:
            i['Continente'] = i['Continente'].replace('North ','')
            i['Continente'] = i['Continente'].replace('South ','')
            if(i['Continente'] == j['Continente']):
                j['Poblacion Mundial'] += i['Poblacion Mundial']
        
        labels = [values['Continente'] for values in continents]
        values = [values['Poblacion Mundial'] for values in continents]
        generate_pie_chart(labels, values)

if __name__ == '__main__':
  init('world_population.csv')