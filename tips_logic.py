import game_points
def on_tips_button_click(event, label_text, label_points, show_tips):
    if game_points.__points <= 0:
        label_text("У вас нет баллов! Иди работай!")
        return
    show_tips()
    game_points.points_down()
    label_points(game_points.__points)
