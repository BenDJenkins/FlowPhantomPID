import time
import simple_pid
import scipy
from tkinter import *
import threading

# A work in progress PID for a cardiovascular flow phantom.

# Values

SetPoint = 0  # Flow rate set point (L/min)
PGain = 1  # Proportional Gain
IGain = 1  # Integral Gain
DGain = 1  # Derivative Gain
simple_pid.sample_time = 0.01  # update every 0.01 seconds

simple_pid.output_limits = (0, 10)    # Output limits

current_value = 1  # Initial value
current_value2 = 1

pump1status = 0  # Setting pumps to off state on program start.
pump2status = 0

output1 = 0
output2 = 0

# Read output of flow meter

flowrate_input = 0

# Filter

flowrate_input_filtered = flowrate_input

# GUI Setup


window = Tk()
window.title("Flow Phantom PID")
window.geometry('420x120')

# PUMP 1

Pump1lbl = Label(window, text="Pump 1")
Pump1lbl.grid(column=0, row=0)

SetPoint1lbl = Label(window, text="Flowrate Setpoint (L/min):")
SetPoint1lbl.grid(column=0, row=1)

SetPoint1 = Entry(window, width=10)
SetPoint1.grid(column=1, row=1)

# Show flowrate and pump speed in GUI

Flowrate1lbl = Label(window, text="Flowrate (L/min):")
Flowrate1lbl.grid(column=0, row=2)


def runflowrate1_val():
    while True:
        Flowrate1_val = Label(window, text=flowrate_input_filtered)  # Updating value
        Flowrate1_val.grid(column=1, row=2)
        time.sleep(0.5)  # Updates every 0.5 seconds so that the program doesn't take up too many resources.


Flowrate1_val = Label(window, text='0')
Flowrate1_val.grid(column=1, row=2)

Pumpspeed1_lbl = Label(window, text="Pump Speed (RPM):")
Pumpspeed1_lbl.grid(column=0, row=3)


def runpumpspeed1_val():
    while True:
        Pumpspeed1_val = Label(window, text=str(200))
        Pumpspeed1_val.grid(column=1, row=3)
        time.sleep(0.5)  # Updates every 0.5 seconds.
        if not runpumpspeed1_val:
            break


Pumpspeed1_val = Label(window, text='0')  # Setting initial label
Pumpspeed1_val.grid(column=1, row=3)

# Threading

def threading_runflowrate1_val():
    t2 = threading.Thread(target=runflowrate1_val)
    t2.setDaemon(True)
    t2.start()

def threadingbtn1():
    t1 = threading.Thread(target=btn1clicked)
    t1.setDaemon(True)
    t1.start()

def threading_runpumpspeed1_val():
    t3 = threading.Thread(target=runpumpspeed1_val)
    t3.setDaemon(True)
    t3.start()

# PID


pid = simple_pid.PID(PGain, IGain, DGain, setpoint=SetPoint1)  # PID block that takes input from flow meter


def run_pump1():
    while pump1status:
        output1 = pid(current_value)
        if not pump1status:
            break


# Buttons


def btn1clicked():

    pump1status = True
    pump1statuslbl.configure(text="Running",
                             bg="green"
                             )
    print(pump1status)  # Debug
    run_pump1()  # Calls pump1 run function
    threading_runflowrate1_val()
    threading_runpumpspeed1_val()


def btn2clicked():

    pump1status: bool = False
    pump1statuslbl.configure(text="Stopped",
                             bg="red"
                             )
    Flowrate1_val = Label(window, text='0')
    Flowrate1_val.grid(column=1, row=2)
    return


pump1btn = Button(window, text='Run', command=threadingbtn1)
pump1btn.grid(column=0, row=4)

pump2btn = Button(window, text='Stop', command=btn2clicked)
pump2btn.grid(column=1, row=4)

pump1statuslbl = Label(window, text='Stopped', bg='red')
pump1statuslbl.grid(column=1, row=0)

# PUMP 2

Pump2lbl = Label(window, text="Pump 2")
Pump2lbl.grid(column=2, row=0)

SetPoint2lbl = Label(window, text="Flowrate Setpoint (L/min):")
SetPoint2lbl.grid(column=2, row=1)

SetPoint2 = Entry(window, width=10)
SetPoint2.grid(column=3, row=1)

# Show flowrate and pump speed in GUI

Flowrate2lbl = Label(window, text="Flowrate (L/min):")
Flowrate2lbl.grid(column=2, row=2)


def runflowrate2_val():
    while True:
        Flowrate2_val = Label(window, text=flowrate_input_filtered)  # Updating value
        Flowrate2_val.grid(column=3, row=2)
        time.sleep(0.5)  # Updates every 0.5 seconds so that the program doesn't take up too many resources.


Flowrate2_val = Label(window, text='0')
Flowrate2_val.grid(column=3, row=2)

Pumpspeed2_lbl = Label(window, text="Pump Speed (RPM):")
Pumpspeed2_lbl.grid(column=2, row=3)


def runpumpspeed2_val():
    while True:
        Pumpspeed2_val = Label(window, text=str(200))
        Pumpspeed2_val.grid(column=3, row=3)
        time.sleep(0.5)  # Updates every 0.5 seconds.


Pumpspeed2_val = Label(window, text='0')  # Setting initial label
Pumpspeed2_val.grid(column=3, row=3)

# Threading

def threading_runflowrate2_val():
    t12 = threading.Thread(target=runflowrate2_val)
    t12.setDaemon(True)
    t12.start()

def threadingbtn3():
    t11 = threading.Thread(target=btn3clicked)
    t11.setDaemon(True)
    t11.start()

def threading_runpumpspeed2_val():
    t13 = threading.Thread(target=runpumpspeed2_val)
    t13.setDaemon(True)
    t13.start()

# PID

pid2 = simple_pid.PID(PGain, IGain, DGain, setpoint=SetPoint2)  # PID block that takes input from flow meter

def run_pump2():
    while pump2status:
        output2 = pid(current_value2)
        if not pump2status:
            break

# Buttons


def btn3clicked():

    pump2status: bool = True
    pump2statuslbl.configure(text="Running",
                             bg="green"
                             )
    print(pump2status)  # Debug
    run_pump2()  # Calls pump1 run function
    threading_runflowrate2_val()
    threading_runpumpspeed2_val()


def btn4clicked():

    pump2status: bool = False
    pump2statuslbl.configure(text="Stopped",
                             bg="red"
                             )
    Flowrate2_val = Label(window, text='0')  # Temporary until can get flowrate from flowmeter.
    Flowrate2_val.grid(column=3, row=2)
    return


pump3btn = Button(window, text='Run', command=threadingbtn3)
pump3btn.grid(column=2, row=4)

pump4btn = Button(window, text='Stop', command=btn4clicked)
pump4btn.grid(column=3, row=4)

pump2statuslbl = Label(window, text='Stopped', bg='red')
pump2statuslbl.grid(column=3, row=0)

window.mainloop()

