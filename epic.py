import tkinter as tk
import random
window_availability_factor = .88#depending on how much space taskbar/window headings/etc take up from the screen, you may have to modify this
SIZE = 40# how many pixels wide/tall each square is
MAX_SIZE = 30
X = 0###how many
Y = 10
NUM_COLORS = 0
COMBO = []
class Game(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.alive=True
        self.title('Megamind')
        self.canvas = tk.Canvas(self, width=max(NUM_COLORS+1,X+(X-1)//4+1)*SIZE+1, height=(Y+2)*SIZE+1, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.won = False
        self.bind("<Button-1>", self.click)
        
    def click(self, event):
        if not self.alive:reset()
        x = event.x // SIZE
        y = event.y // SIZE
        if x >= 0 and x < NUM_COLORS and y == Y+1:
            click(x)
            self.redraw()
            if game_over() and not self.won:self.end()
        if x == NUM_COLORS and y == Y+1:
            undo()
            self.redraw()
            

    def end(self):
        self.alive = False
        self.canvas.create_text(SIZE*X//2,SIZE*Y//2, text='GAME OVER',font=('Monaco',X*SIZE//7))
    def win(self):
        self.alive = False
        self.won=True
    def redraw(self):
#        if not self.alive:return
        for column in range(X):
            for row in range(Y):
                x1 = column*SIZE
                y1 = row * SIZE
                x2 = x1 + SIZE
                y2 = y1 + SIZE
                self.canvas.create_rectangle(x1,y1,x2,y2, fill=c__[guesses[row][column]])
        for i in range(len(vals)):
            for j in range(vals[i][0]):
                self.canvas.create_rectangle((X+(j//2)/2)*SIZE,(i+(j%2)/2)*SIZE,(X+.5+(j//2)/2)*SIZE,(i+.5+(j%2)/2)*SIZE, fill='#000000')
            for j in range(vals[i][0],vals[i][0]+vals[i][1]):
                self.canvas.create_rectangle((X+(j//2)/2)*SIZE,(i+(j%2)/2)*SIZE,(X+.5+(j//2)/2)*SIZE,(i+.5+(j%2)/2)*SIZE, fill='#888888')
        for i in range(NUM_COLORS):
            self.canvas.create_rectangle(i*SIZE,(Y+1)*SIZE,(i+1)*SIZE,(Y+2)*SIZE, fill=c__[i])
        self.canvas.create_rectangle(NUM_COLORS*SIZE,(Y+1)*SIZE,(NUM_COLORS+1)*SIZE,(Y+2)*SIZE, fill='#ffffff')
        self.canvas.create_text(SIZE*(NUM_COLORS+.5),(Y+1.5)*SIZE, text='UNDO',font=('Monaco',SIZE//3))
        if self.won:
            self.canvas.create_text(SIZE*X//2,SIZE*Y//2, text='YOU WON',font=('Monaco',X*SIZE//5))
class ColorPicker(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=SIZE*8+1, height=1+SIZE, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.bind("<Button-1>", self.click)
        self.title('Select How Many Colors You Wish to Use')
        for i in range(8):
            self.canvas.create_rectangle(SIZE*i,0,SIZE*(i+1),SIZE,fill=c__[i])
        for i in range(2,8):
            self.canvas.create_text(SIZE*(i+.5),SIZE/2, text=str(i+1),font=('Monaco',SIZE))
    def click(self, event):
        x = event.x // SIZE
        y = event.y // SIZE
        if x >= 0 and x < 8 and y == 0:
            global NUM_COLORS
            NUM_COLORS = x+1
            global c__
            c__=c__[:NUM_COLORS]+['#bbbbbb']
            self.destroy()
            XPicker()
class XPicker(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=SIZE*9+1, height=1+SIZE, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.bind("<Button-1>", self.click)
        self.title('Pick How Long the Code is')
        for i in range(9):
            self.canvas.create_rectangle(SIZE*i,0,SIZE*(i+1),SIZE,fill='#ffffff')
            self.canvas.create_text(SIZE*(i+.5),SIZE/2, text=str(i+4),font=('Monaco',int(SIZE*.8)))
    def click(self, event):
        x = event.x // SIZE
        y = event.y // SIZE
        if x >= 0 and x < 9 and y == 0:
            global X
            X= x+4
            self.destroy()
            AttemptsPicker()
class AttemptsPicker(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=min(36,int(self.winfo_screenheight()*.05)-5)*SIZE, height=1+SIZE, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.bind("<Button-1>", self.click)
        self.title('Pick How Many Attempts You Get')
        for i in range(min(36,int(self.winfo_screenheight()*.05)-5)):
            self.canvas.create_rectangle(SIZE*i,0,SIZE*(i+1),SIZE,fill='#ffffff')
            self.canvas.create_text(SIZE*(i+.5),SIZE/2, text=str(i+5),font=('Monaco',int(SIZE*.8)))
    def click(self, event):
        global SIZE
        x = event.x // SIZE
        y = event.y // SIZE
        if x >= 0 and x < min(36,int(self.winfo_screenheight()*.05)-5) and y == 0:
            global Y
            Y= x+5
#            print(Y,(self.winfo_screenheight()*.9))
            SIZE = min(MAX_SIZE,int((self.winfo_screenheight()*.88)//(Y+2)))
            self.destroy()
            reset()
def compare(_1,_2):
    q1,q2 = [i for i in _1],[j for j in _2]
    b = 0
    g = 0
    for i in range(len(q1)):
        if q1[i] == q2[i]:b+=1
    while(q1):
        if q1[0] in q2:
            g += 1
            q2.remove(q1[0])
        q1.remove(q1[0])
    return b,g-b
def game_over():
    return tries >= Y
def click(x):
    global square,tries,guesses
    guesses[tries][square] = x
    square += 1
    if square == X:
        global vals
        vals += [compare(COMBO,guesses[tries])]
        if vals[-1] == (X,0):game.win()
        tries += 1
        square = 0
def undo():
    global square,guesses
    square = max(square-1,0)
    guesses[tries][square] = -1
    
def reset():
    global game,vals,guesses,square,tries,COMBO
    COMBO = [int(random.random()*NUM_COLORS) for i in range(X)]
    vals = []
    guesses = [[-1 for i in range(X)] for j in range(Y)]
    square = 0
    tries = 0
    try:game.destroy()
    except:0
    game = Game()
    game.redraw()
    game.mainloop()
#vals = []
#guesses = [[-1 for i in range(X)] for j in range(10)]
#square = 0
#tries = 0

c__ = ["#ff0000","#ffff00","#44ff00","#00ffff","#0044ff","#cc00ff","#ffaaaa","#aaffbb"]
ColorPicker()

#game = Game()
#game.redraw()
#game.mainloop()
