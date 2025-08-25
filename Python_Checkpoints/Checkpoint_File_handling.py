#First Solution
import numpy as np
Data_set = open("Loan_prediction_dataset.csv", "r")

data = np.genfromtxt(Data_set, delimiter=",", skip_header=1,dtype=float)
print(data)


Loan_Amount_= data[:,8]
Loan_Amount = Loan_Amount_[~np.isnan(Loan_Amount_)]
print(Loan_Amount)


print(f"📊 Loan Stats:")
print(f"Mean: {np.mean(Loan_Amount):.2f}")
print(f"Median: {np.median(Loan_Amount):.2f}")
print(f"Standard Deviation: {np.std(Loan_Amount):.2f}")
print(f"Min: {np.min(Loan_Amount):.2f}")
print(f"Max: {np.max(Loan_Amount):.2f}")

Data_set.close()

# Second Solution
import numpy as np
with open("Loan_prediction_dataset.csv","r") as Data_Set:
    Data = np.genfromtxt("Loan_prediction_dataset.csv", delimiter=",", skip_header=1,usecols=8)
    print(Data)
    Loan_Amount= Data[~np.isnan(Data)]
    print(f"📊 Loan Stats:")
    print(f"Mean: {np.mean(Loan_Amount):.2f}")
    print(f"Median: {np.median(Loan_Amount):.2f}")
    print(f"Standard Deviation: {np.std(Loan_Amount):.2f}")
    print(f"Min: {np.min(Loan_Amount):.2f}")
    print(f"Max: {np.max(Loan_Amount):.2f}")
