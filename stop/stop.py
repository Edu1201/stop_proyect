import string, random
import time
import pandas as pd

print("BIENVENIDX")
next = input("¿Estás listx para el juego? (Si/No): ")

if next.capitalize() == "No":
  print (":c... entiendo, ¡nos vemos la proxima!")
  
if next.capitalize () == "Si":
  
  print ()
  print ('''Ahora te explico como funciona nuestro juego: 
  
1.De manera aleatoria te 
asignaremos una letra del abecedario, con esta deberas escribir una palabra de acuerdo con la categoria asignada.

2.Debes escribir una palabra con la letra dada.

3.Por cada acierto que tengas ganas 50 puntos, así mismo, por cada error que cometas perderás 25 puntos.

4.Puedes escoger las rondas que desees, para hacer la mayor cantidad de puntos, la mayor cantidad de puntos por ronda son 250.''')

  print()
  next2 = input("Presiona s para comenzar: ")
  if next2.lower() == "s":

    print()
    cuantasRodas = int(input("cuantas rondas quieres jugar:"))
    print()
    print ("¡¡Preparadx, comencemos!!")
    print()

    
    listasIngresadas = []
    letraQueIngresan = []
    puntaje = 0


   
    for i in range (cuantasRodas):

      if __name__ == '__main__':
        letraRandom = random.choice(string.ascii_letters)
    
        print ('Tu letra es: ' + letraRandom)
        print()

      
      lista = []

      inicio = time.time()
      
      nombre = input("Ingresa el nombre: ")
      print("_________________")
      print()
      
      if nombre[0] == letraRandom[0]:
         puntaje = puntaje + 50        
         print('¡Sigue así!')
        
      elif nombre[0] != letraRandom[0]:
         puntaje = puntaje - 25 
         print('ohhh que mal, ¡Sigue intentado!')
         
      apellido = input("Ingresa el apellido: ")
      print("_________________")
      print()
      
      if apellido[0] == letraRandom[0]:
         puntaje = puntaje + 50        
         print('¡Sigue así!')
        
      elif apellido[0] != letraRandom[0]:
         puntaje = puntaje - 25 
         print('ohhh que mal, ¡Sigue intentado!')
         

      ciudad = input("Ingresa la ciudad: ")
      print("_________________")
      print()
      
      if ciudad[0] == letraRandom[0]:
         puntaje = puntaje + 50        
         print('¡Sigue así!')
        
      elif ciudad[0] != letraRandom[0]:
         puntaje = puntaje - 25 
         print('ohhh que mal, ¡Sigue intentado!')
         

      fruta = input("Ingresa la fruta: ")
      print("_________________")
      print()
      
      if fruta[0] == letraRandom[0]:
         puntaje = puntaje + 50        
         print('¡Sigue así!')
        
      elif fruta[0] != letraRandom[0]:
         puntaje = puntaje - 25 
         print('ohhh que mal, ¡Sigue intentado!')
         

      animal = input("Ingresa el animal:  ")
      print("_________________")
      print()
      
      if animal[0] == letraRandom[0]:
         puntaje = puntaje + 50        
         print('¡Sigue así!')
        
      elif animal[0] != letraRandom[0]:
         puntaje = puntaje - 25 
         print('ohhh que mal, ¡Sigue intentado!')
         

      cosa = input("Ingresa la cosa: ")
      print("_________________")
      print()

      if cosa[0] == letraRandom[0]:
         puntaje = puntaje + 50        
         print('¡Sigue así!')
        
      elif cosa[0] != letraRandom[0]:
         puntaje = puntaje - 25 
         print('ohhh que mal, ¡Sigue intentado!')
         print()
      print("¡Siguiente ronda!")
      final = time.time()
          
      tiempo = round(final-inicio)
      

      
    if tiempo < 15:
        print("tu tiempo fue de: " +str(tiempo)+ " Exelente")
        print()
          
    if tiempo  > 16:
        print("tu tiempo fue de: " +str(tiempo)+ " Lo puedes hacer mejor")
        print()
        
    lista.append(nombre)
    lista.append(apellido)
    lista.append(ciudad)
    lista.append(fruta)
    lista.append(animal)
    lista.append(cosa)
    lista.append(puntaje)
    listasIngresadas.append(lista)
    
  df = pd.DataFrame(listasIngresadas, columns = ['nombre', 'apellido', 'ciudad', 'fruta', 'animal', 'cosa','puntaje'])  
  print("---------")
  print(df)
