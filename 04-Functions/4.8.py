def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    
    elif time_format == '12':
        period = "am" if hours < 12 else "pm"
        
        display_hour = hours % 12
        if display_hour == 0:
            display_hour = 12
        
        return f"{display_hour}:{minutes:02d}{period}"
    
    else:
        return "Invalid format"