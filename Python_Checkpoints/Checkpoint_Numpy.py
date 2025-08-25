""" Create a numpy array called "grades" that contains the following grades: [85, 90, 88, 92, 95, 80, 75, 98, 89, 83]

Import the numpy library and create the "grades" array as specified above.
Use numpy functions to calculate the mean, median, and standard deviation of the grades.
Use numpy function to find the maximum and minimum of the grades.
Use numpy function to sort the grades in ascending order.
Use numpy function to find the index of the highest grade in the array.
Use numpy function to count the number of students who scored above 90.
Use numpy function to calculate the percentage of students who scored above 90.
Use numpy function to calculate the percentage of students who scored below 75.
Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
Create a new array called "passing_grades" that contains all the grades above 75.
Print the result of all the above steps.
Note:

to calculate percentage use numpy.mean(grades > 90) * 100
to extract the grades above 90 use grades[grades > 90]
to extract the grades above 75 use grades[grades > 75]
You can use other numpy functions as well to analyze the data as you want. The above steps are just examples of what can be done. """

import numpy as np

Grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

print(f"The mean:{np.mean(Grades)}, The median:{np.median(Grades)}, The Standard deviation:{np.std(Grades):.2f}\
    The minimum:{np.min(Grades)}, The maximum:{np.max(Grades)}\nThe Ascending sort:{np.sort(Grades)}\nThe highest grade:{np.argmax(Grades)}\nThe number of student that scored above 90: {np.sum(Grades>90)}\nThe percentage of student that scored above 90: {np.mean(Grades>90)*100}%\nThe percentage of student that scored below 75: {np.mean(Grades<75)*100}%")
high_performers = Grades[Grades>90] 
print(high_performers)
passing_grades = Grades[Grades<75]
print(passing_grades)
