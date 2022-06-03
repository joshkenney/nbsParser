import numpy as np
import pandas as pd
import fileinput
import os

def extractFeatures():
    features = pd.DataFrame(columns = ["Subject ID", "Trial Number", "Indicator", "Start Time", "End Time", "Response"])

    subject_number = 2
    total_index = 0

    for i in range(59):
        file_index = str(i + 2)
        intake = ""
        digits = "0"
        sub = ""
        if i+2>9:
            digits = ""
        if i+2>30:
            sub="Sub"
        if os.path.isfile("logfiles/Sub0"+digits+file_index+"/Intake/JJ0001_"+sub+"0"+digits+file_index+"_1-sternberg_block 1.log"):
            intake = "Intake/"

        ResponseMarker = False
        position = 0
        response = ""
        indicator = 0
        currString = ""
        trial_index = 0
        with open(
            "triggers/JJ0001_Sub0" + digits + file_index + "_Stern123_1_Raw Data.text",
            'r') as f:

            for line in f:
                currString += line
                if ResponseMarker is True and line.find("Position") != -1:
                    position = int(line[line.find("<Position>")+10:line.find("</Position>")])

                if line.find("S2") != -1 or line.find("S1") != -1:
                    ResponseMarker = True
                    if line.find("S201") != -1:
                        response = "S201"
                        indicator = 1
                    elif line.find("S101") != -1:
                        response = "S101"
                        indicator = 1
                    elif line.find("S102") != -1:
                        response = "S102"
                        indicator = 0
                    elif line.find("S202") != -1:
                        response = "S202"
                        indicator = 0


                if ResponseMarker is True and line.rfind("</Marker>") != -1:
                    #print("hi")
                    trial_index += 1
                    start_time = position - 10
                    end_time = position + 210
                    if indicator == 0:
                        start_time = None
                        end_time = None
                    #features.append({"Subject ID": [subject_number],
                                     #"Trial Number": [trial_index],
                                     #"Indicator": [indicator],
                                     #"Start Time": [start_time],
                                     #"End Time": [end_time],
                                     #"Response": response}, ignore_index=True)
                    features.loc[total_index] = [subject_number] + [trial_index] + [indicator] + [start_time] + [end_time] + [response]
                    total_index += 1
                    ResponseMarker = False
        subject_number += 1
        trial_index = 0


    print(features)
    features.to_csv("output/features.csv")




