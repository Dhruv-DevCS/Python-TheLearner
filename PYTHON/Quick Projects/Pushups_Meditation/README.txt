# Morning Ritual — Setup Guide

## What it does
A popup appears at every startup asking you to complete a quick habit
before you can use your PC:

- **10 Push-Ups** → Click and the window closes immediately (honor system 💪)
- **3-Minute Meditation** → A timer starts with a breathing guide and
  progress bar. Window closes automatically when the timer ends.

---

## Requirements
- Windows 10/11
- Python 3.x installed (https://www.python.org/downloads/)
  - `tkinter` is included with standard Python on Windows — no pip installs needed.

---

## Installation (3 steps)

### Step 1 — Save the script
Copy `morning_ritual.py` somewhere permanent, e.g.:
```
C:\Users\YourName\Documents\morning_ritual.py
```

### Step 2 — Edit the batch file
Open `morning_ritual_startup.bat` in Notepad.
Change the SCRIPT_PATH line if you saved the .py file somewhere other than Documents:
```
set SCRIPT_PATH=C:\Users\YourName\Documents\morning_ritual.py
```

### Step 3 — Add to Startup
1. Press **Win + R**
2. Type `shell:startup` and press Enter
3. Copy `morning_ritual_startup.bat` into the folder that opens

That's it! Restart your PC to test it.

---

## Customizing the meditation timer
Open `morning_ritual.py` in any text editor.
Find this line near the top:
```python
MEDITATION_SECONDS = 3 * 60  # 3 minutes
```
Change `3` to any number of minutes you want.

---

## Troubleshooting
- **Nothing happens on startup?**  
  Make sure Python is in your PATH. Open CMD and type `python --version`.  
  If it fails, reinstall Python and check "Add Python to PATH" during setup.

- **A black console window flashes?**  
  The batch file uses `pythonw` (windowless) — if you see a flash, it's just
  the batch file itself. This is harmless.

- **Want to test without restarting?**  
  Double-click `morning_ritual.py` directly, or run:  
  `python C:\Users\YourName\Documents\morning_ritual.py`
