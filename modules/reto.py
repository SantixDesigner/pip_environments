import csv
from utils import balance, generate_bar_chart
def run(path, pais):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    dict = {}

    for i in reader:
      if i[2] == pais.capitalize():
        dict = {key:value for (key,value) in zip(header, i)}
    if(dict):
      dict = balance(dict)
      labels = [key.replace('Population', '') for key in dict.keys()]
      values = [values for values in dict.values()]
      generate_bar_chart(labels, values)
    else:
      print("No se encuentra el pais")


if __name__ == '__main__':
  pais = input('¿Qué país desea ver poblacionalmente? => ')
  run('./world_population.csv', pais=pais)