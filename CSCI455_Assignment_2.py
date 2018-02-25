import Maestro
from tkinter import *
import os
import time

# x = Maestro.Controller()
#
# for chan in range(len(x.Targets)):
#      x.setTarget(chan, 6000)
#
# x.setAccel(0, 10)
# x.setAccel(1, 10)
# x.setAccel(2, 30)
# x.setAccel(3, 20)
# x.setAccel(3, 20)
#
os.system('xset r off')

xpos = 0
ypos = 300
action_count = 0
actions = []
pic_size = 100

root = Tk()

ht_icon = PhotoImage(file="icons\HeadTilt.png")
ht_icon = ht_icon.subsample(2, 2)
hr_icon = PhotoImage(file="icons\HeadRotate.png")
hr_icon = hr_icon.subsample(2, 2)
run_icon = PhotoImage(file="icons\Move.png")
run_icon = run_icon.subsample(2, 2)
turn_icon = PhotoImage(file="icons\Rotate.png")
turn_icon = turn_icon.subsample(2, 2)
br_icon = PhotoImage(file="icons\BodyRotate.png")
br_icon = br_icon.subsample(2, 2)
wait_icon = PhotoImage(file="icons\Wait.png")
wait_icon = wait_icon.subsample(2, 2)


def go():
    print('go!')
    for x in range(len(actions)):
        if actions[x].name == 'ht':
            # if actions[x].pos == 1:
            #     x.setTarget(4, 4000)
            # elif actions[x].pos == 2:
            #     x.setTarget(4, 5000)
            # elif actions[x].pos == 3:
            #     x.setTarget(4, 7000)
            # elif actions[x].pos == 4:
            #     x.setTarget(4, 8000)
            # elif actions[x].pos == 0:
            #     x.setTarget(4, 6000)
            time.sleep(actions[x].time)
            # x.setTarget(4, 6000)
        elif actions[x].name == 'hr':
            # if actions[x].pos == 1:
            #     x.setTarget(3, 4000)
            # elif actions[x].pos == 2:
            #     x.setTarget(3, 5000)
            # elif actions[x].pos == 3:
            #     x.setTarget(3, 7000)
            # elif actions[x].pos == 4:
            #     x.setTarget(3, 8000)
            # elif actions[x].pos == 0:
            #     x.setTarget(3, 6000)
            time.sleep(actions[x].time)
            # x.setTarget(3, 6000)
        elif actions[x].name == 'run':
            # if actions[x].pos == 1:
            #     x.setTarget(1, 5000)
            # elif actions[x].pos == 2:
            #     x.setTarget(1, 7000)
            # elif actions[x].pos == 0:
            #     x.setTarget(1, 6000)
            time.sleep(actions[x].time)
            # x.setTarget(1, 6000)
        elif actions[x].name == 'turn':
            # if actions[x].pos == 1:
            #     x.setTarget(2, 7000)
            # elif actions[x].pos == 2:
            #     x.setTarget(2, 5000)
            # elif actions[x].pos == 0:
            #     x.setTarget(2, 6000)
            time.sleep(actions[x].time)
            # x.setTarget(2, 6000)
        elif actions[x].name == 'br':
            # if actions[x].pos == 1:
            #     x.setTarget(0, 4250)
            # elif actions[x].pos == 2:
            #     x.setTarget(0, 7750)
            # elif actions[x].pos == 0:
            #     x.setTarget(0, 6000)
            time.sleep(actions[x].time)
            # x.setTarget(0, 6000)
        elif actions[x].name == 'wait':
            time.sleep(actions[x].time)


def ht():
    global xpos, ypos, action_count, actions
    canvas.create_image(50 + xpos, ypos, image=ht_icon)
    xpos += 105
    actions.append(Icon('ht', action_count))
    action_count += 1


def hr():
    global xpos, ypos, action_count, actions
    canvas.create_image(50 + xpos, ypos, image=hr_icon)
    xpos += 105
    actions.append(Icon('hr', action_count))
    action_count += 1


def run():
    global xpos, ypos, action_count, actions
    canvas.create_image(50 + xpos, ypos, image=run_icon)
    xpos += 105
    actions.append(Icon('run', action_count))
    action_count += 1


