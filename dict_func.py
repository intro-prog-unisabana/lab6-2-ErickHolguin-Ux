# Write your code here!
def employee_print(employee_info):

    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")
    
    #reabre el diccionario con nuevos datos sin afectar los originales
    remaining_info = dict(employee_info)
    remaining_info.pop("Name", None)
    remaining_info.pop("Salary", None)
    remaining_info.pop("Role", None)

    if remaining_info:
        for key, value in remaining_info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")