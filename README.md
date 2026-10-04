# Advanced Logistics Data Analysis and Visualization Using Python

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![Dataset](https://img.shields.io/badge/Dataset-1%2C200%20Shipments-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Project Overview

This project demonstrates how Python-based data analysis and visualization can be applied to a hypothetical logistics operation. The objective is to transform shipment-level data into actionable insights related to delivery performance, transportation costs, shipment volume, route distance, regional performance, and operational bottlenecks.

The project uses a simulated dataset containing **1,200 shipments** across four regions, four warehouses, three transportation modes, and two service priorities.

> **Note:** The dataset is hypothetical and was generated for educational and analytical purposes. It does not represent real company or customer data.

## Objectives

- Simulate a realistic logistics dataset.
- Perform exploratory data analysis (EDA).
- Calculate central tendency and distribution statistics.
- Analyze correlations among key logistics variables.
- Compare transport-mode performance.
- Identify regional and temporal performance differences.
- Visualize cost and delivery-time relationships.
- Identify operational bottlenecks and cost drivers.
- Provide data-driven logistics recommendations.
- Document the complete analysis in a professional report.

## Key Metrics

| Metric | Result |
|---|---:|
| Shipments analyzed | 1,200 |
| Overall on-time delivery rate | 36.2% |
| Average delivery time | 7.78 days |
| Total simulated transportation cost | $1,074,534 |
| Transportation modes | Road, Rail, Air |
| Regions | North, South, East, West |
| Warehouses | WH-A, WH-B, WH-C, WH-D |

## Dataset

The dataset is located at:

```text
data/hypothetical_logistics_dataset.csv
```

### Main Variables

| Variable | Description |
|---|---|
| `Shipment_ID` | Unique shipment identifier |
| `Date` | Shipment date |
| `Region` | Shipment region |
| `Warehouse` | Origin warehouse |
| `Transport_Mode` | Road, Rail, or Air |
| `Priority` | Standard or Express |
| `Shipment_Volume_tons` | Shipment volume in tons |
| `Distance_km` | Transportation distance |
| `Delivery_Time_days` | Actual delivery time |
| `Transport_Cost_USD` | Transportation cost |
| `Target_Days` | Target/SLA delivery time |
| `On_Time` | Whether the shipment met its target |
| `Delay_Days` | Delay beyond target |
| `Cost_per_ton_USD` | Cost normalized by shipment volume |

## Exploratory Data Analysis

The analysis includes:

1. Descriptive statistics
2. Mean, median, standard deviation, minimum, and maximum
3. Distribution analysis
4. Correlation analysis
5. Transport-mode comparison
6. Regional performance analysis
7. Monthly performance analysis
8. Cost-per-ton analysis
9. Delivery-time analysis

## Visualizations

### 1. Delivery-Time Distribution

![Delivery Distribution](visualizations/01_delivery_distribution.png)

The histogram shows the distribution and variability of delivery times. The mean and median help identify skewness and the presence of slower shipments.

### 2. On-Time Delivery by Transport Mode

![On-Time by Mode](visualizations/02_ontime_by_mode.png)

This comparison shows how service reliability differs between Road, Rail, and Air.

### 3. Transportation Cost vs Distance

![Cost vs Distance](visualizations/03_cost_vs_distance.png)

The scatter plot examines the relationship between route distance and transportation cost. Point size represents shipment volume, while the marker grouping represents transportation mode.

### 4. Correlation Matrix

![Correlation Matrix](visualizations/04_correlation_matrix.png)

The correlation matrix highlights relationships between shipment volume, distance, delivery time, cost, delay, and cost per ton.

### 5. Monthly On-Time Performance

![Monthly Performance](visualizations/05_monthly_ontime.png)

The time-series visualization shows changes in on-time performance throughout 2025.

### 6. Regional Performance

![Regional Performance](visualizations/06_region_performance.png)

This visualization compares regional delivery time and average transportation cost.

## Key Insights

### Service Reliability

The simulated network achieves an overall on-time delivery rate of **36.2%**. This indicates substantial opportunity for improvement in the hypothetical operation.

### Speed vs Cost

Air transportation provides faster service but operates at a higher cost structure. This illustrates the common logistics trade-off between delivery speed and transportation expense.

### Distance as a Cost Driver

Transportation cost generally increases as route distance increases. Distance is therefore an important factor when evaluating route and carrier efficiency.

### Shipment Volume

Larger shipments tend to increase total transportation cost and delivery time. Shipment consolidation and improved load planning can therefore contribute to better unit economics.

### Regional Bottlenecks

The regional analysis identifies lower-performing areas that should receive targeted investigation. Route conditions, carrier performance, congestion, warehouse processes, and handoffs should be examined before implementing network-wide changes.

### Cost Normalization

Cost per ton provides a more useful efficiency metric than total shipment cost when comparing shipments of different sizes.

## Recommendations

1. **Use mode selection strategically**  
   Reserve premium transportation for shipments where the time benefit justifies the additional cost.

2. **Investigate underperforming regions**  
   Conduct route-level and carrier-level analysis in regions with weak on-time performance.

3. **Track cost per ton**  
   Use normalized transportation cost to identify inefficient lanes and low-utilization shipments.

4. **Improve shipment consolidation**  
   Combine compatible shipments where service-level requirements allow.

5. **Introduce exception monitoring**  
   Flag shipments that are likely to miss their SLA or exceed expected transportation cost.

6. **Monitor performance monthly**  
   Track on-time delivery, delivery time, cost per ton, shipment volume, and exceptions through a recurring dashboard.

## Project Structure

```text
advanced-logistics-data-analysis/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── data/
│   └── hypothetical_logistics_dataset.csv
│
├── src/
│   └── logistics_analysis.py
│
├── visualizations/
│   ├── 01_delivery_distribution.png
│   ├── 02_ontime_by_mode.png
│   ├── 03_cost_vs_distance.png
│   ├── 04_correlation_matrix.png
│   ├── 05_monthly_ontime.png
│   └── 06_region_performance.png
│
└── report/
    └── Advanced_Logistics_Data_Analysis_Report.docx
```

## Technologies Used

- **Python 3.9+**
- **NumPy** — numerical calculations and data simulation
- **pandas** — data manipulation and exploratory analysis
- **Matplotlib** — data visualization
- **python-docx** — report generation

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/advanced-logistics-data-analysis.git
cd advanced-logistics-data-analysis
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Analysis

The analysis script can be executed with:

```bash
python src/logistics_analysis.py
```

The script reads:

```text
data/hypothetical_logistics_dataset.csv
```

and performs the core EDA and visualization steps.

## Reproducibility

The original dataset was generated using a fixed random seed (`42`). This makes the simulation reproducible.

The project separates:

- **Data** — simulated shipment records
- **Code** — analysis logic
- **Visualizations** — generated analytical outputs
- **Report** — final documented findings

## Report

The complete written report is available at:

```text
report/Advanced_Logistics_Data_Analysis_Report.docx
```

It includes:

- Methodology
- Dataset description
- Exploratory analysis
- Statistical calculations
- Embedded visualizations
- Visualization justification
- Analytical interpretation
- Key insights
- Recommendations
- Python code excerpts
- Limitations
- Conclusion

## Limitations

This project is educational and uses simulated data. Therefore:

- Results should not be interpreted as real logistics performance.
- Simulation relationships are assumptions rather than estimates from real operations.
- Correlation does not prove causation.
- Real-world decisions should use actual shipment, carrier, route, warehouse, fuel, labor, and customer data.
- Additional statistical modeling would be appropriate for forecasting and causal analysis.

## Future Improvements

Possible extensions include:

- Predictive delivery-delay modeling
- Machine-learning based ETA prediction
- Carrier performance scoring
- Route optimization
- Fuel-cost analysis
- Warehouse utilization analysis
- Interactive Power BI/Tableau dashboard
- Automated KPI reporting
- Anomaly detection
- Demand forecasting
- Cost optimization using linear programming

## Author

**POLANKI**

This project was developed as an advanced data analysis and visualization exercise focused on logistics and supply-chain decision-making.

## License

This project is released under the MIT License. See [`LICENSE`](LICENSE) for details.
