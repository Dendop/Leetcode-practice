import sys
import re

def add_time(start, duration, day_opt=None):
    #Extract start values
    start_s = start.split()
    extract_start = start_s[0].split(':')
    start_hours, start_minutes = int(extract_start[0]), int(extract_start[1])
    #start_s[1] is AM or PM
    
    if start_s[1] == "PM":
        start_hours += 12
    
    #Extract duration values
    duration_s = duration.split(':')
    duration_hours, duration_minutes = int(duration_s[0]), int(duration_s[1])
    
    total_minutes = 0
    total_hours = 0
    total_days = 0
    
    #if duration value is big calculation
    while duration_hours >= 24:
        duration_hours -= 24
        total_days += 1
    
    #Calc minutes
    total_minutes = start_minutes + duration_minutes
    if total_minutes >= 60:
        total_hours += 1
        total_minutes -=60
        
    #if start hours is already high
    if start_hours >= 24:
        start_hours -=24
        total_days += 1
    
    #Calc hours
    total_hours = total_hours + start_hours + duration_hours #I had to fix this one, bc 11:43 PM + 24:20 was 23:3 output
    if total_hours > 24:
        total_days += 1
        total_hours -= 24
    
    
    
    
    print(f"{total_hours}:{total_minutes}  ({total_days} days later)")
    

def main():
    add_time("10:10 PM", "3:30")
    
    
if __name__ == "__main__":
    main()