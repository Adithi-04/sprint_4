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
import logging
import pytest
from user_Interface import selected_folder_path
from data_extraction import extract_column_headers
from user_Interface import *
from data_extraction import *

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

# Ensure pytest doesn't capture log output
@pytest.fixture(autouse=True)
def disable_capture_log(caplog):
    caplog.set_level(logging.DEBUG)

"""
SRS REQUIREMENT ID: KEX0002.3.3
URS REQUIREMENT ID: KEX002.4.30
TEST SCENARIO: "The system should have the ability to extract Tables even if there is no Row header /Column header specified."
"""

#positive test case to extract tables and listings for no row/column header


def test_no_row_header_positive():
    if __name__ == "__main__":
        logger.info("Starting test case for empty column headers")
        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
        
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        logger.info(f"Processing file: {file_name}")
                    
                        # Extract column headers using the extract_column_headers function
                        headers_data = extract_column_headers(rtf_content)
                    
                        # Log based on the result of the header extraction
                        if headers_data['data'] == []:
                            logger.info(f"Empty column headers found in file: {file_name}")
                            logger.debug(f"Empty column headers found in file: {file_name}")
                        else:
                            logger.info(f"Column headers extracted in file: {file_name}")
                            logger.debug(f"Column headers extracted in file: {file_name}")
                    
                except Exception as e:
                    logger.info(f"Error processing file {file_name}: {e}")
                    logger.debug(f"Error processing file {file_name}: {e}")


#negative test case to extract tables and listings for no row/column header
def test_no_row_header_negative():
    if __name__ == "__main__":
        logger.info("Starting negative test case for missing/invalid column headers")
        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
        
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        logger.info(f"Processing file: {file_name}")
                    
                        # Extract column headers using the original extract_column_headers function
                        headers_data = extract_column_headers(rtf_content)
                    
                        # Log based on the result of the header extraction
                        if headers_data['data'] == []:
                            logger.warning(f"Column headers missing or invalid in file: {file_name}")
                            logger.debug(f"Column headers missing or invalid in file: {file_name}")
                        else:
                            logger.info(f"Column headers extracted (negative test failed) in file: {file_name}")
                            logger.debug(f"Column headers extracted (negative test failed) in file: {file_name}")
                    
                except Exception as e:
                    logger.error(f"Error processing file {file_name}: {e}")
                    logger.debug(f"Error processing file {file_name}: {e}")


#positive test case to extract tables and listings for null row/column header
def test_no_null_column_header_positive():
    if __name__ == "__main__":

    # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
        
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        logger.info(f"Processing file: {file_name}")
                    
                        # Extract column headers using the original extract_column_headers function
                        headers_data = extract_column_headers(rtf_content)
                    
                        # Check for valid (non-null and non-empty) column headers
                        if headers_data['data'] and all(header.strip() != "" for header in headers_data['data']):
                            logger.info(f"Valid column headers found in file: {file_name}")
                            debug_print(f"Valid column headers found in file: {file_name}")
                        else:
                            logger.error(f"Null/Empty column headers detected (positive test failed) in file: {file_name}")
                            debug_print(f"Null/Empty column headers detected (positive test failed) in file: {file_name}")
                    
                except Exception as e:
                    logger.error(f"Error processing file {file_name}: {e}")
                    logger.debug(f"Error processing file {file_name}: {e}")



#negative test case to extract tables and listings for null row/column header

def test_no_null_column_header_negative():
    # Ensure that this script is being run directly, not imported
    if __name__ == "__main__":    
        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
        
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        logger.info(f"Processing file: {file_name}")
                    
                     # Extract column headers using the original extract_column_headers function
                        headers_data = extract_column_headers(rtf_content)
                    
                    # Check for null/empty column headers
                    if not headers_data['data'] or all(header.strip() == "" for header in headers_data['data']):
                        logger.warning(f"Null/Empty column headers detected in file: {file_name}")
                        logger.debug(f"Null/Empty column headers detected in file: {file_name}")
                    else:
                        logger.warning(f"Column headers extracted (negative test failed) in file: {file_name}")
                        logger.debug(f"Column headers extracted (negative test failed) in file: {file_name}")
                    
                except Exception as e:
                    logger.error(f"Error processing file {file_name}: {e}")
                    logger.debug(f"Error processing file {file_name}: {e}")
    


pytest.main([__file__])
with open(log_file, 'r') as f:
    print(f.read())
