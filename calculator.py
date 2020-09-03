print(f'To calulate how many calories you will be burning at a speed of 6.0 mph,\nwe will need to know how much you weigh and the amount of miles you will be running')

user_weight_input = input(f'Please enter your weight in pounds. ')
user_miles_input = input(f'Please enter how many miles you plan on running. ')

user_weight = int(user_weight_input)
user_miles = int(user_miles_input)

user_permile_cal = user_weight * .75
user_end_cal = user_permile_cal * user_miles

print(
    f'Your final calorie burn if you were to run at 6.0mph for {user_miles} miles would be {user_end_cal}')
