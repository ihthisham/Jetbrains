# put your python code here
duration = abs(int(input()))
food_cost = abs(int(input())) * duration
flight_cost = abs(int(input())) * 2
hotel_fare = abs(int(input())) * (duration - 1)

total_amount = food_cost + flight_cost + hotel_fare

print(total_amount)
