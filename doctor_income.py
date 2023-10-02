# A doctor has a clinic where he serves his patients. The doctor's consultation fees are different for different groups of patients depending on their age. If the patient's age is below 17, fees is 200 INR. If the patient's age is between 17 and 40, fees is 400 INR. If patient's age is above 40, fees is 300 INR. Write a code to calculate earnings in a day for which one array/List of values representing age of patients visited on that day is passed as input.

# Note:
# Age should not be zero or less than zero or above 120
# Doctor consults a maximum of 20 patients a day
# Enter age value (press Enter without a value to stop):

# Example:
# Input
# 20 30 40 50 2 3 14
# Output
# Total Income: 2000 INR
# For any wrong input display INVALID INPUT

def get_list_of_ages():
    age = []
    for i in range(20):
        m = input()

        try:
            if m == "":
                break
            elif int(m) in range(0,120):
                age.append(int(m))
            else:
                print("INVALID INPUT")
                continue
        except ValueError:
            print("INVALID INPUT")
            continue

    return age


def calculate_fees(age_list):
    fees = 0

    for i in age_list:
        if i < 17:
            fees+=200
        elif i < 40:
            fees+=400
        else:
            fees+=300

    return fees


if __name__=='__main__':
    print('Enter ages of all the patients for the day:')

    ages_of_patients = get_list_of_ages()
    total_income = calculate_fees(age_list=ages_of_patients)

    print(f"Total Income: {total_income} INR")