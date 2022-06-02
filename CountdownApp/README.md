# Countdown App

## Overview
Sometimes, you may want to introduce a countdown procedure into your Kivy UI. You can do this in many ways. For example,
you can create a new Thread that does the counting, you can create an animation which changes a label, but the most
straightforward way is to schedule a Kivy Clock Event.

You can read more about the Kivy Clock [here](https://kivy.org/doc/stable/api-kivy.clock.html).

In essence, the Kivy Clock is in charge of scheduling all the lines of code to be run. If we wanted to create a countdown
from 10 seconds to 0 seconds we could schedule the Kivy Clock to decrement a label every second starting at 10 until it
reaches 0. This example also shows that you can switch screens after the countdown is done. 

Take note of the comments in `countdown.py` which show how to check how many Clock events are running and how to unschedule
a Clock event using `return False` to ensure you do not have too many Clock events slowing down your program.


## Running the App
Ensure you are using a python interpreter with Kivy installed, navigate to the CountdownApp folder, and run the following
in your terminal --
```
python3 countdown.py
```