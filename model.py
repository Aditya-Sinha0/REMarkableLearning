import pyedflib
import pandas as pd
import numpy as np
import os
from tqdm import tqdm

def export_psg_to_csv(edf_file_path, csv_file_path, channel_labels=None):

    if not os.path.exists(edf_file_path):
        raise FileNotFoundError(f"The EDF file '{edf_file_path}' does not exist.")

    edf_file = pyedflib.EdfReader(edf_file_path)

    # Get the indices and labels of the selected channels
    if channel_labels == None:
        channel_labels = edf_file.getSignalLabels()
    channel_indices = [edf_file.getSignalLabels().index(name) for name in channel_labels]

    total_samples = edf_file.getNSamples()[0]

    # Calculate all timestamps at once using NumPy
    timestamps = np.arange(total_samples) * edf_file.getSampleFrequency(channel_indices[0])

    # Prepare an empty array to store the channel data
    channel_data = np.empty((total_samples, len(channel_indices)), dtype=float)

    # Use tqdm to show progress bar
    for i in tqdm(range(0, total_samples, 1000), desc="Exporting PSG Data", unit=" row"):
        channel_data[i] = [edf_file.readSignal(idx)[i] for idx in channel_indices]

    edf_file.close()

    # Create the DataFrame with timestamps and channel data
    df_data = np.column_stack((timestamps, channel_data))
    df_columns = ['Timestamp'] + channel_labels
    df = pd.DataFrame(df_data, columns=df_columns)

    # Write the data to the CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"PSG data has been exported to {csv_file_path}.")

# Example usage:
edf_file_path = 'data\DatabaseSubjects\subject1.edf'
csv_file_path = 'data\CSV_Data\subject1_data.csv'

export_psg_to_csv(edf_file_path, csv_file_path, ['ECG', 'SAO2'])
