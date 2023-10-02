# # An Automobile Company An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). 
# A company manager wants to make the production of both types of vehicle according to the given data below: 
# 1st data, Total number of vehicle (two-wheeler + four-wheeler)=v 
# 2nd data, Total number of wheels = W 
# The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.

def calculate_vehicles(v: int, W: int):
    four_wheelers = int((W / 2) - v)
    two_wheelers = v - four_wheelers

    return two_wheelers, four_wheelers

if __name__=='__main__':
    total_vehicles = int(input('Enter Total number of Vehicles: '))
    total_wheels = int(input('Enter Total number of Wheels: '))

    result = calculate_vehicles(total_vehicles, total_wheels)

    print('Number of two-wheelers:', result[0])
    print('Number of four-wheelers:', result[1])