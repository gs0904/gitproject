import numpy as np

hours_studied = np.array([5, 8, 3, 7, 6])
attendance = np.array([85, 92, 75, 88, 90])
previous_scores = np.array([68, 85, 55, 82, 72])
final_scores = np.array([70, 91, 58, 87, 76])

print("Hours Studied - Shape:", hours_studied.shape)
print("Hours Studied - Data type:", hours_studied.dtype)

print("Attendance - Shape:", attendance.shape)
print("Attendance - Data type:", attendance.dtype)

print("Previous Scores - Shape:", previous_scores.shape)
print("Previous Scores - Data type:", previous_scores.dtype)

print("Final Scores - Shape:", final_scores.shape)
print("Final Scores - Data type:", final_scores.dtype)

#Mean final score
print("\nMean final score:", np.mean(final_scores))

#Maximum and minimum
print("Maximum final score:", np.max(final_scores))
print("Minimum final score:", np.min(final_scores))

#Standard deviation
print("Standard deviation of final scores:", np.std(final_scores))

bonus_scores = final_scores + 5
print("Scores after adding bonus marks:", bonus_scores)

passed = final_scores >= 75
print("Boolean array:", passed)

print("Scores >= 75:", final_scores[passed])