from time import time
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


def summarize2():
    output = pd.DataFrame(columns = ["Subject ID", "S201", "S202", "S102", "S101", "S103", "Total Trials"])

    for i in range(59):
        S201 = 0
        S202 = 0
        S101 = 0
        S102 = 0
        S103 = 0
        sub_index = str(i + 2)
        for j in range(3):
            list = []
            #print(str(i+2))
            file_index = str(j + 1)
            f = open('new_logfiles/Sub' + sub_index + '/sternberg_block_' + file_index + '.log')
            line = f.readline()
            #line = line.strip()
            line_index = 0
            while line:
                line = line.strip()
                if 'JJ' in line or "sub" in line or "003_1" in line or (sub_index == "53" and file_index == "2" and line_index >= 5 and line_index <= 309):
                    try:
                        list.append(line)
                    except ValueError:
                        print('Error in line :' + line )
                line = f.readline()
                line_index += 1

            for i in range(len(list) - 1):
                if("Response" in list[i] and "Sound" in list[i+1]):
                    response = list[i][list[i].find('Response') + 9:list[i].find('Response') + 12]
                    if response == "201":
                        S201+=1
                    elif response == "202":
                        S202+=1
                    elif response == "101":
                        S101+=1
                    elif response == "102":
                        S102+=1
                if "Sound" in list[i+1] and "timeout" in list[i+1]:
                    S103+=1
                    
        output = output.append({'Subject ID': sub_index, 'S201': S201, 'S202': S202, 'S102': S102, 'S101': S101, 'S103': S103, 'Total Trials': S201 + S202 + S101+ S102 + S103},
                          ignore_index=True)
    #output.to_csv('output/updated_trial_responses.csv')
    print(output)

    """
    df = pd.DataFrame([sub.split(" ") for sub in list])
    df.columns = ['Subject', 'Trial', 'Event Type', 'Code', 'Time',	'TTime', 'Uncertainty Duration'	'Uncertainty', 'ReqTime', 'ReqDur']
    print(df)
    """
    #print(list[16][list[16].find('Response') + 13])
    #print(list[16])


def summarize3():
    output = pd.DataFrame(columns = ["Subject ID", "Trial Number", "Response Type", "Number of Letters", "Position of Probed Letter", "Probe Start Time", "Probe End Time", "Response Time"])
    response = ""
    for i in range(59):
        sub_index = str(i + 2)
        trial_number = 1
        for j in range(3):
            list = []
            trialList = []
            file_index = str(j + 1)
            f = open('new_logfiles/Sub' + sub_index + '/sternberg_block_' + file_index + '.log')
            line = f.readline()
            line_index = 0
            while line:
                #line = line.strip()
                if 'JJ' in line or "sub" in line or "003_1" in line or (sub_index == "53" and file_index == "2" and line_index >= 5 and line_index <= 309):
                    try:
                        list.append(line)
                    except ValueError:
                        print('Error in line :' + line )
                line = f.readline()
                line_index += 1
            
            for i in range(len(list) - 1):
                if "Sound" in list[i+1] and "timeout" in list[i+1]:
                    response = "S103"
                    #print(trialList)
                    output = output.append({"Subject ID": sub_index, "Trial Number" :trial_number, "Response Type" :response, "Number of Letters" :None, "Position of Probed Letter" :None, "Probe Start Time": None, "Probe End Time": None, "Response Time" :None}, ignore_index=True)
                    trial_number += 1
                    trialList.clear()
                elif "Picture" in list[i]:
                    try:
                        trialList.append(str(list[i][list[i].find('Picture') + 8:list[i].find('Picture') + 9]))
                    except ValueError:
                        print('Error in line :' + line )
                elif("Response" in list[i] and "Sound" in list[i+1]):
                    response = "S" + list[i][list[i].find('Response') + 9:list[i].find('Response') + 12]
                    trialList.remove("+")
                    numletters = len(trialList) - 1
                    if response == "S101" or response == "S202":
                        posofprobe = trialList.index(trialList[len(trialList) - 1]) + 1
                        try:
                            time_index = list[i-(numletters - posofprobe + 1)].find('Picture') + 10
                            #print(sub_index, file_index, i)
                            probed_start_time = int(list[i - (numletters - posofprobe + 1)][time_index: list[i - (numletters - posofprobe + 1)].find('\t', time_index)])
                            probed_end_time = probed_start_time + 200
                        except:
                            probed_start_time = None
                            probed_end_time = None
                    else:
                        posofprobe = None
                        probed_start_time = None
                        probed_end_time = None
                    
                    time_index = list[i].find('Response') + 13
                    start_response = list[i][time_index: list[i].find('\t', time_index)]
                    #print(start_response)
                    time_index = list[i-1].find('Picture') + 10
                    start_probe = list[i - 1][time_index: list[i - 1].find('\t', time_index)]
                    #print(sub_index, file_index, i)
                    response_time = int(start_response) - int(start_probe)

                    output = output.append({"Subject ID" : sub_index, "Trial Number" : trial_number, "Response Type" : response, "Number of Letters" : numletters, "Position of Probed Letter" : posofprobe, "Probe Start Time": probed_start_time, "Probe End Time": probed_end_time, "Response Time" : response_time}, ignore_index=True)
                    trialList.clear()
                    trial_number += 1
                
    output.to_csv('output/trial_summaries.csv', index = False)
    #print(output)

    """
    df = pd.DataFrame([sub.split(" ") for sub in list])
    df.columns = ['Subject', 'Trial', 'Event Type', 'Code', 'Time',	'TTime', 'Uncertainty Duration'	'Uncertainty', 'ReqTime', 'ReqDur']
    print(df)
    """
    #print(list[16][list[16].find('Response') + 13])
    #print(list[16])



