import pandas as pd

data = {
        'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
        'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
        'Age': [30, 40, 25, 35, 45, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
        'Experience': [3, 7, 2, 5, 10, 4]
        }

employee_df = pd.DataFrame(data)

#Select the first 3 rows of the dataframe
selected_rows = employee_df.iloc[:3,:]


#Select all rows where the Department is "Marketing"
selected_Marketing = employee_df.loc[employee_df["Department"] == 'Marketing']
print(selected_Marketing)

#select the Age and Gender columns for the first 4 rows of the dataframe.
selected_4rows = employee_df.iloc[0:4,[2,3]]
print(selected_4rows)

# select the Salary and Experience columns for all rows where the Gender is "Male".
selected_male = employee_df.loc[employee_df["Gender"]== "Male", ["Salary","Experience"]]
print(selected_male)