import pandas as pd
import matplotlib.pyplot as plt
from utils import obtenerPaises
from graphic import generate_pie_chart
def init(path):
  df = pd.read_csv(path)
  df['Continent'].replace(['North America', 'South America'], 'America', inplace=True)
  df = df.groupby('Continent')['World Population Percentage'].sum().reset_index()
  plt.pie(x=df['World Population Percentage'], labels=df['Continent'], autopct='%0.f%%')
  plt.savefig('grafico_pie.png')

if __name__ == '__main__':
  init('world_population.csv')