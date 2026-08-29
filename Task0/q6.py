import pandas as pd
import matplotlib.pyplot as mat

df = pd.read_csv("data/processed_student_performance.csv")

#Bar chart
mat.figure(figsize=(14, 6)) 
mat.bar(df["Student"], df["Final_Score"]) 
mat.title("Student Final Scores") 
mat.xlabel("Student") 
mat.ylabel("Final Score") 
mat.xticks(rotation=90) 
mat.tight_layout() 
mat.savefig("plots/final_scores.png") 
mat.show()

#Scatter plot
mat.figure(figsize=(8, 6)) 
mat.scatter(df["Hours_Studied"], df["Final_Score"]) 
mat.title("Hours Studied vs Final Score") 
mat.xlabel("Hours Studied") 
mat.ylabel("Final Score") 
mat.tight_layout() 
mat.savefig("plots/study_vs_score.png") 
mat.show()

#Histogram
mat.figure(figsize=(8, 6)) 
mat.hist(df["Final_Score"], bins=10) 
mat.title("Distribution of Final Scores") 
mat.xlabel("Final Score") 
mat.ylabel("Number of Students") 
mat.tight_layout() 
mat.savefig("plots/score_distribution.png") 
mat.show()

#Custom graph
mat.figure(figsize=(8, 6)) 
mat.scatter(df["Attendance"], df["Final_Score"]) 
mat.title("Attendance vs Final Score") 
mat.xlabel("Attendance (%)") 
mat.ylabel("Final Score") 
mat.tight_layout() 
mat.savefig("plots/custom_plot.png") 
mat.show()
