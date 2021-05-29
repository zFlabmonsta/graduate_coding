#! /usr/bin/python3
import numpy as np
import pandas as pd
import os


'''
Why am I using pandas and numpy? 

Pandas and Numpy allows me to convert the JSON files into DataFrame which is a 2D data structure with columns that can handle different types.
You can view the input data like a spreadsheet or SQL table. With pandas library I am able to use logic along while utilising function/methods 
that pandas provides to manipulate the data in way that allows problems to be solved. Pandas also has index optimalisation, vector operations, memory optimisation
and filter optimisation to gain optimal performance.
'''

'''
This function converts JSON file into DataFrame and returns it as a DataFrame by using the location of the JSON file as the input.
'''
def convert_JSON_df(file_location):
    # reads json file based on the input(location of the json file) then uses pandas API to generate a dataframe and returns it
    return pd.read_json(file_location)
    

'''
This function will breakdown the users address and calculate by counting how many users live in each state using the dataframe input then return the dataframe
of counted active users by each state
'''
def calculate_users_in_state(df):
    '''
    - To calculate and count the users in each state we should remove/drop any unecessary columns(id, firstname, lastname)
    - inplace as true will operate on the original dataframe (given df)
    - axis = 1 means that we working on the column not row
    '''
    # drop id column
    df.drop('id', inplace=True, axis=1)
    # drop firstName column
    df.drop('firstName', inplace=True, axis=1)
    #drop lastName column
    df.drop('lastName', inplace= True, axis=1)
    
    # remove all non-active users from the dataframe
    df = df[df['active'] == True].copy()
    #  reset the index
    df.reset_index(drop=True, inplace=True)

    '''
    - Every address follows the same format ([(num street suburb), (state), (postcode)])
    - We can breakdown the address into state only by turning the address into an array separated by commas then selecting the index of the array that
    contains the the state
    '''
    # rename the column 'address' to 'state'
    df.rename(columns={'address': 'state'}, inplace=True)

    # iterate through each row of column 'state' (previously address) to:
    for index, row in df.iterrows():
        # split the address into an array seperated by comma and remove white spaces
        row['state'] = row['state'].split(',')[1].replace(" ","")
        # replace current 'state' column value with new value of just the state of the address
        df.loc[df.index == index, 'state'] = row['state']
        
    '''
    - We now have a dataframe that contains all active users with the state that they live in
    - We can group and count the number of active users living in each state
    '''
    
    # group the state of the current dataframe and generate a new dataframe that contains the number of active users in each state
    counted_df = df.groupby(['state']).size()

    # display counted users on terminal
    print(counted_df.reset_index(name='users').to_string())

    return counted_df

# originally inside main, but separted to use for API calling!
def run_process():
  '''
  root(graduate-coding)
    |-./data
      |-members.json
    |-./scripts
    |-./solution
      |-./main.py
      |-counted_users_by_state.csv
  '''
  # get the path of current file
  file_path = os.path.dirname(os.path.realpath(__file__))
  # To get the location of 'members.json', we need to go back one directory, since 'main.py' is in solution then move into 'data' directory to find 'members.json'
  json_location = os.path.join(file_path, '../data/members.json')

  # convert JSON into datafram
  df = convert_JSON_df(json_location)

  # group active users per state into dataframe
  df = calculate_users_in_state(df)

  # Converts dataframe to csv file and outputs it into the same directory as this python file (main.py)
  df.to_csv('./counted_users_by_state.csv', header=False)


'''
This is the entry point of the program when the python interpreter runs the python program.
'''
if __name__ == "__main__":
  run_process()


