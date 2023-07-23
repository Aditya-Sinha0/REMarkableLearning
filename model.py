import pyedflib
import csv
import pandas as pd
import os
from tqdm import tqdm

def export_psg_to_csv(edf_file_path, csv_file_path):
    if not os.path.exists(edf_file_path):
        raise FileNotFoundError(f"The EDF file '{edf_file_path}' does not exist.")

    edf_file = pyedflib.EdfReader(edf_file_path)

    # Get the indices and labels of the selected channels
    channel_labels = edf_file.getSignalLabels()
    channel_indices = [edf_file.getSignalLabels().index(name) for name in channel_labels]

    # Create an empty DataFrame
    df = pd.DataFrame(columns=['Timestamp'] + channel_labels)

    total_samples = edf_file.getNSamples()[0]

    # Use tqdm to show progress bar
    for i in tqdm(range(0, total_samples, 100000), desc="Exporting PSG Data", unit=" row"):
        timestamp = edf_file.getSampleFrequency(channel_indices[0]) * i
        row_data = [timestamp] + [edf_file.readSignal(idx)[i] for idx in channel_indices]
        df.loc[i] = row_data

    edf_file.close()

    # Write the data to the CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"PSG data has been exported to {csv_file_path}.")

# Example usage:
edf_file_path = 'data\DatabaseSubjects\subject1.edf'
csv_file_path = 'data\CSV_Data\subject1_data.csv'

export_psg_to_csv(edf_file_path, csv_file_path)
