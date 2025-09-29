## **Analytical Approach**

## **Data Cleaning**

**Handled Missing Values:**  
Replaced all null or missing values in key numeric columns with `0` to prevent calculation errors and ensure smooth merging and computations.


## **Data Merging and Summary Creation**

**Inventory Summary:**  
Merged inventory movement data with the product catalog to create a stock summary showing current inventory and stock levels per product.

**Advertising Summary:**  
Combined advertising data with performance metrics to generate an ad summary, highlighting spend and conversion effectiveness for each product.


## **KPI Calculations**

Calculated the following **Key Performance Indicators (KPIs)** for each product:

**Return Rate**  
Used to identify products with potential quality or customer satisfaction issues.

**Advertising Spend Efficiency**  
Highlights products with strong or weak marketing ROI.

**Sales Velocity**  
Measured units sold relative to inventory levels to distinguish fast-moving versus slow-moving products.


## **Adaptive Thresholds**

Used **quantile-based**, **data-driven thresholds** instead of fixed numbers.  
This approach flags products performing unusually well or poorly, enabling focus on problematic SKUs.


## **Key Discoveries**

**Stockouts:** Some products frequently ran out of stock, leading to missed sales opportunities and revenue drops.  
**High Return Rates:** A few SKUs showed high return ratios, indicating possible quality issues, listing inaccuracies, or low satisfaction.  
**Inefficient Ad Spend:** Certain products exhibited low marketing ROI, suggesting ad budget optimization opportunities.  
**Variable Sales Velocity:** Some SKUs sold rapidly, while others moved slowly, tying up inventory capital.


## **Assumptions**

**Missing Data Handling:** All missing numeric values (inventory, sales, ad spend) were treated as `0`.  
**Adaptive Thresholding:** Quantile-based thresholds better captured natural variability and outliers than static cutoffs.  
**Inventory Interpretation:** Zero or null stock was treated as stockouts, not data gaps, affecting sales velocity calculations.


## **AI Usage Disclosure**

**AI Tools Used:** Assisted with drafting content, structuring the analysis, and generating initial code snippets.  
**Manual Validation:** All data cleaning, KPI computation, and results were manually validated to ensure accuracy and business relevance.  
**Data Understanding:** Column names and meanings were documented to avoid misinterpretation.


## **Future Enhancements & Recommendations**

## **Automate Data Pipelines**  
Build automated ingestion and transformation pipelines for real-time KPI tracking.

## **Integrate Customer Feedback**  
Add sentiment analysis from reviews to explain high returns or low satisfaction.

## **Predictive Modeling**  
Apply machine learning to forecast demand and detect at-risk SKUs early.

## **Inventory Optimization**  
Use KPIs and forecasts for smarter replenishment and stock allocation.

## **Interactive Dashboards**  
Create visual dashboards to monitor KPI trends, inventory health, and marketing performance.
