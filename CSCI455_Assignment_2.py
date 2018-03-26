from MockMaestro import Controller
from tkinter import *
import time
import os

# Maestro instantiation
controller = Controller()
for chan in range(len(controller.Targets)):
    controller.setTarget(chan, 6000)
controller.setAccel(0, 10)
controller.setAccel(1, 10)
controller.setAccel(2, 30)
controller.setAccel(3, 20)
controller.setAccel(3, 20)
os.system('xset r off')

# Global Variables
xpos = 0
ypos = 0
actions = []
pic_size = 50

# Main Tk window instantiation
root = Tk()
root.title("Robot Control GUI")

# Icon files and subsample
icons = [PhotoImage(file="icons/HeadTilt.png"), PhotoImage(file="icons/HeadRotate.png"),
         PhotoImage(file="icons/Move.png"), PhotoImage(file="icons/Rotate.png"),
         PhotoImage(file="icons/BodyRotate.png"), PhotoImage(file="icons/Wait.png")]
for i in range(len(icons)):
    icons[i] = icons[i].subsample(4, 4)


# Function to run all actions
def go():
    global actions, xpos, ypos
    print('go!')
    for x in range(len(actions)):
        if actions[x].name == 'Head Tilt':
            if actions[x].pos == 1:
                controller.setTarget(4, 4000)
            elif actions[x].pos == 2:
                controller.setTarget(4, 5000)
            elif actions[x].pos == 3:
                controller.setTarget(4, 7000)
            elif actions[x].pos == 4:
                controller.setTarget(4, 8000)
            elif actions[x].pos == 0:
                controller.setTarget(4, 6000)
            actions[x].animate()
            controller.setTarget(4, 6000)
        elif actions[x].name == 'Head Rotate':
            if actions[x].pos == 1:
                controller.setTarget(3, 4000)
            elif actions[x].pos == 2:
                controller.setTarget(3, 5000)
            elif actions[x].pos == 3:
                controller.setTarget(3, 7000)
            elif actions[x].pos == 4:
                controller.setTarget(3, 8000)
            elif actions[x].pos == 0:
                controller.setTarget(3, 6000)
            actions[x].animate()
            controller.setTarget(3, 6000)
        elif actions[x].name == 'Move':
            if actions[x].pos == 1:
                controller.setTarget(1, 5000)
            elif actions[x].pos == 2:
                controller.setTarget(1, 7000)
            elif actions[x].pos == 0:
                controller.setTarget(1, 6000)
            actions[x].animate()
            controller.setTarget(1, 6000)
        elif actions[x].name == 'Turn':
            if actions[x].pos == 1:
                controller.setTarget(2, 7000)
            elif actions[x].pos == 2:
                controller.setTarget(2, 5000)
            elif actions[x].pos == 0:
                controller.setTarget(2, 6000)
            actions[x].animate()
            controller.setTarget(2, 6000)
        elif actions[x].name == 'Body Rotate':
            if actions[x].pos == 1:
                controller.setTarget(0, 4250)
            elif actions[x].pos == 2:
                controller.setTarget(0, 7750)
            elif actions[x].pos == 0:
                controller.setTarget(0, 6000)
            actions[x].animate()
            controller.setTarget(0, 6000)
        elif actions[x].name == 'Wait':
            actions[x].animate()
    posx = 25
    posy = 25
    for x in range(len(actions)):
        if posx < 700:
            canvas.create_image(posx, posy, image=actions[x].icon)
            posx += 55
        else:
            posy += 55
            posx = 25
            canvas.create_image(posx, posy, image=actions[x].icon)
            posx += 55


# Function to delete all actions and reset canvas
def del_all():
    global xpos, ypos, actions
    canvas.delete("all")
    xpos = 0
    ypos = 0
    actions = []


