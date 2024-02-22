import matplotlib.pyplot as plt 
def generate_pie_chart():
  labels = ['A','B','C']
  values = [200,34,120]
  fig, ax = plt.subplots()
  ax.pie(x=values, labels=labels)
  plt.savefig('image.png')
  plt.close()

generate_pie_chart()