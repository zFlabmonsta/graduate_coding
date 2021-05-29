# Peter Nguyen's solution - Technical Challenge

Programming Language: Python, JavaScript

Bonus: Along with the task, I also created a client-server application utilising the task's output

## Project setup
Here is what you need in your environment to run the thing:

I am running the application on a `Linux device`.

1. Install `python3.8`. Run this command in the terminal:
```
$ sudo apt install python3.8
```

2. Install Python package-management `pip3`. Run this command in the terminal:
```
$ sudo apt install python3-pip
```
3. Install `numpy`. Run this command in the terminal:
```
$ pip3 install numpy
```
4. Install `pandas`. Run this command in the terminal:
```
$ pip3 install pandas
```

## Running the solution

`cd` into `graduate-coding/solution` directory then,

Run this command to run the solution:
```
$ ./main.py
```

or

```
$ python3 main.py
```

or

```
python main.py
```

The solution will output a csv file `graduate-coding/solution/counted_users_by_state.csv`


## Output 
filename: `counted_users_by_state.csv`

Active users per state:

```
ACT,967
NSW,893
NT,986
QLD,922
SA,900
TAS,987
VIC,965
WA,930
```


## Thoughts on the problem

### Timeline of thoughts on the problem !!

Before starting on the task:
- Took the time to understand the problem deeper. At this point in time, the question/task given was quite vague to me and with little requirements
so, I started asking myself questions on what I wanted to do and what I needed to consider.

- Looking at the data, there are many ways I could approach this:
  - Utilising Postcode to identify state
  - Extract the state's acronyms from the address
  - Possibly use a geographic location library to pin point which state/location

- Further understanding how address and postcode works in Australia, these addresses from dataset will not allow me to pinpoint a location or utilise Australia's
postcode system to identify the state of its address as they were inconsistent and did not adhere to the postcode system in Australia. For example, NSW's postcode format is
2xxx, while some of the data in the dataset contains 2xxx postcode format in other states, which leaves me to only extracting the acronyms from the address as the best option.

- I started thinking about if the program/system I was going to design needed any implementation for other countries and state outside of Australia. Do I need to future proof this program by designing it in a way that it is modular?

- I was able to come up with two ways of going by it:
  1. Utilising Pandas and Numpy (showcase less problem solving but follow KISS)
  2. Utilising Data Structures (showcase more problem solving but more complex)

- I was in a bit of a dilemma deciding whether to take option 1 (KISS) or 2(Complex but showcases problem solving skills) - one solution made it more simple than the other but showcases less of problem solving skills. I enquired Dean that I may have two solutions and asked him what should I do. Do I provide both solutions? Do I pick what I think is best solution? He suggested if possible to provide both solution. If not come up with one solution and provide pros and cons for both. 

- Thinking... Thinking... So far, I have considered duplicate data and missing data, as data itself can be very noisy and dirty, with my possible solutions. Do I need to do data cleansing? I wasn't too sure.
- And also the question/task was still a bit ambiguous to me as the example solution output counted active users, but the task didn't mention or require anything about it.

- I emailed Dean once again to ask about whether or not I needed to cleanse the data and do I consider only active members? And I'm glad I asked because his answers allowed me to finally direct myself to where I needed to go to come up with a solution. Dean answers:
  1. No need to perform data cleansing
  2. Only report on active members

- Ok, with Dean's help and now having a direction that I can work towards, I no longer need to consider using "Data Structure" solution as a lot of complexity are removed and can really focus on KISS and getting the requirements and solution done. No longer do I need to:
  - Consider states outside of the country
  - Cleanse data (remove duplicates, missing data)
both of which would have added lots of complexity to my solutions.

### Lets start implementing !!!

- 3 core things I need to do:
  1. Open and convert JSON into Data Frame
  2. Solve the problem
  3. Output CSV

More comments and also thought process outlined in `main.py`

Assumptions:
  - No need to cleanse data so I assumed that the data format is consistent throughout the dataset

