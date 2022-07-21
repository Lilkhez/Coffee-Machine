# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
#
# print(timmy)
# print(my_screen.canvheight, my_screen.canvwidth)
# timmy.color("DeepSkyBlue", "Red")
# timmy.begin_fill()
#
#
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#
#     if abs(timmy.pos()) < 1:
#         break
#
# timmy.end_fill()
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"],
])

table.align = "r"
print(table)
