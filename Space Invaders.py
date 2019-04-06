import turtle
import math
import random

#Draw Background
turtle.Screen()
turtle.bgcolor("Black")
turtle.title("Space Invaders")
turtle.bgpic("giphy.gif")

#For writing the name of the game
game_name=turtle.Turtle()
game_name.speed(0)
game_name.color("Yellow")
game_name.penup()
game_name.setposition(-300,300)
gn="SPACE   INVADERS" 
game_name.write(gn, False, align="left", font=("Cooper Black", 45, "normal"))
game_name.hideturtle()

#Register the shapes
turtle.register_shape("giphy1.gif")
turtle.register_shape("rock.gif")

#Draw Border
border=turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setpos(-300, -300)
border.pendown()
border.pensize(3)
for i in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

#Set the score to zero
score=0

#Draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-290,270)
scorestring="Score : %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Draw Player
player=turtle.Turtle()
player.shape("rock.gif")
player.penup()
player.speed(0)
player.setpos(0,-200)
player.setheading(90)
player.shapesize(2,2)


playerspeed=15

#Draw enemies
#Choose number of enemies
number_of_enemies=5
#Create empty list of enemies
enemies=[]

#Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.color("Red")
    enemy.shape("giphy1.gif")
    enemy.speed(0)
    enemy.penup()
    x=random.randint(-200,200)
    y=random.randint(100,250)    
    enemy.setposition(x, y) 

enemyspeed=2

#Draw bullet
bullet=turtle.Turtle()
bullet.color("Yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate="ready"

#Move player left and write
def move_left():
    x=player.xcor()
    x=x-playerspeed
    if x<-280:
        x=-280
    player.setx(x)
    
def move_right():
    x=player.xcor()
    x=x+playerspeed
    if x>280:
        x=280
    player.setx(x)
    
def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        #Move the bullet just above the player
        bulletstate="fire"
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()
        
def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False
    
    
#Create Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

c=0
#Main Game loop
while True:
    
            
    for enemy in enemies:    
        #Move the enemy
        x=enemy.xcor()
        x=x+enemyspeed
        enemy.setx(x)
        
        
        #Move the enemy back and down
        if enemy.xcor()>280:
            #Moves all the enemies down
            for i in enemies:
                y=i.ycor()
                y=y-40
                i.sety(y)
            #Change enemy direction
            enemyspeed=enemyspeed*(-1)
            
        if enemy.xcor()<-280:
            #Moves all the enemies down
            for i in enemies:
                y=i.ycor()
                y=y-40
                i.sety(y)
            #Change enemy direction
            enemyspeed=enemyspeed*(-1)
            
        #Check for a collision between bullet and the enemy
        if isCollision(bullet,enemy):
            #Reset the bullet
            bullet.heading()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #Reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,250)    
            enemy.setposition(x, y) 
            #Update score
            score+=10
            scorestring="Score : %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

            
            
        #Check for a collision between player and the enemy
        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            bullet.hideturtle()
            c=1
            break
    
    if c==1:
        for enemy in enemies:
            enemy.hideturtle()
        #To print Game over    
        game_over=turtle.Turtle()
        game_over.speed(0)
        game_over.color("Yellow")
        game_over.penup()
        game_over.setposition(-190,-20)
        go="GAME OVER"
        game_over.write(go, False, align="left", font=("Algerian", 50, "normal"))
        game_over.hideturtle()
        break

            
    #Move the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
            
        
    #Check to see if the bullet has gone to the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"
        
        
turtle.done()
