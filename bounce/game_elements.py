from random import shuffle


class Ball:
    canvas: "tkinter.Canvas"
    platform: "Platform"
    score: "Score"
    color: str
    object_id: int
    x: int
    y: int
    canvas_height: int
    canvas_width: int

    def __init__(self, canvas, platform, score, color):
        self.hit_bottom = False
        self.canvas = canvas
        self.platform = platform
        self.score = score
        self.color = color
        self.object_id = canvas.create_oval(10,10, 25, 25, fill=self.color)

        self.canvas.move(self.object_id, 245, 100)

        _starts = [-2, -1, 1, 2]
        shuffle(_starts)

        self.x = _starts[0]
        self.y = -2

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_platform(self, pos):
        platform_pos = self.canvas.coords(self.platform.object_id)

        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if platform_pos[1] <= pos[3] <= platform_pos[3]:
                self.score.hit()
                return True

        return False

    def draw(self):
        self.canvas.move(self.object_id, self.x, self.y)
        pos = self.canvas.coords(self.object_id)

        if pos[1] <= 0:
            self.y = 2

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.canvas.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')

        if self.hit_platform(pos):
            self.y = -2

        if pos[0] <= 0:
            self.x = 2

        if pos[2] >= self.canvas_width:
            self.x = -2


class Platform:
    canvas: "tkinter.Canvas"
    color: str
    object_id: int
    canvas_width: int
    x: int
    speed: float
    started: bool

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.object_id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.x = 0
        self.speed = 2.0
        self.started = False

        _start_1 = [40, 60, 90, 120, 150, 180, 200]
        shuffle(_start_1)

        self.starting_point_x = _start_1[0]
        self.canvas.move(self.object_id, self.starting_point_x, 300)

        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def turn_right(self, event):
        self.x = 2 * self.speed

    def turn_left(self, event):
        self.x = -2 * self.speed

    def start_game(self, event):
        self.started = True

    def draw(self):
        self.canvas.move(self.object_id, self.x, 0)
        pos = self.canvas.coords(self.object_id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


class Score:
    canvas: "tkinter.Canvas"
    color: str
    score: int

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.score = 0
        self.object_id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.object_id, text=self.score)
