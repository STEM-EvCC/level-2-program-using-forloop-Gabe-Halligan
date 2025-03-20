mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = len(mission_names)

successful_missions = sum(mission_success)

success_rate = (successful_missions / total_missions) * 100

missions_before_2000 = [mission_names[i] for i in range(total_missions) if mission_years[i] <2000]

print(f"Total number of missions: {total_missions}")
print(f"Number of successful missions {successful_missions}")
print(f"Success rate: {success_rate: .2f}%")
print("Missions launched befoe the year 2000:")
for mission in missions_before_2000:
    print(f"-{mission}")