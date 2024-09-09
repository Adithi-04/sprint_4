"""
PROGRAM NAME: Test Functions for Sprint 4
AUTHOR(S): L. Adithi
VERSION AND DATE: 4.1 | September 6, 2024

PURPOSE: 
This module contains test functions designed to validate the RTF processing system as part of Sprint 4.

TEST SCENARIOS:
1. "The system should have the ability to extract Tables even if there is no Row header /Column header specified."

2. "The system should have the ability to extract Lists even if there is no Row header /Column header specified."

3. "The system should have the capability to handle and extract data from Table files that have columns with Null column headers."

4. "The system should have the capability to handle and extract data from List files that have columns with Null column headers."

5. Generic Test Cases:
   - Validation of RTF file integrity.
   - Schema validation for RTF files.
   - Conversion process from RTF to JSON or other required formats.
   - Extraction of basic data components of the file as seen in sprint-1

LINK TO TEST SCENARIO SHEET:
For further details, please refer to the test scenario sheet: https://docs.google.com/spreadsheets/d/1Rw6rX8bqjbrdjF0NaNotoCAPgYxmmgTacLEXOluY4po/edit?usp=sharing

COPYRIGHT: © M/s CARE2DATA 2024. All Rights Reserved.

"""

import os
import re
import logging
import pytest
from user_Interface import selected_folder_path
from data_extraction import extract_column_headers
from data_extraction import debug_print

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
log_file = "test_log.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)


"""
SRS REQUIREMENT ID: KEX0002.3.3
URS REQUIREMENT ID: KEX002.4.30
TEST SCENARIO: "The system should have the ability to extract Tables even if there is no Row header /Column header specified."
"""

#positive test case to extract tables and listings for no row/column header


def no_row_header_positive(selected_folder_path):
    valid_files = []
    logging.info("Starting test case for empty column headers")
    
    # Process each RTF file in the selected folder
    for file_name in os.listdir(selected_folder_path):
        file_path = os.path.join(selected_folder_path, file_name)
        
        if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    rtf_content = file.read()
                    logging.info(f"Processing file: {file_name}")
                    
                    # Extract column headers using the extract_column_headers function
                    headers_data = extract_column_headers(rtf_content)
                    
                    # Log based on the result of the header extraction
                    if headers_data['data'] == []:
                        logging.info(f"Empty column headers found in file: {file_name}")
                        debug_print(f"Empty column headers found in file: {file_name}")
                    else:
                        logging.info(f"Column headers extracted in file: {file_name}")
                        debug_print(f"Column headers extracted in file: {file_name}")
                    
                    valid_files.append(file_name)  # Add valid file to the list

            except Exception as e:
                logging.error(f"Error processing file {file_name}: {e}")
                debug_print(f"Error processing file {file_name}: {e}")

    logging.info("Test case for empty column headers completed")
    return valid_files

#negative test case to extract tables and listings for no row/column header
def no_row_header_negative(selected_folder_path):
    invalid_files = []
    logging.info("Starting negative test case for missing/invalid column headers")
    
    # Process each RTF file in the selected folder
    for file_name in os.listdir(selected_folder_path):
        file_path = os.path.join(selected_folder_path, file_name)
        
        if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    rtf_content = file.read()
                    logging.info(f"Processing file: {file_name}")
                    
                    # Extract column headers using the original extract_column_headers function
                    headers_data = extract_column_headers(rtf_content)
                    
                    # Log based on the result of the header extraction
                    if headers_data['data'] == []:
                        logging.warning(f"Column headers missing or invalid in file: {file_name}")
                        debug_print(f"Column headers missing or invalid in file: {file_name}")
                        invalid_files.append(file_name)  # Add invalid file to the list
                    else:
                        logging.error(f"Column headers extracted (negative test failed) in file: {file_name}")
                        debug_print(f"Column headers extracted (negative test failed) in file: {file_name}")
                    
            except Exception as e:
                logging.error(f"Error processing file {file_name}: {e}")
                debug_print(f"Error processing file {file_name}: {e}")
                invalid_files.append(file_name)  # Add invalid file to the list

    logging.info("Negative test case for missing/invalid column headers completed")
    return invalid_files


#positive test case to extract tables and listings for null row/column header
def no_null_column_header_positive(selected_folder_path):
    valid_null_header_files = []
    logging.info("Starting positive test case for valid column headers")
    
    # Process each RTF file in the selected folder
    for file_name in os.listdir(selected_folder_path):
        file_path = os.path.join(selected_folder_path, file_name)
        
        if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    rtf_content = file.read()
                    logging.info(f"Processing file: {file_name}")
                    
                    # Extract column headers using the original extract_column_headers function
                    headers_data = extract_column_headers(rtf_content)
                    
                    # Check for valid (non-null and non-empty) column headers
                    if headers_data['data'] and all(header.strip() != "" for header in headers_data['data']):
                        logging.info(f"Valid column headers found in file: {file_name}")
                        debug_print(f"Valid column headers found in file: {file_name}")
                        valid_null_header_files.append(file_name)  # Add valid file to the list
                    else:
                        logging.error(f"Null/Empty column headers detected (positive test failed) in file: {file_name}")
                        debug_print(f"Null/Empty column headers detected (positive test failed) in file: {file_name}")
                    
            except Exception as e:
                logging.error(f"Error processing file {file_name}: {e}")
                debug_print(f"Error processing file {file_name}: {e}")

    logging.info("Positive test case for valid column headers completed")
    return valid_null_header_files


#negative test case to extract tables and listings for null row/column header

def no_null_column_header_negative(selected_folder_path):
    invalid_null_header_files = []
    logging.info("Starting negative test case for null column headers")
    
    # Process each RTF file in the selected folder
    for file_name in os.listdir(selected_folder_path):
        file_path = os.path.join(selected_folder_path, file_name)
        
        if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    rtf_content = file.read()
                    logging.info(f"Processing file: {file_name}")
                    
                    # Extract column headers using the original extract_column_headers function
                    headers_data = extract_column_headers(rtf_content)
                    
                    # Check for null/empty column headers
                    if not headers_data['data'] or all(header.strip() == "" for header in headers_data['data']):
                        logging.warning(f"Null/Empty column headers detected in file: {file_name}")
                        debug_print(f"Null/Empty column headers detected in file: {file_name}")
                        invalid_null_header_files.append(file_name)  # Add file with null headers to the list
                    else:
                        logging.error(f"Column headers extracted (negative test failed) in file: {file_name}")
                        debug_print(f"Column headers extracted (negative test failed) in file: {file_name}")
                    
            except Exception as e:
                logging.error(f"Error processing file {file_name}: {e}")
                debug_print(f"Error processing file {file_name}: {e}")
                invalid_null_header_files.append(file_name)  # Add file to the list in case of errors

    logging.info("Negative test case for null column headers completed")
    return invalid_null_header_files


if __name__ == "__main__":
    pytest.main([__file__])

    # After the test run, open and print the log file contents
    with open(log_file, 'r') as f:
        print(f.read())