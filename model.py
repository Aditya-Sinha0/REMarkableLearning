import pyedflib
import csv
import pandas as pd
import numpy as np
import os

    
def export_psg_to_csv(edf_file_path, csv_file_path):
    
    #Error handling For If edf file does not exist
    if not os.path.exists(edf_file_path):
        raise FileNotFoundError(f"The EDF file '{edf_file_path}' does not exist.")

    edf_file = pyedflib.EdfReader(edf_file_path)

    # Get the indices and labels of the selected channels
    channel_labels = edf_file.getSignalLabels()
    channel_indices = [edf_file.getSignalLabels().index(name) for name in channel_labels]

    csv_data = []

    # Iterate through the signals and store the data in a list of lists
    for i in range(edf_file.getNSamples()[0]):
        timestamp = edf_file.getSampleFrequency(channel_indices[0]) * i
        row_data = [timestamp] + [edf_file.readSignal(idx)[i] for idx in channel_indices]
        csv_data.append(row_data)

    edf_file.close()

    # Write the data to the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Timestamp'] + channel_labels)  # Write header row
        csvwriter.writerows(csv_data)  # Write data rows

    print(f"PSG data has been exported to {csv_file_path}.")


# DRIVER
edf_file_path = 'data\DatabaseSubjects\subject1.edf'
csv_file_path = 'data\CSV_Data\subject1_data.csv'

export_psg_to_csv(edf_file_path, csv_file_path)