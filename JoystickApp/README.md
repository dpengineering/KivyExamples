# Joystick App

## Overview
This example shows you how to repeatedly poll for joystick values inside a Kivy application. We can either do this polling
manually or with a scheduled Kivy Clock event. This example shows you how to display joystick values onto a screen as well
as using them to move an ImageButton. The main takeaway in this example is to become more comfortable interacting with
the Kivy Clock.

## Troubleshooting `pygame` issues
You may encounter an issue that says `segmentation fault (pygame parachute error)` or similar. It is because
that the newest version of `pygame` > 2.0 does not seem compatible with the Joystick class we use for the DPEA. To fix
this, instead use an older version of `pygame==1.9.6`. To install this older version type the following into your

## Running the App
Ensure you are using a python interpreter with Kivy installed, navigate to the JoystickApp folder, and run the following
in your terminal --
```
python3 joystick_example.py
```