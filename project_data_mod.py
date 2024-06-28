import pandas as pd
import project_data_mod as pdm

def run_accounting():
        while True:
            print('\nRetail business profile')
            print('1. total_sales')
            print('2. workers salary')
            print('3. profit')
            print('4. total tips')
            print('5. Exit')


            choice = input('Enter your choice (1-5): ')
            if choice == '1':
                total_sales()
            elif choice == '2':
                workers_salary()
            elif choice == '3':
                profit()
            elif choice == '4':
                total_tips()
            elif choice == '5':
                break
            else:
                print('Invalid choice. please enter a number between 1 and 5.')


# morning sales function
def morning_shift_sales():
    # n is the size of the list
    n = int(input("Enter the size of morning_shift_sales(4): "))
 
    # Using list comprehension with input to prompt the user for the morning shift sales
    # split funct split the numbers separately using white space as the delimeter
    morning_shift_sales = list(int(x) for x in input("Enter morning_shift_sales: " ).strip().split())[:n]
    return morning_shift_sales


# Evening sales function
def evening_shift_sales():
    # n is the size of the list
    n = int(input("Enter the size of evening_shift_sales(4): "))
 
    # Using list comprehension with input to prompt the user for the evening shift sales
    # split funct split the numbers separately using white space as the delimeter
    evening_shift_sales = list(int(x) for x in input("Enter evening_shift_sales: " ).strip().split())[:n]
    return evening_shift_sales


# total sales function
def total_sales():
    
        # Validate input lengths
    if len(morning_shift_sales()) != len(evening_shift_sales()):
        print("Error: Input lengths do not match.")
        return
    
    total_sales_data = [x + y for x,y in zip (morning_shift_sales(),evening_shift_sales())]
    print('\n')
    print(f'total_sales: {total_sales_data}')
    return total_sales_data


# profit function
def profit():
     # n is the size of the list
    n = int(input("Enter the size of the cost of item(4): "))
 
     # Using list comprehension with input to prompt the user for the cost of item
     # split funct split the numbers separately using white space as the delimeter
    cost_of_item = list(int(y) for y in input("Enter cost of item: " ).strip().split())[:n]
    
    total_sales_data = total_sales()
    
      # Validate input lengths
    if len(cost_of_item) != len(total_sales_data):
        print("Error: Input lengths do not match.")
        return
    
    profit_loss_list = [x - y for x,y in zip(total_sales_data,cost_of_item)]
    print('\n')
    print(f'profit/loss: {profit_loss_list}')


# worker's salary function
def workers_salary():
    try:
         # prompt the user for hourly_rate & hours_eorned
     
         # n is the size of the list
        n = int(input("Enter the size of the hourly rate list(4): "))
 
         # Using list comprehension with input to prompt the user for the hourly_rate
         # split funct split the numbers separately using white space as the delimeter
        hourly_rate = list(float(x) for x in input("Enter hourly rate: " ).strip().split())[:n]
                                           
         # a is the size of the list 
        a = int(input("Enter the size of the hours worked(4): "))
                                               
         # Using list comprehension with input to prompt the user for hours_worked
         # split funct split the numbers separately using white space as the delimeter 
        hours_worked = list(int(y) for y in input("Enter hours worked: ").strip().split())[:n]
        
             # Validate input lengths
        if len(hourly_rate) != len(hours_worked):
            print("Error: Input lengths do not match.")
            return
    
         # using list comprehension to calculate salary of each worker
         # the round function round the salary to 2 decimal place
        salary = [round(x,2) * round(y,2) for x,y in zip(hourly_rate,hours_worked)]
        print('\n')
        print(f'workers salary: {salary}')
    
    except ZeroDivisionError:
                print("Error: Cannot divide by zero")

            
# tips function for workers
def morning_tips():
     # using list comprehension to calculate morning tips of each worker                                           
    morning_tips = [0.02 * y for y in (morning_shift_sales())]
    return morning_tips

def evening_tips():   
     # using list comprehension to calculate evening tips of each worker                                           
    evening_tips = [0.02 * y for y in (evening_shift_sales())]
    return evening_tips


def total_tips():
    total_tips_data = [round(x,2) + round(y,2) for x,y in zip(morning_tips(),evening_tips())]
    print('\n')
    print(f'total tips: {total_tips_data}')
    
    
    Challenges Encountered

1. I had to surf the internet to first determine how to pass in input for a list of numbers which was my major challenge.
2. I had to define a function for the morning and evening shift sales so as to reuse it for the tips, I am not sure if there is a way of returning a variable and reusing it.
3. I was at having a value errors for my total tips, and profits but later solved it.