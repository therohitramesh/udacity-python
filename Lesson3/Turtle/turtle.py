#! /usr/bin/python
import turtle

def draw_square(some_turtle) :
	for i in (1,5):
		some_turtle.forward(100)
		some_turtle.right(90)


def draw_art() :
	
	window = turtle.Screen()
	window.bgcolor("red")
	

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(3)
	draw_square(brad)

	angie = turtle.Turtle()
	angie.shape("circle")
	angie.circle(100)
	
	window.exitonclick()

draw_art()