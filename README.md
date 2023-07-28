# Dataset 
https://zenodo.org/record/2650142

 # Sleep Analysis Project

The Sleep Analysis Project aims to analyze and predict certain aspects of physiological data collected from PSG (Polysomnography) recordings. PSG is a powerful diagnostic tool used in sleep medicine to monitor and record various physiological signals during sleep. In this project, we use Python and various machine learning techniques to parse, process, and analyze PSG data.

## Requirements

To run this project, you'll need the following dependencies:

- Python (>=3.6)
- pandas
- scikit-learn
- pyedflib
- tqdm

You can install the required dependencies using pip:

pip install -r requirements.txt

## Project Structure

The project has the following structure:


Sure! Here's the README.md content that you can directly paste into your repository's README.md file:

vbnet
Copy code
# Sleep Analysis Project

The Sleep Analysis Project aims to analyze and predict certain aspects of physiological data collected from PSG (Polysomnography) recordings. PSG is a powerful diagnostic tool used in sleep medicine to monitor and record various physiological signals during sleep. In this project, we use Python and various machine learning techniques to parse, process, and analyze PSG data.

## Requirements

To run this project, you'll need the following dependencies:

- Python (>=3.6)
- pandas
- scikit-learn
- pyedflib
- tqdm

You can install the required dependencies using pip:

pip install -r requirements.txt

shell
Copy code

## Project Structure

The project has the following structure:

sleep/
|-- data/
| |-- CSV_Data/
| | |-- subject1_data_1200.csv
| | |-- subject2_data_1200.csv
| |-- DatabaseSubjects/
| | |-- subject1.edf
| | |-- subject2.edf
|-- scripts/
| |-- psg_data_parser.py
| |-- model.py
|-- sleepenv/
| |-- (virtual environment files, if used)
|-- .gitignore
|-- README.md
|-- requirements.txt


## Data

The `data/` directory contains the CSV files (`CSV_Data`) and EDF files (`DatabaseSubjects`) used in the project. The CSV files contain preprocessed data extracted from PSG recordings, while the EDF files store raw PSG data.

## Scripts

The `scripts/` directory contains Python scripts used for data parsing and machine learning modeling. Here's a brief description of each script:

### 1. psg_data_parser.py

The `psg_data_parser.py` script contains a function `export_psg_to_csv()` to parse PSG data from EDF files and export it to CSV format. It utilizes the `pyedflib` library to read EDF files and `pandas` to create CSV files containing selected channels of interest.

To run the script, use the following command:

python scripts/psg_data_parser.py --edf_path data/DatabaseSubjects/subject2.edf --csv_path data/CSV_Data/subject2_data.csv --samples_wanted 1200


Replace `data/DatabaseSubjects/subject2.edf` with the path to the EDF file, `data/CSV_Data/subject2_data.csv` with the desired path for the output CSV file, and `1200` with the number of samples wanted.

### 2. model.py

The `model.py` script contains functions to load data from a CSV file, train various regression models using scikit-learn, and evaluate their performance. It includes a function `load_data()` to load data from the CSV file and a function `test_all_models()` to train and evaluate multiple regression models.

To run the script, use the following command:

python scripts/model.py --data_path data/CSV_Data/subject2_data.csv --x_column PULSE --y_column ECG


Replace `data/CSV_Data/subject2_data.csv` with the path to the CSV data file, `PULSE` with the name of the column containing the X variable, and `ECG` with the name of the column containing the Y variable.

## How to Use

1. Download or clone the repository to your local machine.
2. Set up a virtual environment (optional but recommended).
3. Install the required dependencies using `pip`.
4. Execute the `psg_data_parser.py` script to parse PSG data from EDF to CSV format (if needed).
5. Run the `model.py` script to train and evaluate regression models using the CSV data.

Note: Ensure that you have the necessary EDF files (if using `psg_data_parser.py`) and CSV data files (if using `model.py`) in the appropriate directories (`data/CSV_Data` and `data/DatabaseSubjects`, respectively).

## Contribution

We welcome contributions to this project. If you find any issues, have suggestions, or want to add new features, feel free to open a pull request or submit an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

Please note that you should also create a requirements.txt file in the root directory of your project, containing the required dependencies (pandas, scikit-learn, pyedflib, tqdm). The requirements.txt file should look like this:

pandas
scikit-learn
pyedflib
tqdm