### How did I get the state of the address ?

Given that the address is a consistent format, and consider this address from data as an example:
```
"address": "3 Kennedy Elbow\nHancockfurt, SA, 2898",
```
I was able to extract the acronym of the states of the address by turning the string into an array where the `,` in the string act as the delimiter i.e. the above example turn into:
```
address = ["3 Kennedy Elbow\nHancockfurt", " SA", "2898"]
```

Since the data is assumed consistent, I also assumed that the acronym of the state also sits on the same index for every data in the set. This means that I can extract the state by just
referencing to the index `address[1]`

There were still white spaces in the string:
```
" SA"
```
I removed all white spaces to keep the value of string consistent throughout the dataframe
```
"SA"
```

### If data cleansing was required / we could improve
Datasets are dirty and noisy. With the data given to us, the format of the address it's in can be inconsistent if the address was not input properly. Thus, possibly making our solution not viable with inconsistent data and would require some cleansing before doing any sort of computation. The structure of the given data could be improved by breaking the address down further into `meta-data`. i.e:
```
# From this
[
  {
    "address": "3 Kennedy Elbow\nHancockfurt, SA, 2898",
    "firstName": "Shannon",
    "active": false,
    "lastName": "Robertson",
    "id": 0
  }
]
# To this
[
  {
    "address": {
      "number": "3" ,
      "street": "Kennedy Elbow\nHancockfurt",
      "state": "SA",
      "postcode: "2898"
    },
    "firstName": "Shannon",
    "active": false,
    "lastName": "Robertson",
    "id": 0
  },
]
```
This will allow the structure of the address to be more consistent which would make it easier to process and retrieve, and also allowing me to use the solutions I have previously mentioned.

### Other possible solutions

Other solutions that came in mind that doesn't require `pandas`, `numpy` detailed in pseudocode below:

This solution in psuedocode:
  - uses an array to keep track of counts of each state
```python
import json
import csv
# first we initialise the counts of each state as a track keeper
states = ['NSW', 'ACT', 'VIC', 'SA', 'WA', 'NT', 'TAS', 'QLD']
# each count index corresponds to the state array index i.e. count[0] belongs to 'NSW', which is states[0]
count = [0, 0, 0, 0, 0, 0, 0, 0]

# The members.json file needs to open so that the json library can convert json into python dictionary
with open('members.json') as f:
  data = json.load(f)

# iterate through each line of data file
for line in data:
  # extract state from address by splitting the address('string') with a ',' delimiter
  get_state = line['address'].split(',')
  # if it is an active users
  if (line['active'] == True):
    # increment the count of the state
    # we need to find the index of the state
    i = 0
    for j in state:
      # if the states index value equals to extracted state from json then increment the count of the state otherwise continue and increment i
      if j == get_state:
        counts[i] += 1
        # exit loop to optimise instead of continuing for no particular reason
        break
      else:
        i += 1

# now that we have the counted data for each state, we need to write it to a csv file
with open('counted_users_by_state.csv') as csv_file:
  csv_reader = csv.reader(csv_file)
  num_state = 0
  # iterate through states and count to print result into csv file
  for row in csv_reader:
    print(states[num_state] + ', ' + count[num_state])
    # increment num_state to go to next state/index
    num_state += 1
```

The above solution can be improved by using a dictionary as a track keeper instead of arrays. This makes accessing data instant rather than iterating through to get the state.
```python
import json
import csv
# first we initialise the counts of each state as a track keeper using dictionary
state_counts = {
  'NSW': 0, 
  'ACT': 0,
  'VIC': 0,
  'SA': 0,
  'WA': 0,
  'NT': 0,
  'TAS': 0,
  'QLD': 0
}


# The members.json file needs to open so that the json library can convert json into python dictionary
with open('members.json') as f:
  data = json.load(f)

# iterate through each line of data file
for line in data:
  # extract state from address by splitting the address('string') with a ',' delimiter
  get_state = line['address'].split(',')
  # if it is an active users
  if (line['active'] == True):
    # increment the count of the state
    state[get_state] += 1

# now we have the counted data for each state we need to write it to a csv file
with open('counted_users_by_state.csv') as csv_file:
  csv_reader = csv.reader(csv_file)
  num_state = 0
  # iterate through states and count to print result into csv file
  for row in csv_reader:
    print(states[num_state] + ', ' + count[num_state])
    # increment num_state to go to next state/index
    num_state += 1
```

