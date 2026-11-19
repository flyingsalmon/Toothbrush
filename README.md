# Toothbrush
## Smart Toothbrush Firmware Simulation
A Python simulation of a smart electric toothbrush that tracks brush-head usage and determines when a brush head should be replaced.
This project explores how embedded firmware might identify individual brush heads, persist usage counts, and restore history when previously used heads are reattached.
While the example is implemented in Python for readability and education, real-world consumer devices typically implement similar logic in C/C++ firmware running on memory-constrained microcontrollers.
Features
•	Tracks individual brush-head IDs
•	Maintains usage count per brush head
•	Detects first-time and previously-used heads
•	Simulates replacement reminders
•	Demonstrates concepts commonly found in embedded systems

## Example Scenarios
•	New brush head installation
•	Expired brush-head detection
•	Reusing an expired brush head
•	Switching between multiple brush heads
•	Restoring usage history


## Educational Topics
This simulation can be used to explore:
•	Embedded firmware design
•	Device identity tracking
•	Non-volatile storage concepts
•	EEPROM vs FRAM
•	Memory optimization
•	Python vs embedded C implementations

## Running
python toothbrush.py

##Read the full article: https://flyingsalmon.net/smart-toothbrush-firmware-design/

Author: Tony Rahman
##Website: https://flyingsalmon.net

This project is intended solely for educational and demonstration purposes.
