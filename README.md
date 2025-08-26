📊 Customer Segmentation Analysis – Final Report
1. Project Description

The goal of this project is to perform customer segmentation for an e-commerce company using the marketing_campaign.csv dataset. By analyzing demographics, spending behavior, and campaign responses, customers are grouped into segments. These insights help improve targeted marketing strategies, customer satisfaction, and business performance.

2. Dataset Overview

Rows: 2,240 customers

Columns: 29 features (demographics, spending, purchases, campaigns)

Key Features:

Demographics: Year_Birth, Education, Marital_Status, Income, Dt_Customer

Spending: MntWines, MntFruits, MntMeatProducts, … MntGoldProds

Purchases: NumWebPurchases, NumCatalogPurchases, NumStorePurchases

Campaigns: AcceptedCmp1–5, Response

Others: Recency, Complain

3. Data Cleaning & Feature Engineering

Missing values in Income handled using median.

Converted Dt_Customer to datetime (format = %d-%m-%Y).

Created new features:

Age = 2025 – Year_Birth

Total_Spent = Sum of all product spending columns

Dropped irrelevant columns: ID, Z_CostContact, Z_Revenue.

4. Exploratory Data Analysis (EDA)

Age Distribution: Most customers are 30–60 years old.

Income vs Spending: Positive relationship (higher income → higher spending).

Campaign Response: Most customers did not respond; response rate is low.

(Include plots: Age histogram, Income vs Spending scatter, Campaign Response countplot).

5. Customer Segmentation (K-Means Clustering)

Features used: Income, Recency, Total_Spent, NumWebPurchases, NumCatalogPurchases, NumStorePurchases.

Standardized data and applied KMeans (k=4).

Cluster Profiles:

Cluster	Avg Income	Avg Age	Avg Spending	Recency	Insights
0	High	40s	High	Recent buyers	Premium segment – target with luxury campaigns
1	Medium	30s	Medium	Recent buyers	Growing customers – nurture loyalty
2	Low	50s	Low	Older customers	Value-seekers – discounts work best
3	Medium	60s	Low-Mid	Not recent	Dormant – need re-engagement strategies

(Include scatterplot: Income vs Total Spending colored by cluster).

6. Insights & Recommendations

High spenders: Focus on premium products, exclusive offers.

Value-seekers: Provide discounts, bundled offers.

Dormant customers: Send reactivation campaigns (emails, coupons).

Young professionals: Target digital/online campaigns, as they shop more online.

7. Learning Outcomes

Gained practical experience in clustering algorithms (KMeans).

Improved data cleaning & feature engineering skills.

Learned visualization techniques to present insights.
