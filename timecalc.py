import sys


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
    if total_hours >= 24:
        total_hours -= 24
        total_days += 1
    
    #Optional day parameter handle
    if day_opt is not None:
        day_style = day_opt.lower() #tuesday
        week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        new_day_index = (week.index(day_style) + total_days) % 7
        new_day = week[new_day_index]
        
        #AM handle
        if total_hours < 12:
            if total_days == 1:
                print(f"{total_hours}:{total_minutes:02d} AM, {new_day.title()} (next day)")
            else:
                print(f"{total_hours}:{total_minutes:02d} AM, {new_day.title()} ({total_days} days later)")
        
    
        #Midnight handle
        elif total_hours == 0:
            total_hours = 12
            if total_days == 1:
                print(f"{total_hours}:{total_minutes:02d} AM, {new_day.title()} (next day)")
            else:
                print(f"{total_hours}:{total_minutes:02d} AM, {new_day.title()} ({total_days} days later)")
        #PM handle   
        else:
            total_hours -= 12
            if total_days == 1:
                print(f"{total_hours}:{total_minutes:02d} PM, {new_day.title()} (next day)")
            else:
                print(f"{total_hours}:{total_minutes:02d} PM, {new_day.title()} ({total_days} days later)")
    
    else:
        # AM handle without optional parameter
        if total_hours < 12:
            if total_days == 0:
                print(f"{total_hours}:{total_minutes:02d} AM")
            elif total_days == 1:
                print(f"{total_hours}:{total_minutes:02d} AM, (next day)")
            else:
                print(f"{total_hours}:{total_minutes:02d} AM ({total_days} days later)")
    
    # Midnight handle
        if total_hours == 0:
            total_hours = 12
            if total_days == 0:
                print(f"{total_hours}:{total_minutes:02d} AM")
            elif total_days == 1:
                print(f"{total_hours}:{total_minutes:02d} AM (next day)")
            else:
                print(f"{total_hours}:{total_minutes:02d} AM ({total_days} days later)")
    
    # PM handle
        if total_hours > 12:
            total_hours -= 12
            if total_days == 0:
                print(f"{total_hours}:{total_minutes:02d} PM")
            elif total_days == 1:
                print(f"{total_hours}:{total_minutes:02d} PM (next day)")
            else:
                print(f"{total_hours}:{total_minutes:02d} PM ({total_days} days later)")
    
def main():
    add_time("8:16 PM", "466:02", "tUeSdAy")
    
    
if __name__ == "__main__":
    main()