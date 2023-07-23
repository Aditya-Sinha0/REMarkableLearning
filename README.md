#Dataset 
https://zenodo.org/record/2650142

# PSG Data Exporter

This repository contains a Python script (`export_psg_to_csv.py`) that allows you to export PSG (Polysomnography) data from an EDF file to a CSV file. PSG data is commonly used in sleep studies and consists of various physiological signals, such as EEG, EOG, EMG, etc.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.x
- pyEDFlib
- pandas
- numpy

You can install the required packages using pip:

pip install pyEDFlib pandas numpy


## Setup Git LFS

To ensure that you can properly work with large files, such as EDF files, this repository uses Git LFS (Git Large File Storage). To set up Git LFS on your local machine, follow these steps:

1. Install Git LFS: Visit the Git LFS website (https://git-lfs.github.com/) for installation instructions specific to your operating system.

2. Clone the Repository: Clone this repository to your local machine using `git clone`.

3. Initialize Git LFS: Navigate to the repository's root directory in the terminal and run the following command:

git lfs install


4. Pull the Repository: After initializing Git LFS, pull the repository using:

git pull origin master


## Disclaimer

This script is provided as-is and may require customization based on your specific PSG data and EDF file format. Ensure that you have the necessary rights and permissions to use the provided EDF files and data.