def turn():
    global xpos, ypos, action_count, actions
    canvas.create_image(50 + xpos, ypos, image=turn_icon)
    xpos += 105
    actions.append(Icon('turn', action_count))
    action_count += 1


def br():
    global xpos, action_count, actions
    canvas.create_image(50 + xpos, ypos, image=br_icon)
    xpos += 105
    actions.append(Icon('br', action_count))
    action_count += 1


def wait():
    global xpos, action_count, actions
    canvas.create_image(50 + xpos, ypos, image=wait_icon)
    xpos += 105
    actions.append(Icon('wait', action_count))
    action_count += 1


class Icon:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.time = 2
        self.pos = 0

    def open_settings(self):
        def save_val():
            self.time = time_scale.get()
            self.pos = position.get()

        settingstk = Tk()
        label1 = Label(settingstk, text="Time (S)")
        label1.pack()
        time_scale = Scale(settingstk, from_=1, to=10, orient=HORIZONTAL)
        time_scale.pack()
        if self.name == 'ht':
            label1 = Label(settingstk, text="Position (Left to Right)")
            label1.pack()
            position = Scale(settingstk, from_=1, to=4, orient=HORIZONTAL)
            position.pack()
        elif self.name == 'hr':
            label1 = Label(settingstk, text="Position (Left to Right)")
            label1.pack()
            position = Scale(settingstk, from_=1, to=4, orient=HORIZONTAL)
            position.pack()
        elif self.name == 'turn':
            label1 = Label(settingstk, text="Direction (Left or Right)")
            label1.pack()
            position = Scale(settingstk, from_=1, to=4, orient=HORIZONTAL)
            position.pack()
        elif self.name == 'run':
            label1 = Label(settingstk, text="Direction (Foreword or Backward)")
            label1.pack()
            position = Scale(settingstk, from_=1, to=4, orient=HORIZONTAL)
            position.pack()
        elif self.name == 'br':
            label1 = Label(settingstk, text="Position (Left to Right)")
            label1.pack()
            position = Scale(settingstk, from_=1, to=4, orient=HORIZONTAL)
            position.pack()
        save_values = Button(settingstk, text="Save Values", command=save_val)
        save_values.pack()
        delete = Button(settingstk, text="Delete", command=self.__delete__)
        delete.pack()
        settingstk.mainloop()

    def __delete__(self):
        self.time = 0


class MouseMovement:
    def __init__(self):
        self.flag = False

    def mouse_pressed(self, event):
        global action_count, actions
        for x in range(len(actions)):
            if (x * 105 + 100) > event.x > (x * 105) and 250 < event.y < 350 and action_count > x:
                self.flag = True
                actions[x].open_settings()

    def mouse_release(self, event):
        if self.flag:
            self.flag = False


m = MouseMovement()

canvas = Canvas(root, bg= "#1F1F1F", width="830", height="660")
canvas.pack(side=RIGHT)
canvas.bind('<ButtonPress-1>', m.mouse_pressed)
canvas.bind('<ButtonRelease-1>', m.mouse_release)

ht = Button(root, command=ht)
ht.config(image=ht_icon, width=pic_size, height=pic_size)
ht.pack(side=TOP)

hr = Button(root, command=hr)
hr.config(image=hr_icon, width=pic_size, height=pic_size)
hr.pack(side=TOP)

run = Button(root, command=run)
run.config(image=run_icon, width=pic_size, height=pic_size)
run.pack(side=TOP)

turn = Button(root, command=turn)
turn.config(image=turn_icon, width=pic_size, height=pic_size)
turn.pack(side=TOP)

br = Button(root, command=br)
br.config(image=br_icon, width=pic_size, height=pic_size)
br.pack(side=TOP)

wait = Button(root, command=wait)
wait.config(image=wait_icon, width=pic_size, height=pic_size)
wait.pack(side=TOP)

go = Button(root, width=13, text='GO!', bg='black', fg='white', command=go)
go.pack(side=TOP)

root.mainloop()

os.system('xset r on')