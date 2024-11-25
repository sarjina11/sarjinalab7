#!/usr/bin/env python3
# Student ID: skarki28

class Time:
    """Simple object type for time of the day."""
    
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a human-readable string for the Time object."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a machine-readable string for the Time object."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time object as a formatted string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two Time objects and return their sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Adjust time by a given number of seconds."""
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second
        return None

    def time_to_sec(self):
        """Convert Time object to seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    def valid_time(self):
        """Check if the Time object is valid."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert seconds to a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

