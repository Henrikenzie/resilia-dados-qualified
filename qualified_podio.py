def podio_olimpico(x,y,z):
    # Implemente aqui a lógica da função
  resultpodio = ' '
  if(x<y<z):
    resultpodio = (f'1 - {x} minutos\n' 
                   f'2 - {y} minutos\n'
                   f'3 - {z} minutos\n')
    print(resultpodio)
    return resultpodio
  elif(x<z<y):
    resultpodio = (f'1 - {x} minutos\n'
                   f'2 - {z} minutos\n'
                   f'3 - {y} minutos\n')
    print(resultpodio)
    return resultpodio
  elif(y<z<x):
    resultpodio = (f'1 - {y} minutos\n'
                   f'2 - {z} minutos\n'
                   f'3 - {x} minutos\n')
    print(resultpodio)
    return resultpodio
  elif(y<x<z):
    resultpodio = (f'1 - {y} minutos\n'
                   f'2 - {x} minutos\n'
                   f'3 - {z} minutos\n')
    print(resultpodio)
    return resultpodio
  elif(z<y<x):
    resultpodio = (f'1 - {z} minutos\n'
                   f'2 - {y} minutos\n'
                   f'3 - {x} minutos\n')
    print(resultpodio)
    return resultpodio
  elif(z<x<y):
    resultpodio = (f'1 - {z} minutos\n'
                   f'2 - {x} minutos\n'
                   f'3 - {y} minutos\n')
    print(resultpodio)
    return resultpodio

podio_olimpico(1,2,3)