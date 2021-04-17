total_days = 0
total_distance_travelled = 0

while total_distance_travelled <= 100:
    day_distance_travelled = int(input("Enter the distance travlled for the day: "))
    total_distance_travelled = total_distance_travelled + day_distance_travelled
    total_days = total_days + 1
    
print("It took", str(total_days), "days to surpass 100km driven.")
print("The average distance driven per day is", total_distance_travelled/total_days, "km")