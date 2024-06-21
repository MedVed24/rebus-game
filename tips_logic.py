import game_points
def on_tips_button_click(event, num_tips_click, len_answer, label_text, label_points, show_tips):
    if num_tips_click<len_answer:
        if game_points.__points <= 0:
            label_text("У вас нет баллов!")
            return
        show_tips()
        game_points.points_down()
        label_points(game_points.__points)
