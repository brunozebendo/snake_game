from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
"""as variáveis foram escritas no começo para facilitar caso se queira mudá-las 
no futuro. São maiúsculas pois são constantes
Observar como foi utilizado o POO nesse código, aqui se criou a classe SNAKE
 com as carcterísticas necessárias, primeiro, as características obrigatórias, depois a posição inicial,
  depois a função mover"""

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    """ esta função pega as posições no dicionário e atribui as características a ela
     (forma, cor, caneta para cima, posição (conforme as duplas no dicionário)"""

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
"""os números no for loop significam start, stop, step, mas o python não aceita que se escreva
 dentro de um for loop. O uso do len serve para que a função funcione independentemente do tamanho.
  Segments é a lista criada para enfileirar as três “tartarugas” em sequência. A intenção da função
   é fazer com que a “tartaruga” posterior fique na posição da anterior e crie assim o efeito cobra.
    Notar como se usa o self pois se está dentro da classe"""
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
"""essas funções controlam a cobrinha conforme as funções criadas na função main.
 Os graus da direção estão no começo do código, o if serve para não permitir que a cobra “dê ré”"""