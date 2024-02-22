import csv
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
def run(path, pais):
  df = pd.read_csv('world_population.csv')
  pais_bd = df[df['Country/Territory'] == pais.capitalize()].reset_index()

  if(len(pais_bd) > 0):
    pais_bd = pais_bd[['2022 Population','2020 Population', '2015 Population', '2010 Population']].T.reset_index()
    plt.title(pais.capitalize())
    plt.bar(x=pais_bd['index'], height=pais_bd[0])
  else:
    print("Gualá")


if __name__ == '__main__':
  pais = input('¿Qué país desea ver poblacionalmente? => ')
  run('./world_population.csv', pais=pais)