#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    """Return time object as a formatted string"""
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"


def time_to_sec(time):
    """Convert a time object to total seconds since midnight"""
    return time.hour * 3600 + time.minute * 60 + time.second


def sec_to_time(seconds):
    """Convert seconds since midnight to a time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def sum_times(t1, t2):
    """Add two time objects using seconds conversion."""
    seconds_sum = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(seconds_sum)


def valid_time(t):
    """Check validity of time object attributes."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True


def change_time(time, seconds):
    """Modify time by adding or subtracting seconds."""
    total_seconds = time_to_sec(time) + seconds
    total_seconds %= 86400  # Ensure within 24-hour range
    if total_seconds < 0:
        total_seconds += 86400
    updated_time = sec_to_time(total_seconds)
    time.hour = updated_time.hour
    time.minute = updated_time.minute
    time.second = updated_time.second

