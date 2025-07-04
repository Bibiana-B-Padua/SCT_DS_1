# SCT_DS_1
# 📊 Task 01: Population Age Distribution Visualization – India (2022)
 This project is part of a data analysis and visualization assignment focused on using Python to create meaningful visual representations from structured data.

## 🧾 Objective

To create a bar chart that visually represents **India’s population distribution by age groups** for the year **2022**, using official demographic data.

## 📁 Files Included

- `task01_population_chart.py` – Python script to generate the bar chart.
- `Task01_India_Age_Distribution_Explained.pdf` – Final output PDF with the bar chart and an explanation slide.
- `India_Population_Distribution_2022.pdf` – Simple bar chart based on official data.
- `API_SP.POP.TOTL_DS2_en_excel_v2_127106.xls` – World Bank dataset used for population totals.

## 📊 Data Used

Data Sources:
- **UN World Population Prospects 2022** – for age group distribution proportions.
- **World Bank** dataset for total population: `API_SP.POP.TOTL_DS2_en_excel_v2_127106.xls`

| Age Group      | Population (in millions) | Percentage |
|----------------|--------------------------|------------|
| 0–20 Years     | 512                      | 36.1%      |
| 21–64 Years    | 807                      | 57.0%      |
| 65+ Years      | 98                       | 6.9%       |

## 📂 Dataset Source

This project references population data from the **World Bank Open Data Portal**:

- File: `API_SP.POP.TOTL_DS2_en_excel_v2_127106.xls`
- Indicator: **SP.POP.TOTL** – Total population by country and year
- [World Bank Dataset](https://data.worldbank.org/indicator/SP.POP.TOTL)

Although the bar chart is based on aggregated age groups, the overall population figure for **India in 2022** was derived from this dataset.

> Note: Full age-wise segmentation was simulated based on official proportions from **UN World Population Prospects 2022**.

## 🛠️ Technologies Used

- Python
- `matplotlib` for data visualization
- Jupyter/VS Code for development

## 📈 Output

The resulting bar chart clearly breaks down India's population into three distinct age categories. Each bar is color-coded and annotated with percentage values for better interpretability.

## 🔍 Insights

- The **working-age population (21–64 years)** forms the largest segment (57.0%), indicating strong economic potential.
- **Youth (0–20)** represent future contributors, while **elderly (65+)** indicate healthcare demand.

## 💡 How to Run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install matplotlib
   ```
3. Run the script:
   ```bash
   python task01_population_chart.py
   ```

## 📄 License

This project is released under the MIT License.
