#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    """Return time object (t) as a formatted string"""
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"


def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    result = Time(0, 0, 0)
    result.hour = t1.hour + t2.hour
    result.minute = t1.minute + t2.minute
    result.second = t1.second + t2.second

    # Normalize seconds to minutes
    while result.second >= 60:
        result.second -= 60
        result.minute += 1

    # Normalize minutes to hours
    while result.minute >= 60:
        result.minute -= 60
        result.hour += 1

    # Normalize hours to 24-hour format
    while result.hour >= 24:
        result.hour -= 24

    return result


def valid_time(t):
    """Check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True


def change_time(time, seconds):
    """Modify the time object by adding or subtracting seconds."""
    time.second += seconds

    # Normalize seconds to minutes
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    # Normalize minutes to hours
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    # Normalize hours to 24-hour format
    while time.hour < 0:
        time.hour += 24

    while time.hour >= 24:
        time.hour -= 24

    return None
