from pydantic import BaseModel # for declaring how model takes data as input

class Bankinputdata(BaseModel): # defining the input data model
    # Define the input fields based on your model's requirements
    Age: int
    Sex: int
    Job: int
    Housing: int
    Saving_accounts: int
    Checking_account: int
    Credit_amount: int
    Duration: int
    Purpose_car: int
    Purpose_domestic_appliances: int
    Purpose_education: int
    Purpose_furniture_equipment: int
    Purpose_radio_TV: int
    Purpose_repairs: int
    Purpose_vacation_others: int