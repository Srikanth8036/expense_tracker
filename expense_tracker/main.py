import pandas as pd 
import datetime
import logging
import os 

logging.basicConfig(filename='logging.txt', level=logging.INFO)

def add_expense():
    l = []
    while True:
        category = input('Enter your category: ')
        description = input('Enter your description: ')
        amount = input('Enter the amount: ')
        l.append({
            'date': datetime.datetime.now().strftime('%B: %m %Y'),
            'Category': category,
            'Description': description,
            'Amount': amount
        })
        option = input('Do you want to add more items? (yes/no): ').strip().lower()
        if option == 'no':
            break


    df = pd.DataFrame(l)
    file_path = 'data/expense.csv'
    
    if not os.path.isfile(file_path):
        df.to_csv(file_path, mode='a',index=False, header=True)
    else:
        df.to_csv(file_path, mode='a',index=False, header=False)


def view_expenses():
    try:
        data = pd.read_csv('data/expense.csv')
        if data.empty:
            print('“No expenses found yet.”')
        else:
            print(data)
    except Exception as e:
        logging.info(f'error at read expenses func {e}')
        print('“No expenses found yet.”')

def search_by_category(user_input):
    try:
        data = pd.read_csv('data/expense.csv')
        filtered_data = data[data['Category'].str.lower() == user_input.lower()]
        filtered_data.loc[:,['Amount']] = pd.to_numeric(filtered_data['Amount'], errors='coerce')

        if filtered_data.empty:
            print(f'there is no expense on this category please check the catogory name--{user_input}')
        else:
            total_expense = filtered_data['Amount'].sum()
            print(filtered_data)
            print(f'Total expense for category "{user_input}": {total_expense}')
        
    except Exception as e:
        logging.info(f'error in search_by_category {e}')
        print('Error reading expenses:', e) 

def month_report(ask_date_format):
    try:
        df = pd.read_csv('data/expense.csv')
        date_df = df[df['date'].str.lower().str.split(':').str[0].str.strip() == ask_date_format.lower()]
        df_sum = date_df['Amount'].sum()
        print(f'monthly: {ask_date_format} is total expenses are {df_sum}')
    except Exception as e:
        logging.info(f'error in month report  is {e}')


def display_method():
    print('='*10)
    print('EXPENSE TRACKER CLI TOOL')
    print('='*10)
    user_input = input("""
                    1. Add Expense
                    2. View All Expenses
                    3. Search by Category
                    4. View Monthly Summary
                    5. Exit \n
    Choose the number from the above:- """ 
    )
    return user_input




def flow_func():
    i = 3
    while True:
        dis_func = display_method()
        if dis_func == str(1):
            add_expense()
            os.system('cls' if os.system == 'nt' else 'clear')
            print('Data addede successfully into the CSV.... thank you \u270c you can choose more from below')

        elif dis_func == str(2):
            view_expenses()
        elif dis_func == str(3):
            search_cat = input('Enter your Category ("food", "travel","entertanment")')
            search_by_category(search_cat)
        elif dis_func == str(4):
            month_report_input = input('Enter your month to get the total expense on month(oct,sep,...):- ')
            month_report(month_report_input)
        elif dis_func == str(5):
            print('see you next time...bye  \U0001F44B')
            break
        else:
            os.system('cls' if os.system == 'nt' else 'clear')
            print('invalid input please try again.... \u270c')
            i -= 1
            if i == 0:
                print('you lost the chances please try after some time')
                break
            print(f'you have {i} left')
            continue 
    


def main():
    flow_func()  


    
if __name__ == '__main__':
    main()
# import pandas as pd
# # data = pd.read_csv('data/expense.csv', index_col='Category')
# # data['monthly report'] = data['Amount']*2
# # # print(data.iloc[0])
# # # print(data)

# # print(data.iloc[3,:3])



# ask_name = 'October'
# df = pd.read_csv('data/expense.csv')
# date_df = df[df['date'].str.lower().str.split(':').str[0].str.strip() == ask_name.lower()]
# df_sum = date_df['Amount'].sum()
# print(f'monthly: {ask_name} is total expenses are {df_sum}')