### Opinion on the task
The task was simple and I believe any person that has experience in computer science is capable of coming with a solution to this task. However, simple is a trick, there will be many solutions but not all works and are correct. The hard part of a simple task is to make sure requirements are met and going towards the right direction as it is important to ensure that we provide the correct outcome for stakeholders. In this case, the requirement for active users were not mentioned making the task ambiguous and by asking Dean about it I was then able to correctly approach designing my solution.

## Creating a friendly interface for users to download csv file
Just having a bit more fun with myself! I created a super simple web-interface to allow clients to download the csv file and see the table over the browser. Not everyone knows how to use a terminal and run commands )=.

Used:
- JavaScript
- HTML
- Flask
- Python
- JQuery

#### Server Side
The server-side provides API endpoints for users to use. I kept it simple! There are two API end-points:
1. Provides client with a json consisting of counted active users in each state
2. Allows client to download csv file
Each time the API is invoked, the server will compute the problem domain and generate a new csv file based on the data, so in the future if the original `members.json` file gets updated the client will also receive the latest update.

#### Client Side
A simple `HTML` file that runs `AJAX` call to the API endpoints provided by the server.
The website provides an interface for users to:
1. See the latest counts of users per state
2. Download the csv file of the latest counts of users per state.

#### Running the server

Requirements:

1. Install `flask`
```
$ pip3 install flask
```

2. Install `flask_cors`
```
$ pip3 install flask_cors
```

To run the server, `cd` into `graduate-coding/solution/server-side` directory and the following command:
```
$ python3 run.py
```

To open the webpage, `cd` into `graduate-coding/solution/client-side` directory and open `index.html`

When you press on the button to invoke and action, you will see a response from the server (terminal) which means that the client communicated with the server and the server is spitting a response back with the content the client required. 

You can checkout these endpoints by entering the following url into the browser with the server is running, API endpoints:
- http://127.0.0.1:5000/api/csv/
- http://127.0.0.1:5000/api/file/


## References
If you found cool things on the internet that helped you (yes, this is not a closed book test) then throw them here for our reference!

- Pandas: 
  - [pandas doc](https://pandas.pydata.org/docs/)
  - [pandas read json](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)
  - [pandas drop df](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)
  - [pandas reset index in df](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.reset_index.html)
  - [pandas groupby dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)
  - [how to replace values in df with a condtion](https://www.kite.com/python/answers/how-to-replace-values-in-a-pandas-dataframe-that-satisfy-a-condition-in-python#:~:text=Use%20syntax%20pandas.,the%20rows%20satisfying%20the%20condition)
  - [drop a row based on a condition in df](https://www.geeksforgeeks.org/drop-rows-from-the-dataframe-based-on-certain-condition-applied-on-a-column/)
  - [iterating through df](https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/)
  - [renaming pandas dataframe](https://note.nkmk.me/en/python-pandas-dataframe-rename/#:~:text=You%20can%20use%20the%20rename,change%20column%20%2F%20index%20name%20individually.&text=Specify%20the%20original%20name%20and,index%20is%20for%20index%20name.)

- csv
  - [convert csv to python dict](https://stackoverflow.com/questions/14091387/creating-a-dictionary-from-a-csv-file)

- json
  - [convert python dict to json object](https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/)

- AJAX
  - [AJAX methods](https://www.w3schools.com/jquery/jquery_ref_ajax.asp)

- flask
  - [Flask doco](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  - [Flask API help](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