# Class to represent an action to be run
class Action:
    def __init__(self, name, icon):
        global xpos, ypos
        self.name = name
        self.icon = icon
        if xpos < 700:
            canvas.create_image(25 + xpos, 25 + ypos, image=self.icon)
        else:
            ypos += 55
            xpos = 0
            canvas.create_image(25 + xpos, 25 + ypos, image=self.icon)
        self.time = 2
        self.pos = 0
        self.settings_tk = ''
        self.animate_tk = ''
        xpos += 55

    # Animation function!
    def animate(self):
        canvas.delete("all")
        rect = []
        canvas.create_text(100, 130, text=self.name + " : " + str(self.time) + " seconds", fill="white")
        if self.pos == 0:
            canvas.create_text(100, 150, text="Waiting...", fill="white")
        else:
            canvas.create_text(100, 150, text="Position : " + str(self.pos), fill="white")
        for x in range(self.time):
            rect.append(canvas.create_image(25 + 55 * x, 200, image=self.icon))
        for x in range(self.time):
            canvas.update()
            canvas.delete(rect[self.time - x - 1])
            time.sleep(1)
        canvas.delete("all")

    # Function to edit settings or remove instance
    def open_settings(self):
        def save_val():
            self.time = time_scale.get()
            self.pos = position.get()
            self.settings_tk.destroy()

        self.settings_tk = Tk()
        self.settings_tk.title("Settings")
        label1 = Label(self.settings_tk, text="Time (S)")
        label1.pack()
        time_scale = Scale(self.settings_tk, from_=1, to=10, orient=HORIZONTAL)
        time_scale.set(self.time)
        time_scale.pack()
        if self.name == 'Head Tilt':
            label1 = Label(self.settings_tk, text="Head Tilt Position (Left to Right)")
            position = Scale(self.settings_tk, from_=1, to=4, orient=HORIZONTAL)
        elif self.name == 'Head Rotate':
            label1 = Label(self.settings_tk, text="Head Rotate Position (Left to Right)")
            position = Scale(self.settings_tk, from_=1, to=4, orient=HORIZONTAL)
        elif self.name == 'Turn':
            label1 = Label(self.settings_tk, text="Turning Direction (Left or Right)")
            position = Scale(self.settings_tk, from_=1, to=2, orient=HORIZONTAL)
        elif self.name == 'Move':
            label1 = Label(self.settings_tk, text="Movement Direction (Foreword or Backward)")
            position = Scale(self.settings_tk, from_=1, to=2, orient=HORIZONTAL)
        elif self.name == 'Body Rotate':
            label1 = Label(self.settings_tk, text="Body Rotate Position (Left to Right)")
            position = Scale(self.settings_tk, from_=1, to=4, orient=HORIZONTAL)
        position.set(self.pos)
        position.pack()
        label1.pack()
        save_values = Button(self.settings_tk, text="Save Values", command=save_val)
        save_values.pack()
        delete = Button(self.settings_tk, text="Delete", command=self.__delete__)
        delete.pack()
        self.settings_tk.mainloop()

    def __delete__(self):
        global xpos, actions
        self.time = 0
        self.pos = 0
        canvas.delete("all")
        xpos -= 55
        posx = 25
        posy = 25
        actions.remove(self)
        self.settings_tk.destroy()
        for x in range(len(actions)):
            if posx < 700:
                canvas.create_image(posx, posy, image=actions[x].icon)
                posx += 55
            else:
                posy += 55
                posx = 25
                canvas.create_image(posx, posy, image=actions[x].icon)
                posx += 55


# Mouse movement class
class MouseMovement:
    def __init__(self):
        self.flag = False

    def mouse_pressed(self, event):
        global actions
        y = 0
        for x in range(len(actions)):
            if x == 13 * (y + 1):
                y += 1
            if x * 55 + 50 - 715 * y > event.x > x * 55 - 715 * y and y * 55 < event.y < y * 55 + 50:
                self.flag = True
                actions[x].open_settings()

    def mouse_release(self, event):
        if self.flag:
            self.flag = False


# Mouse movement class instantiation
m = MouseMovement()

# Root's canvas
canvas = Canvas(root, bg="#1F1F1F", width="740", height="443")
canvas.pack(side=RIGHT)
canvas.bind('<ButtonPress-1>', m.mouse_pressed)
canvas.bind('<ButtonRelease-1>', m.mouse_release)

# Root's buttons
go = Button(root, height=3, width=6, text='GO!', bg='black', fg='white', command=go)
go.pack(side=TOP)
ht = Button(root, command=lambda: actions.append(Action('Head Tilt', icons[0])), image=icons[0], width=pic_size,
            height=pic_size)
ht.pack(side=TOP)
hr = Button(root, command=lambda: actions.append(Action('Head Rotate', icons[1])), image=icons[1], width=pic_size,
            height=pic_size)
hr.pack(side=TOP)
run = Button(root, command=lambda: actions.append(Action('Move', icons[2])), image=icons[2], width=pic_size,
             height=pic_size)
run.pack(side=TOP)
turn = Button(root, command=lambda: actions.append(Action('Turn', icons[3])), image=icons[3], width=pic_size,
              height=pic_size)
turn.pack(side=TOP)
br = Button(root, command=lambda: actions.append(Action('Body Rotate', icons[4])), image=icons[4], width=pic_size,
            height=pic_size)
br.pack(side=TOP)
wait = Button(root, command=lambda: actions.append(Action('Wait', icons[5])), image=icons[5], width=pic_size,
              height=pic_size)
wait.pack(side=TOP)
del_all = Button(root, height=3, width=6, text='Clear', bg='black', fg='white', command=del_all)
del_all.pack(side=TOP)

# Main tk loop and geometry
root.geometry("800x450")
root.mainloop()
os.system('xset r on')
