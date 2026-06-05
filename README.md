# Habit Tracker CLI

A command-line habit tracker written in Python that logs your daily habits and tracks your current streaks.

## What it does

The program runs in a loop and accepts three commands. Log saves which habits you completed today. Stats shows your current streak for each habit. Quit exits the program. All data is saved to a local JSON file so your streaks persist between sessions.

## How to use

Run the program with:

python habit_tracker.py

Then enter one of the following commands:

- log: records which habits you completed today
- stats: displays your current streak for each habit
- quit: exits the program

When logging, type your habits separated by spaces. For example: coding exercise reading

## Habits tracked

Coding, exercise, and reading. You can change these by editing the HABITS list at the top of the file.

## Requirements

Python 3. No external libraries needed, only json, os, and datetime from the standard library.

## Notes

Streaks are calculated by counting consecutive days ending from today. If you miss a day, the streak resets to zero. Data is stored in habits.json in the same directory as the script.
