# Week 6 Final Capstone — Sales Data Analytics & Business Intelligence

**Student:** Tiwari Aman Dhananjay  
**Internship:** Internova Technologies  
**Project:** Sales Performance & Business Intelligence Dashboard

## Project overview
This capstone extends the actual Week 5 Power BI sales project. It combines Git/GitHub workflow, data cleaning, EDA, Python visualizations, business insights, and the existing Power BI dashboard. The included CSVs and PBIX come from the Week 5 project supplied for this capstone.

## Business problem
Analyze sales transactions to understand category, region, customer segment, and monthly performance, and turn the findings into practical business recommendations.

## Dataset
- `datasets/Sales_Raw.csv` — raw transactions (121 rows including a duplicate; missing Quantity and Discount values).
- `datasets/Sales_Clean.csv` — Week 5 prepared sales table (120 records).
- `datasets/Customers.csv` — customer region and segment information.
- `datasets/Products.csv` — product names, categories, and unit prices.

The source data uses Discount as a percentage (for example, 5 means 5%). The script removes duplicate Sale_ID values and infers missing Quantity/Discount from the existing Sales_Amount where possible, then recalculates Sales_Amount.

## Tools
Python, Pandas, NumPy, Matplotlib, Power BI Desktop, Power Query, DAX, Git, GitHub.

## Run the analysis
```bash
pip install -r requirements.txt
python src/analysis.py
```
The script writes cleaned/enriched data, descriptive statistics, correlations, outlier records, grouped summaries, six charts, and key insights into `outputs/` and `visualizations/`.

## EDA and visualizations
Six charts are included: monthly sales trend, sales by category, region, customer segment, quantity versus sales, and sales amount distribution. See `outputs/Key_Insights.txt` and the grouped CSVs for the numeric findings.

## Power BI dashboard
The actual Week 5 file is included at `powerbi_support/Internova_Week5_PowerBI_Business_Intelligence.pbix`, and its screenshot is in `screenshots/Week5_PowerBI_Dashboard_Final.png`. The dashboard uses KPI cards, category/month/region visuals, a product table, and slicers. The original Week 5 model and DAX references are retained under `powerbi_support/`. If you modify the dashboard for Week 6, save a new copy as `Internova_Week6_Sales_Capstone.pbix` rather than overwriting the original.

## Key insights
- The cleaned dataset contains 120 transactions and total sales of ₹9,534,180.
- Average transaction value is ₹79,451.50; the highest transaction is ₹432,250 (S0032) and the lowest is ₹1,080 (S0086).
- Computers is the top sales category at ₹5,371,450.
- East is the leading region at ₹5,490,620.
- Corporate is the largest customer segment by sales at ₹4,168,450.
- Feb has the highest monthly sales at ₹3,023,670; Mar is lowest at ₹1,452,015.

## Recommendations
1. Maintain inventory availability in leading categories and regions, while validating profit margin and stock-out levels.
2. Investigate weaker categories/regions/segments and run controlled promotions or product bundles, comparing performance to a baseline.
3. Monitor discounting and order value together; revenue alone does not measure profitability.

## Git/GitHub workflow — minimum 3 meaningful commits
From the project root, after creating an empty GitHub repository:
```bash
git init
git add datasets/
git commit -m "Add Week 5 sales datasets for capstone"
git add src/ outputs/ visualizations/
git commit -m "Add cleaning, EDA, and sales visualizations"
git add README.md report/ presentation/ powerbi_support/ screenshots/
git commit -m "Add dashboard, report, presentation, and documentation"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
git pull origin main
```
Replace the placeholder with your own repository URL. Do not commit credentials.

## Submission checklist
- [ ] Review findings against generated outputs.
- [ ] Confirm the PBIX opens and screenshot is readable.
- [ ] Include at least five insights and two recommendations in the final report/presentation.
- [ ] Make at least three meaningful commits and verify the GitHub repository.
- [ ] Ensure no private credentials or unrelated files are included.
