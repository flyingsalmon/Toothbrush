"""
Smart Toothbrush Firmware Simulation
------------------------------------

A Python simulation demonstrating how a smart electric toothbrush
can track brush-head usage, detect replacements, and restore usage
history when previously-used heads are reattached.

This project was created for educational purposes to illustrate
firmware design concepts such as:

- Device identification
- Usage counters
- Persistent storage concepts
- EEPROM/FRAM-style tracking
- Memory-constrained embedded systems

Although implemented in Python, production firmware would typically
be written in C/C++ for an embedded microcontroller.

Author: Tony Rahman
Website: https://flyingsalmon.net

Copyright (c) 2026 Tony Rahman
"""


class Toothbrush:
    def __init__(self, max_usage_limit=200):
        self.current_head_id = None
        self.usage_count = 0
        self.max_usage_limit = max_usage_limit
        self.head_history = {}  # stores usage_count per head_id

    def attach_head(self, head_id):
        # Save current head usage before switching
        if self.current_head_id is not None:
            self.head_history[self.current_head_id] = self.usage_count
            
        # Switch to new head
        self.current_head_id = head_id

        # Restore usage if head was seen before
        if head_id in self.head_history:
            self.usage_count = self.head_history[head_id]
            if self.usage_count >= self.max_usage_limit:
                return f"Head {head_id} ⚠WARNING: Expired!"
            return f"Head {head_id} attached."
        else:
            # First time ever
            self.usage_count = 0
            self.head_history[head_id] = 0
            return f"Head {head_id} attached for the first time."

    def record_usage(self):
        if self.current_head_id is None:
            return "Error: No head attached."

        self.usage_count += 1
        self.head_history[self.current_head_id] = self.usage_count

        if self.usage_count >= self.max_usage_limit:
            return f"Usage {self.usage_count}: ⛔ Replace toothbrush head!"
        else:
            return f"Usage {self.usage_count}: OK"

# ----------------------------------------------------------------------------------------------
# Simulations: Brush sessions per day --- once in morning, once in evening (each day = 2 usages)
# ----------------------------------------------------------------------------------------------

tb = Toothbrush(max_usage_limit=200)  # 200 usages = 100 days @ 2 uses/day

# Simulate attaching a brand new head
HEAD="111"
print(f"▶Scenario A: User attaches a new head for the first time. [max usage: {tb.max_usage_limit}X]\n")
print(tb.attach_head(HEAD))

days = 107  # simulate 107 days to show reminder

# each day -> user brushes twice = 2 usages. Call tb.record_usage() twice in each loop.
for day in range(1, days + 1):
    print(f"Day {day}")

    # Morning session
    print("  Morning:", tb.record_usage())

    # Evening session
    print("  Evening:", tb.record_usage())

    # Stop once reminder has triggered
    if tb.usage_count >= tb.max_usage_limit:
        break

###############

# Simulate reusing the same head (for another n days past replacement threshold)
days = 3
print(f"\n▶Scenario A.1: Using an expired head {HEAD} for another {days} days")
for day in range(1, days + 1): # for range, we need add 1 to the desired upper limit (exclusive upper limit)
    print(tb.attach_head(HEAD))
    # user brushes twice a day...
    # Morning session
    print("  Morning:", tb.record_usage())
    # Evening session
    print("  Evening:", tb.record_usage())


# Simulate replacing the head
HEAD = "123"
print("\n▶Scenario B: User replaces the head with a new one...")
print(tb.attach_head(HEAD))

# One more brushing session (1 day: morning and evening) with new head
print("\nAfter replacement:", tb.record_usage())

# and brush for another n days (using the new head)
days = 5
for day in range(1, days + 1): 
    print(tb.attach_head(HEAD))
    # Morning session
    print("  Morning:", tb.record_usage())
    # Evening session
    print("  Evening:", tb.record_usage())


# Now simulate putting back an older/expired head
HEAD = "111"
print("\n▶ Scenario A.2: Reusing an expired head (removes an unexpired head and puts in a previously expired head)...")
print(tb.attach_head(HEAD))

# and user brushes with the older/expired head for another n days
days = 3
for day in range(1, days + 1): 
    print(tb.attach_head(HEAD))
    # Morning session
    print("  Morning:", tb.record_usage())
    # Evening session
    print("  Evening:", tb.record_usage())


# User puts back the correct head (not brand new, but not expired) 
HEAD = "123"
print("\n▶ Scenario B.1: Reusing an older head (but not expired)...")
print(tb.attach_head(HEAD))

# and brushes with the correct head (not brand new, but not expired) for n days
days = 2 # each day = 2 usages (morning, event)
for day in range(1, days + 1): # for range, we need add 1 to the desired upper limit (exclusive upper limit)
    print(tb.attach_head(HEAD))
    # Morning session
    print("  Morning:", tb.record_usage())
    # Evening session
    print("  Evening:", tb.record_usage())



# Simulate attaching a brand new head
HEAD="999"
print(f"▶Scenario C: User attaches a brand new head. [max usage: {tb.max_usage_limit}X]\n")
print(tb.attach_head(HEAD))

# and brushes with the brand new head for another n days
days = 1
for day in range(1, days + 1): 
    print(tb.attach_head(HEAD))
    # Morning session
    print("  Morning:", tb.record_usage())
    # Evening session
    print("  Evening:", tb.record_usage())


# print history to show which head IDs were used so far
print("\n➡ Brush head history (ID:Usage):", tb.head_history)

# output should show: {'111': 212, '123': 15, '999': 2}
