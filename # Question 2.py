# Question 2
# Calculate the points earned by a soccer team. The team won 18 games and ended 7 games as a draw.
# A win brings 3 points, while a draw brings 1 point

next = input("""Press Enter to continue with Question 2...""")

win = 3 
draw = 1
loss = 0

team = input("""Soccer team(club name):
 """)
no_of_win = int(input("""Number of game won:
"""))
no_of_draw = int(input("""Number of game drawn:
"""))
no_of_loss = int(input("""Number of game lost:
"""))
game_played = (no_of_win + no_of_draw + no_of_loss)
points_earned = ((no_of_win * win) + (no_of_draw * draw) + (no_of_loss * loss))

win_singular = "win"
win_plural = win_singular + "s"
if(no_of_win > 1):
    win = win_plural
else:
    win = win_singular

draw_singular = "draw"
draw_plural = draw_singular + "s"
if(no_of_draw > 1):
    draw = draw_plural
else:
    draw = draw_singular
    
loss_singular = "loss"
loss_plural = loss_singular + "es"
if(no_of_loss > 1):
    loss = loss_plural
else:
    loss = loss_singular
point_singular = "point"
point_plural = point_singular + "s"
if(points_earned > 1):
    point = point_plural
else:
    point = point_singular
print(f"{team} have earned {points_earned} {point} from {no_of_win} {win}, {no_of_draw} {draw}, and {no_of_loss} {loss}, haven played {game_played} games")