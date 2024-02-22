import random
opciones = {
    'piedra': {
        'piedra': 'empate',
        'papel': 'perdiste',
        'tijera': 'ganaste'
    },
    'papel': {
        'papel': 'empate',
        'tijera': 'perdiste',
        'piedra': 'ganaste',
    },
    'tijera': {
        'tijera': 'empate',
        'piedra': 'perdiste',
        'papel': 'ganaste'
    }
}

usuario_ganando = 0
computadora_ganando = 0
def rules_of_game(computer_option, opcion, usuario_ganando, computadora_ganando):
  if (opciones.get(opcion)):
    for j in opciones.keys():
      if (j == computer_option[0]):
        for k in opciones[j]:
          if k == opcion:
            print(opciones[j][opcion])
            if (opciones[j][opcion] == 'perdiste'): computadora_ganando += 1
            elif (opciones[j][opcion] == 'ganaste'): usuario_ganando += 1
  else:
    print("No es valido")
 

  return computadora_ganando, usuario_ganando


while True:
  computer_option = random.choices(list(opciones))
  opcion = input(
      'Digite una de las opciones: (piedra, papel, tijera): ').lower()
  computadora_ganando, usuario_ganando = rules_of_game(computer_option, opcion, usuario_ganando, computadora_ganando)
  print(computadora_ganando, usuario_ganando)
  if(computadora_ganando == 2 or usuario_ganando == 2):
    print(f'Resultado: \nResultado Computadora: {computadora_ganando}\n usuario: {usuario_ganando}')
    break
