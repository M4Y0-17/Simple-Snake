import turtle
import time
import random
import colorama
from colorama import Fore
from signal import signal, SIGINT
from sys import exit



class snake_direction:
	def up():
		head.direction = "up"
	def down():
		head.direction = "down"
	def left():
		head.direction = "left"
	def right():
		head.direction = "right"



## Ventana
window = turtle.Screen()
window.title("Snake")
window.bgcolor("green")
window.setup(width = 600, height = 600)
# Hace mas fluidas las animaciones
window.tracer(0)


# Aqui almacenamos los cuantos cuadrados ha crecido la serpiente
snake = []


## Comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
# Color de al comida
food.color("red")
# No deja rastro cuando pasa por algun sitio
food.penup()
# Empieza desde la posicion 0,0
food.goto(0,100)
# La cabeza no tiene que moverse aun
food.direction = "stop"


## Cabeza
head = turtle.Turtle()
head.speed(0)
head.shape("square")
# Color de al cabeza
head.color("white")
# No deja rastro cuando pasa por algun sitio
head.penup()
# Empieza desde la posicion 0,0
head.goto(0,0)
# La cabeza no tiene que moverse aun
head.direction = "stop"


## Puntuacion
txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()
txt.goto(0, 260)
txt.write("Score: 0	High Score: 0", align = "center", font = ("Courier", 24, "normal"))


## Teclado
window.listen()
window.onkeypress(snake_direction.up, "Up")
window.onkeypress(snake_direction.down, "Down")
window.onkeypress(snake_direction.left, "Left")
window.onkeypress(snake_direction.right, "Right")


def marker(score, high_score):

	txt.clear()
	txt.write("Score: {}	High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))


def motion():

	# Si la direccion es arriba registra la posicion "y" en la variable y
	if head.direction == "up":
		y = head.ycor()
		# Aumentamos 20 pixeles la posicion actual
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		# Aumentamos 20 pixeles la posicion actual
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		# Aumentamos 20 pixeles la posicion actual
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		# Aumentamos 20 pixeles la posicion actual
		head.setx(x + 20)


def restart_snake():

	time.sleep(1)
	head.goto(0,0)
	head.direction = "stop"


def map_limits(score, high_score):

	restart_snake()

	# Reiniciamos el marcador
	marker(score, high_score)

	for body in snake:
		#large_snake.color("green")
		body.goto(1000, 1000)

	snake.clear()


def eat(score, high_score):

	# Creamos numeros random para las posiciones x y y
	x = random.randint(-280, 280)
	y = random.randint(-280, 280)
	# Actualizamos la posicion de la manzana
	food.goto(x, y)

	# Hacer grande la serpiente
	large_snake = turtle.Turtle()
	large_snake.speed(0)
	large_snake.shape("square")
	large_snake.color("gray")
	large_snake.penup()
	snake.append(large_snake)

	marker(score, high_score)


def Snake():

	# Marcador
	score = 0
	high_score = 0

	while True:
		window.update()

		# Bordes del mapa
		if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
			score = 0
			map_limits(score, high_score)

		# Si la distancia entre la comida y la serpiente es de menos de 20px que es lo que ocupa en pantalla un objeto, es decir si se sobreponen una a la otra...
		if head.distance(food) < 20:
			# Aumentar marcador
			score += 1

			# Aumentamos el record si el marcador actual es mayor que el record
			if score > high_score:
				high_score = score

			eat(score, high_score)

		# Si la serpiente ya tiene cuerpo la nueva parte del cuerpo va a seguir a la ultima parte del cuerpo
		total_snake = len(snake)
		for i in range(total_snake -1, 0, -1):
			x = snake[i - 1].xcor()
			y = snake[i - 1].ycor()
			snake[i].goto(x, y)

		# Si la serpiente solo tiene la cabeza el cuerpo va a seguir a la cabeza
		if total_snake > 0:
			x = head.xcor()
			y = head.ycor()
			snake[0].goto(x,y)

		motion()

		# Chocar con el cuerpo
		for x in snake:
			if x.distance(head) < 20:
				restart_snake()
				score = 0
				body_crash(score, high_score)

		seg_retard = 0.1
		time.sleep(seg_retard)


def body_crash(score, high_score):

	for x in snake:
		x.goto(1000, 1000)

	snake.clear()
	marker(score, high_score)


def banner():

	banner_tool='''
  ________  _____  ___        __       __   ___  _______  
 /"       )(\ "  \|"  \      /""\     |/"| /  ")/"     "| 
(:   \___/ |.\    \    |    /    \    (: |/   /(: ______) 
 \___  \   |: \.   \   |   /' /\  \   |    __/  \/    |   
  __/   \  |.  \    \. |  //  __'  \  (// _  \  // ___)_  
 /" \   :) |    \    \ | /   /  \   \ |: | \  \(:      "| 
(_______/   \___|\____\)(___/    \___)(__|  \__)\_______) 
	'''
	by = '''                                                 by M4Y0'''
	snake = '''
                                                                              
                      ████████████████                                
                  ████  ██░░░░██  ██▒▒████                            
                ██      ██░░██      ██▒▒▒▒██                          
              ██      ██░░░░██        ██▒▒██                          
            ██      ████░░████        ██▒▒██                          
            ██    ██████░░██████      ██▒▒▒▒██                        
            ██    ██████░░██████      ██▒▒▒▒██                        
            ██    ████░░░░██████      ██▒▒▒▒██                        
            ██      ██░░░░████      ██▒▒▒▒▒▒██                        
            ████████░░░░░░██      ██▒▒▒▒▒▒▒▒██                        
            ██▒▒▒▒▒▒░░░░░░░░██████▒▒▒▒▒▒▒▒▒▒██                        
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██                          
                ████████████████████▒▒▒▒▒▒██                          
                ▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                            
              ▒▒▒▒▒▒▒▒  ████▒▒▒▒▒▒▒▒▒▒██                              
          ▒▒▒▒▒▒▒▒▒▒    ██    ▒▒▒▒▒▒▒▒████████                        
      ▒▒▒▒▒▒▒▒▒▒▒▒    ██░░░░░░░░▒▒▒▒████▒▒▒▒▒▒██                      
  ▒▒▒▒▒▒▒▒▒▒▒▒        ██        ▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██                    
        ▒▒▒▒          ██░░░░░░▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒████████            
      ▒▒▒▒            ██      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██          
                      ██░░░░░░▒▒░░▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
                      ██    ▒▒░░▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██            
                      ██░░░░░░▒▒▒▒▒▒▒▒██  ██  ▒▒▒▒▒▒▒▒██              
                        ██░░░░░░▒▒▒▒██      ██  ▒▒████                
                          ██████████        ██████                    
	'''

	print("")
	print(Fore.GREEN + banner_tool)
	print(Fore.MAGENTA + by)
	print(Fore.RESET)
	print(snake)


def finish(signal_received, frame):

	print()
	print(Fore.RED)
	print("|-------------------------------------------------------|")
	print("|                         FINISH                        |")
	print("|-------------------------------------------------------|")
	print(Fore.RESET)
	exit(0)


if __name__ == '__main__':

	signal(SIGINT, finish)
	banner()
	Snake()