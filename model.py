import pandas as pd
import numpy as np
import os

def dat_to_csv(dat_file_path, num_channels, csv_file_path):

    if os.path.exists(csv_file_path):
        print("CSV file exists")
        return

    #Read file and load into np array
    data = np.fromfile(dat_file_path, dtype=np.float32)

    # Reshape data to a 2D array with correct  num of channels
    num_channels = 4
    num_samples = len(data) // num_channels
    data_reshaped = data.reshape(num_samples, num_channels)

    #Save data as CSV
    np.savetxt(csv_file_path, data_reshaped, delimiter=",", fmt="%.6f")
    print("CSV file created")



#DRIVERS

#test dat_to_csv
test_dat_file_path = "data\mit-bih-polysomnographic-database-1.0.0\slp01a.dat"
test_csv_file_path = "data\mit-BIH-csv\slp01a.csv"
dat_to_csv(test_dat_file_path, 4, test_csv_file_path)

