import numpy as np
import pandas as pd
import fileinput
import os
import shutil

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
        if os.path.isfile("logfiles copy/Sub0"+digits+file_index+"/Intake/JJ0001_"+sub+"0"+digits+file_index+"_1-sternberg_block 1.log"):
            intake = "/Intake"
            print("yes")

        src1 = "logfiles copy/Sub0"+digits+file_index+intake+"/JJ0001_"+sub+"0"+digits+file_index+"_1-sternberg_block 1.log"
        src2 = "logfiles copy/Sub0"+digits+file_index+intake+"/JJ0001_"+sub+"0"+digits+file_index+"_1-sternberg_block 2.log"
        src3 = "logfiles copy/Sub0"+digits+file_index+intake+"/JJ0001_"+sub+"0"+digits+file_index+"_1-sternberg_block 3.log"

        dest1 = "new_logfiles/Sub"+file_index+"/sternberg_block_1.log"
        dest2 = "new_logfiles/Sub"+file_index+"/sternberg_block_2.log"
        dest3 = "new_logfiles/Sub"+file_index+"/sternberg_block_3.log"

        os.mkdir("new_logfiles/Sub"+file_index)

        shutil.move(src1, dest1)
        shutil.move(src2, dest2)
        shutil.move(src3, dest3)