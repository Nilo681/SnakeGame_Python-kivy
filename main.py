from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

class SnakePart(Widget):
    pass


class GameScreen(Widget):
    step_size = 40
    movement_x = 0
    movement_y = 0
    snake_parts = []

    def new_game(self):
        self.snake_parts = []
        movement_x = 0
        movement_y = 0
        head = SnakePart()
        head.pos = (0,0)
        self.snake_parts.append(head)
        self.add_widget(head)

    def on_touch_up(self, touch):
        dx = touch.x - touch.opos[0]
        dy = touch.y - touch.opos[1]
        if abs(dx) > abs(dy):
            # moving left or right
            self.movement_y = 0
            if dx > 0:
                self.movement_x = self.step_size
            else:
                self.movement_x = -self.step_size
        else:
            # moving up or down
            self.movement_x = 0
            if dy >0:
                self.movement_y = self.step_size
            else:
                self.movement_y = -self.step_size

    def next_frame(self, *args):
        
        #move the snake
        #move the head
        head = self.snake_parts[0]
        head.x += self.movement_x
        head.y += self.movement_y
        #move the body

        #check for snake collinding with food
        #check for snake collinding with snake
        #check for snake collinding with wall
        pass
    pass

class MainApp(App):
    def on_start(self):
        self.root.new_game()

        Clock.schedule_interval(self.root.next_frame, .5)
    pass


MainApp().run()