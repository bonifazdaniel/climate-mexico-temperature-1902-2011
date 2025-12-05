Instructions
User Guide for the Climate Data Analysis Project
This document provides instructions for using, reproducing, and adapting the climate data analysis project contained in your GitHub repository. The project analyzes long-term temperature trends in Mexico using structured data, reproducible scripts, and professional visualization standards.
1. Project Structure
The repository follows a professional data science folder structure:

• data/raw/ – Stores original input files (KML or CSV)
• data/interim/ – Intermediate transformed files
• data/processed/ – Final cleaned dataset
• src/data/ – Python scripts for data conversion and preprocessing
• src/visualization/ – Scripts for charts and analytics
• reports/ – Visual outputs and documentation
• docs/ – Documentation such as user guides
• README.md – Main project description
2. Requirements
You will need the following tools installed:

• Python 3.10 or later
• Power BI Desktop (optional for dashboard)
• Required libraries:
  pip install pandas numpy matplotlib geopandas

3. Running the Data Processing Pipeline
1. Place raw files into data/raw/
2. Run preprocessing:
     python src/data/build_processed_dataset.py
3. The cleaned CSV will appear in data/processed/

4. Running Visualizations
To generate charts such as temperature trends and thermal amplitude graphs:

     python src/visualization/basic_analysis.py

Charts will be saved inside reports/figures/.
5. Power BI Dashboard Instructions
1. Open Power BI Desktop
2. Import the file temperaturas_mx_1902_2011.csv from data/processed/
3. Create charts for Mean Temperature, Min/Max Temperature, and Thermal Amplitude
4. Save the dashboard as climate_dashboard.pbix inside docs/

6. Interpretation of Results
The analysis reveals progressive warming trends across Mexican regions between 1902 and 2011. Users can explore thermal extremes, compare regions, and apply insights to climate, agriculture, urban planning, or environmental studies.
7. Reproducibility Notes
All scripts in src/ are fully modular. Running them again will regenerate all outputs, making this project easy to extend or adapt to additional climate datasets.
