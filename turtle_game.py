import turtle 
import random

'''This project is created by sourabh gond in 3rd year, 5th sem'''

WIDTH=800
HEIGHT=600
screen = turtle.Screen()
screen.setup( width = WIDTH, height = HEIGHT)

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)


class Race:
    
    def __init__(self,total_turtle):
        turtle_size=50
        self.turtle_size = turtle_size
        self.total_turtle = total_turtle
        self.turtle_size = turtle_size
        self.players = [None]*total_turtle
        colors  = ["red","green","blue","orange","purple","pink","yellow","brown","grey","black"]
        turtle.tracer(False)
        for i in range(len(self.players)):
            self.players[i] = turtle.Turtle()
            self.players[i].shape("turtle")
            color = random.choice(colors)
            colors.remove(color)
            self.players[i].color(color)
            self.players[i].setheading(90)
            self.players[i].shapesize(2)
            
        
    def createRaceTrack(self):
        turtle.tracer(False)
        self.total_turtle+=2
        start = (-(self.total_turtle/2)*self.turtle_size)+self.turtle_size
        track = turtle.Turtle()
        track.setheading(0)
        track.up()
        track.goto(start,-HEIGHT/2+self.turtle_size)
        track.down()
        track.forward(self.turtle_size*(self.total_turtle-2))
        track.setheading(90)
        track.forward(HEIGHT-2*self.turtle_size)
        track.setheading(180)
        track.forward((self.turtle_size*(self.total_turtle-2)))
        for i in range(self.total_turtle-1):
            track.up()
            track.goto(start,-HEIGHT/2+self.turtle_size)
            track.down()
            track.setheading(90)
            track.forward(HEIGHT-2*self.turtle_size)
            start+=self.turtle_size
        track.hideturtle()
        

    def createPlayers(self):
        turtle.tracer(True)
        start = (-(self.total_turtle/2)*self.turtle_size)+self.turtle_size
        for player in self.players:
            player.up()
            #player.speed(100)
            player.goto(start+25,-HEIGHT/2+self.turtle_size-self.turtle_size/2)
            player.setheading(90)
            start+=self.turtle_size
    def move(self):
        i=0
        l = len(self.players)
        for player in self.players:
            player.up()
            player.forward(random.randint(1,10))
            if(player.position()[1]>=(HEIGHT/2-self.turtle_size-self.turtle_size/2)):     
                return i+1
            i=(i+1)%l
        return None
    
def main():
    race = Race(10)   #Race(total_turtle) pass total number of turtle<=10
    race.createRaceTrack()
    
    race.createPlayers()
    while True:
        y = race.move()
        if y==None:
            continue
        else:
            print(y,'th Turtle won')
            return
            
        
    
if __name__=='__main__':
    try:
        main()
        screen.exitonclick()
        screen.done()
    except Exception:
        pass
    finally:
        print('Bye')
