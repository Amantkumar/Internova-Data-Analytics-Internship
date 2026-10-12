
Internova Week 5 -- Power BI & Business Intelligence
Student Details
Name: Tiwari Aman Dhananjay
Internship: Internova Technologies
Week: Week 5
Topic: Power BI & Business Intelligence
Project: Sales Performance & Business Intelligence Dashboard
1. Project Overview
This project was completed as part of the Internova Week 5 assignment on Power BI and Business Intelligence.

The main objective was to build an interactive sales dashboard using Power BI and demonstrate practical skills in:

Data import
Data cleaning using Power Query
Data modeling
Relationships
DAX measures
Data visualization
Interactive filters
Business insights
Business recommendations
The final output is a Power BI dashboard named:

Sales Performance & Business Intelligence Dashboard

2. Tools & Technologies
Power BI Desktop
Power Query
DAX
CSV datasets
Data Modeling
Data Visualization
Business Intelligence
3. Project Structure
Internova-Week5-PowerBI-Business-Intelligence/
│
├── datasets/
│   ├── Customers.csv
│   ├── Products.csv
│   ├── Sales_Raw.csv
│   └── Sales_Clean.csv
│
├── outputs/
│   ├── Sales_by_Region.csv
│   └── Sales_by_Category.csv
│
├── powerbi_support/
│   ├── DAX_Measures.md
│   ├── Data_Model.md
│   ├── PowerBI_Task_Guide.md
│   └── Business_Insights_Reference.md
│
├── report/
│   └── Internova_Week5_PowerBI_Business_Intelligence_Detailed_Report.pdf
│
├── SCREENSHOT/
│   └── Power BI dashboard screenshot
│
├── Internova_Week5_PowerBI_Business_Intelligence.pbix
├── README.md
└── SUBMISSION_CHECKLIST.txt
4. Assignment Tasks
Task 1 -- Power BI Introduction & Data Import
The required sales datasets were imported into Power BI Desktop.

The project uses three main tables:

Customers
Products
Sales_Clean
The datasets contain customer information, product information, and sales transaction details.

Task 2 -- Data Cleaning & Preparation
Power Query was used to inspect and prepare the sales data.

The cleaning process included:

Checking column data types
Checking missing values
Removing duplicate records where required
Verifying numeric columns
Preparing the final clean sales table
Ensuring the dataset was ready for analysis
The cleaned table used for the dashboard is:

Sales_Clean

Task 3 -- Data Modeling & Relationships
Relationships were created between the dimension tables and the sales table.

Relationship Model
Customers
    │
    │ 1 : Many
    ▼
Sales_Clean
    ▲
    │ 1 : Many
    │
Products
Relationships
Customers[Customer_ID] → Sales_Clean[Customer_ID]
Products[Product_ID] → Sales_Clean[Product_ID]
This model allows customer and product information to be used for sales analysis.

5. DAX Measures
The following DAX measures were created for the dashboard.

Total Sales
Total Sales = SUM(Sales_Clean[Sales_Amount])
Average Sales
Average Sales = AVERAGE(Sales_Clean[Sales_Amount])
Total Records
Total Records = COUNTROWS(Sales_Clean)
Maximum Sale
Maximum Sale = MAX(Sales_Clean[Sales_Amount])
Minimum Sale
Minimum Sale = MIN(Sales_Clean[Sales_Amount])
Total Quantity
Total Quantity = SUM(Sales_Clean[Quantity])
Average Order Value
Average Order Value = DIVIDE([Total Sales], [Total Records])
Sales Percentage of Total
Sales % of Total =
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALL(Sales_Clean))
)
6. Dashboard Visualizations
The final dashboard contains multiple visuals for analyzing sales performance.

KPI Cards
Total Sales
Total Records
Average Order Value
Charts
Total Sales by Category
Total Sales by Month
Total Sales by Region
Product Analysis
A table was included to show:

Product
Total Quantity
Total Sales
Interactive Filters
Slicers were added for:

Region
Category
These filters allow users to interactively analyze different parts of the sales data.

7. Dashboard Title
The final dashboard heading is:

Sales Performance & Business Intelligence Dashboard

This title represents the purpose of the report and provides a professional presentation for the Power BI project.

8. Key Business Insights
The dashboard can be used to identify:

Overall sales performance.
Sales contribution from different product categories.
Monthly sales trends.
Regional sales performance.
Product-level sales and quantity performance.
Differences in sales across regions and categories.
High-performing areas that may require continued inventory support.
Lower-performing areas that may require further investigation.
The exact values should be taken from the final Power BI dashboard because they can change based on filters and selected data.

9. Business Recommendations
Based on the dashboard analysis, the following recommendations can be considered:

Recommendation 1 -- Focus on High-Performing Categories
Maintain sufficient inventory and operational support for categories generating higher sales.

Recommendation 2 -- Analyze Regional Performance
Compare regional sales performance and investigate regions with comparatively lower sales.

Recommendation 3 -- Monitor Monthly Trends
Use monthly sales trends to identify changes in demand and support better planning.

Recommendation 4 -- Review Product Performance
Identify products with strong sales and quantity performance and evaluate low-performing products for possible improvement.

10. Skills Demonstrated
This project demonstrates practical knowledge of:

Power BI Desktop
Power Query
Data Cleaning
Data Transformation
Data Modeling
Table Relationships
DAX
KPI Creation
Data Visualization
Interactive Dashboards
Business Intelligence
Business Analysis
Business Recommendations
11. Project Output
The main output of this project is an interactive Power BI dashboard that provides a consolidated view of sales performance.

The Power BI file is saved as:

Internova_Week5_PowerBI_Business_Intelligence.pbix

The project also contains supporting datasets, documentation, screenshots, and a detailed PDF report.

12. Screenshot Evidence
The SCREENSHOT folder contains the final Power BI dashboard screenshot used as project evidence.

The screenshot demonstrates:

Dashboard heading
KPI cards
Category analysis
Monthly sales trend
Regional sales analysis
Product-level analysis
Region and Category filters
13. How to Open the Project
Install and open Power BI Desktop.
Open the .pbix file.
Check the dashboard page.
Interact with the Region and Category slicers.
Explore the charts and KPI cards.
Review the data model and DAX measures if required.
14. Submission Checklist
Before submission, make sure the project contains:

 Power BI .pbix file
 Datasets
 Power Query cleaning
 Relationships
 DAX measures
 Dashboard visuals
 Interactive filters
 Dashboard screenshot
 PDF report
 README documentation
Conclusion
The Internova Week 5 project demonstrates the complete workflow of converting sales data into an interactive Business Intelligence dashboard using Power BI.

The project covers data preparation, modeling, DAX calculations, visualization, filtering, and business interpretation. It provides a practical example of how Power BI can be used to understand sales performance and support data-driven business decisions.

Author: Tiwari Aman Dhananjay
Project: Sales Performance & Business Intelligence Dashboard
Internship: Internova Technologies
