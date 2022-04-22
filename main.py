import pyray as pr

if __name__ == '__main__':
    pr.init_window(500, 500, "new window")

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.WHITE)
        # pr.draw_text("Hello World", 190, 200, 20, pr.VIOLET)
        pr.end_drawing()

    pr.close_window()
