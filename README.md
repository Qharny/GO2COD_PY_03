# Python Alarm Clock

## Description

This is a simple command-line alarm clock application built in Python. The program allows users to set an alarm time in 24-hour format, and it will sound an alert when the specified time is reached.

## Features

- Set alarm time in 24-hour format (HH:MM)
- Continuous beeping sound when alarm time is reached
- Ability to stop the alarm using Ctrl+C
- Simple and lightweight command-line interface

## Prerequisites

- Python 3.x
- Windows Operating System (due to use of `winsound` module)

## Dependencies

- `datetime` (built-in Python module)
- `time` (built-in Python module)
- `winsound` (Windows-specific module for sound generation)

## Installation

1. Ensure you have Python 3.x installed on your Windows machine
2. No additional installation of external libraries is required

## Usage

1. Run the script
2. Enter the desired alarm time in 24-hour format (e.g., 07:30)
3. The program will wait and alert you at the specified time
4. Press Ctrl+C to stop the alarm when it goes off

### Example

```
Set the alarm time (24-hour format, HH:MM): 
14:45
Alarm set for 14:45
Alarm is set. Press Ctrl+C at any time to stop the alarm.
```

## Limitations

- Currently only works on Windows due to `winsound` module
- Requires the script to be running continuously
- No support for multiple alarms or recurring alarms


## Author

Manasseh Kabutey Kwame

## Acknowlegement
# GO2COD