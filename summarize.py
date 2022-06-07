import pandas as pd

"""
1. create 4 new cols for total count of s201, s202, s101, s102, s103
"""

def summarize():
    longfile = 'output/features.csv'
    df = pd.read_csv(longfile)

    output = pd.DataFrame(columns = ["Subject ID", "S201", "S202", "S102", "S101", "S103"])
    currSubject = 2
    S201 = 0
    S202 = 0
    S101 = 0
    S102 = 0
    S103 = 0;

    for i in range(len(df)):
        #print(row)
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



