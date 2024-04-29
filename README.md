# MacBook Pro I/O Device Obsolescence & Environmental Implications

## Introduction
This Streamlit app visualizes the obsolescence of various I/O devices for MacBook Pro and their environmental implications. Users can select an I/O device from the dropdown menu, and the corresponding charts will be displayed.

## Usage
- ### Setup Environment:
Ensure Python environment with required packages. Our code was tested with python version of 3.11.
install Streamlit to view our generated results: `pip install streamlit`.
- ### Run Streamlit App:
Execute the Streamlit app: `python -m streamlit run final.py`.
- ### Interact with Streamlit UI:
https://llms-generated-vis-code-3r8paqrspbzpoykzhke9cn.streamlit.app/

## How to Run
### Results Visualization:
- Clone the repository: `git clone https://github.com/elvashenyutong/LLMs-Generated-Vis-Code`
- Navigate to the directory: cd LLMs-Generated-Vis-Code
- Or download the package of the code
- Install dependencies: `pip install streamlit` for full test
- Run the Streamlit app: `python -m streamlit run final.py`.
- After executing the Streamlit app, it will create a local website
- OR you can simply access this [URL](https://llms-generated-vis-code-3r8paqrspbzpoykzhke9cn.streamlit.app/) to view what we have achieved.
### Data Collection:
- Download Google Extention: Amazon Product Finder - AMZScout PRO Extension
- Enable AMZScout PRO Extension
- Open the product detail page of the product you want
- Click the AMZScout icon in the lower right corner to open the expanded window
- Click on product history
- Open Chrome DevTools
- Copy and paste the script in `code_for_getting_data.js` to the console amd click Enter
- After collecting the data from the chart, you will get a .csv file


## Files Description
- [final.py]: Streamlit app for visualizing the results.
- [code_for_getting_data.js]: Code for collecting data.

## Dependencies
- Python 3.11+
- Streamlit
- Pandas