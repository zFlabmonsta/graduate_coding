from flask import Flask, send_file
from flask_cors import CORS, cross_origin

# append directory for parent files
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from main import run_process as a # This function is from the original task to solve and generate a csv which provides the counted active users per state
import csv #import csv library
import json #import json library

app = Flask(__name__) # create flask object application, allowing the app to perform certain actions
app.config["DEBUG"] = True
CORS(app)

filename = '../counted_users_by_state.csv'

'''
This end point will provide a json of counted active users per state to the client 
'''
@app.route('/api/csv/', methods=['GET'])
def provide_data():
    # initialise a dictionary to contain csv data
    data = {}

    
    #update the csv_file by generating a new one in the server
    a()

    # open files and parse csv file, appending each line of the csv file to the dictionary, then closes the file
    file = open(filename)
    reader = csv.reader(file)
    for row in reader:
        key = row[0]
        data[key] = row[1]
    file.close()

    # convert dict to json
    json_object = json.dumps(data, indent=4)

    return json_object

'''
This end point will allow client to download the current csv file
'''
@app.route('/api/file/', methods=['GET'])
def download_file():
    #update the csv_file by generating a new one in the server
    a()
    return send_file(filename, as_attachment=True)

app.run() # runs the app