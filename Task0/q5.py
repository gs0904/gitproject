import pandas as pd

df = pd.read_csv("data/student_performance.csv")

print("First five rows:")
print(df.head())

print("Number of rows and columns:")
print(df.shape)

print("Column names:")
print(df.columns)

print("Missing values:")
print(df.isnull().sum())

avg = df["Final_Score"].mean()
print("Average Final Score:", avg)

highest = df["Final_Score"].max()
top_student = df[df["Final_Score"] == highest]
print("Student with highest Final Score:")
print(top_student)

df["Improvement"] = df["Final_Score"] - df["Previous_Score"]
print("Data with Improvement column:")
print(df)

print("Students with attendance >= 80:")
print(df[df["Attendance"] >= 80])

df = df.sort_values(by="Final_Score", ascending=False)
print("Sorted by Final Score:")
print(df)

df.to_csv("data/processed_student_performance.csv", index=False)
print("Processed file saved successfully.")
