import pyedflib
import pandas as pd
import os
from tqdm import tqdm

def export_psg_to_csv(edf_file_path, csv_file_path, channel_labels=None, overwrite=False, samples_wanted=None):

    #CSV file overwrite functionality
    if overwrite and os.path.exists(csv_file_path):
        os.remove(csv_file_path)
    elif not overwrite and os.path.exists(csv_file_path):
        raise FileExistsError(f"The file '{csv_file_path}' already exists")

    # Error handling for if edf does not exist
    if not os.path.exists(edf_file_path):
        raise FileNotFoundError(f"The EDF file '{edf_file_path}' does not exist.")

    # Open the EDF file
    with pyedflib.EdfReader(edf_file_path) as edf_file:

        # Get the indices and labels of the selected channels
        if channel_labels is None:
            channel_labels = edf_file.getSignalLabels()
        channel_indices = [edf_file.getSignalLabels().index(name) for name in channel_labels]

        # Calculate 'samples_increment' based on 'samples_wanted'
        total_samples = edf_file.getNSamples()[0]
        samples_wanted = total_samples if samples_wanted is None else samples_wanted
        samples_increment = max(1, total_samples // samples_wanted)

        # Create a DataFrame from the data list
        df = pd.DataFrame(columns=['Timestamp'] + channel_labels)

        #Compute data - stop value is 'total_samples - samples_increment + 1' to prevent potential extra sample
        for i in tqdm(range(0, total_samples - samples_increment + 1, samples_increment), desc="Exporting PSG Data", unit="row"):
            timestamp = edf_file.getSampleFrequency(channel_indices[0]) * i
            row_data = [timestamp] + [edf_file.readSignal(idx)[i] for idx in channel_indices]
            df.loc[i] = row_data

    # Write the data to the CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"PSG data has been exported to {csv_file_path}.")

# Driver Code
edf_file_path = 'data\DatabaseSubjects\subject2.edf'
csv_file_path = 'data\CSV_Data\subject2_data.csv'

export_psg_to_csv(edf_file_path, csv_file_path, samples_wanted=1200)
