# --------------------------
# Step 1: Import libraries
# --------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import warnings
import os

# Suppress joblib CPU warning
warnings.filterwarnings("ignore", category=UserWarning, module="joblib")
os.environ["LOKY_MAX_CPU_COUNT"] = "4"   # set manually to avoid WMIC issue

# --------------------------
# Step 2: Load dataset
# --------------------------
df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("Shape:", df.shape)
print(df.head())

# --------------------------
# Step 3: Data Cleaning
# --------------------------

# Fill missing Income with median
df["Income"] = df["Income"].fillna(df["Income"].median())

# Convert Dt_Customer (format = dd-mm-yyyy)
df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], format="%d-%m-%Y")

# Create Age feature
df["Age"] = 2025 - df["Year_Birth"]

# Create Total Spending
df["Total_Spent"] = df[[
    "MntWines","MntFruits","MntMeatProducts",
    "MntFishProducts","MntSweetProducts","MntGoldProds"
]].sum(axis=1)

# Drop unnecessary columns
df.drop(["ID","Z_CostContact","Z_Revenue"], axis=1, inplace=True)

print("\nCleaned Columns:", df.columns)

# --------------------------
# Step 4: Exploratory Data Analysis
# --------------------------

# Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Age"], bins=30, kde=True, color="blue")
plt.title("Age Distribution")
plt.show()

# Income vs Spending
plt.figure(figsize=(6,4))
sns.scatterplot(x="Income", y="Total_Spent", data=df, alpha=0.6)
plt.title("Income vs Total Spending")
plt.show()

# Response Count
plt.figure(figsize=(5,3))
sns.countplot(x="Response", data=df, palette="Set2")
plt.title("Campaign Response Distribution")
plt.show()

# --------------------------
# Step 5: Clustering
# --------------------------

# Select features for clustering
features = ["Income","Recency","Total_Spent",
            "NumWebPurchases","NumCatalogPurchases","NumStorePurchases"]

X = df[features]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans (4 clusters)
kmeans = KMeans(n_clusters=4, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# --------------------------
# Step 6: Cluster Visualization
# --------------------------

plt.figure(figsize=(7,5))
sns.scatterplot(x="Income", y="Total_Spent", hue="Cluster", data=df, palette="Set2", alpha=0.7)
plt.title("Customer Segmentation: Income vs Spending")
plt.show()

# --------------------------
# Step 7: Cluster Insights
# --------------------------

cluster_summary = df.groupby("Cluster")[["Income","Age","Total_Spent","Recency"]].mean().round(2)
print("\nCluster Summary:\n", cluster_summary)

# Count customers per cluster
print("\nCluster Counts:\n", df["Cluster"].value_counts())
