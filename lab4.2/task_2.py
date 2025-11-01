import numpy as np

lengths_str = "15 22 10 8 12 25 18 30"
speeds_str = "60 50 70 40 55 65 45 75"
k = 3
p = 6

lengths = np.array(list(map(float, lengths_str.split())))
speeds = np.array(list(map(float, speeds_str.split())))

start_index = k - 1
end_index = p - 1

selected_lengths = lengths[start_index:end_index + 1]
total_length = np.sum(selected_lengths)

times = selected_lengths / speeds[start_index:end_index + 1]
total_time = np.sum(times)

average_speed = total_length / total_time

print(f"S = {total_length:.2f} км")
print(f"T = {total_time:.2f} часа")
print(f"V = {average_speed:.2f} км/ч")