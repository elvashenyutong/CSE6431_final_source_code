# Technological Progress and Obsolescence: Analyzing the Environmental and Economic Impacts of MacBook Pro I/O Devices

## Introduction
This Streamlit app visualizes the obsolescence of various I/O devices for MacBook Pro and their sales history. Users can select an I/O device from the dropdown menu, and the corresponding charts will be displayed. The Jupyter Notebook is used to visualize the sales data obtained from Amazon.

## Usage
- ### Setup Environment:
    - #### For Results Visualization:
        Ensure you have Python 3.11+ installed on your system.
        Install Streamlit to view our generated results: `pip install streamlit`.
   - #### For Chart Generation:
        Ensure you have Python 3 installed, as well as Jupyter Notebook.
        You can install Jupyter using pip:`pip install notebook`.
        This notebook requires the following Python libraries:
            - pandas (for data manipulation)
            - matplotlib (for plotting graphs)
        You can install these dependencies using pip:`pip install pandas matplotlib`

- ### How to Run
    #### Results Visualization:
    - Clone the repository: `git clone https://github.com/elvashenyutong/CSE6431_final_source_code.git`
    - Navigate to the directory: cd CSE6431_final_source_code
    - OR download the package of the code
    - Install dependencies: `pip install streamlit` for full test
    - Run the Streamlit app: `python -m streamlit run final.py`.
    - After executing the Streamlit app, it will create a local website
    - OR you can simply access the website to view what we have achieved.
    - Interact with Streamlit UI: https://cse6431finalsourcecodegit-bdmappukqboyjk5zq2vx8bx.streamlit.app/
    ### Data Collection:
    - Download the Google Extention: Amazon Product Finder - AMZScout PRO Extension
    - Enable AMZScout PRO Extension
    - Open the product detail page of the product you want
    - Click the AMZScout icon in the lower right corner to open the expanded window
    - Click on product history
    - Open Chrome DevTools
    - Copy and paste the script in `code_for_getting_data.js` to the Chrome DevTools console section and click Enter
    - After collecting the data from the chart, you will get a .csv file
    ### Chart Generation:
    - Clone the repository: `git clone https://github.com/elvashenyutong/CSE6431_final_source_code.git`
    - Navigate to the directory: cd CSE6431_final_source_code
    - OR download the package of the code
    - Install dependencies: `pip install pandas matplotlib` for the test
    - After installing the dependencies and cloning the repository, navigate to the directory containing the notebook and start Jupyter Notebook: `jupyter notebook`
    - OR you can simply see the result that we have run in the file `OS Final Project Plots.ipynb`.

## Files Description
- [final.py]: Streamlit app for visualizing the results.
- [code_for_getting_data.js]: Code for collecting data.
- [OS Final Project Plots.ipynb]: Code for generate chart.

## Dependencies
- Python 3.11+
- Streamlit
- Pandas
- Matplotlib