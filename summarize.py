import pandas as pd

"""
1. create 4 new cols for total count of s201, s202, s101, s102, s103
"""

def summarize():
    #reads in the summary csv file and converts to dataframe
    longfile = 'output/features.csv'
    df = pd.read_csv(longfile)

    #sets cols of the output dataframe
    output = pd.DataFrame(columns = ["Subject ID", "S201", "S202", "S102", "S101", "S103"])

    #initializes needed variables such as the subject being looked at and the number of times each type of response happens for a subject
    currSubject = 2
    S201 = 0
    S202 = 0
    S101 = 0
    S102 = 0
    S103 = 0;

    #iterates through the dataframe
    for i in range(len(df)):

        #checks if the subject in the row changes, and then resets all variables, keeping new tally for new subject
        if df.loc[i, 'Subject ID'] != currSubject:
            print(S201)
            output = output.append({'Subject ID': currSubject, 'S201': S201, 'S202': S202, 'S102': S102, 'S101': S101, 'S103': S103},
                          ignore_index=True)
            S201 = 0
            S202 = 0
            S101 = 0
            S102 = 0
            S103 = 0
            currSubject += 1;

        #increments response variable if this is the response given in a row in the dataframe
        if df.loc[i, 'Response'] == "S201":
            S201 += 1
        elif df.loc[i, 'Response'] == "S202":
            S202 += 1
        elif df.loc[i, 'Response'] == "S101":
            S101 += 1
        elif df.loc[i, 'Response'] == "S102":
            S102 += 1
        elif df.loc[i, 'Response'] == "S103":
            S103 += 1

    print(output)

    output.to_csv('output/trial_responses.csv')



