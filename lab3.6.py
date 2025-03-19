for i in range(24):
    if i==0:
        print(f"12:00 midnight")
    elif i==12:
        print(f"12:00 noon")
    elif i<12:
        print(i,":AM")
    else:
        print(i-12,":PM")