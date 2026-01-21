# Market Basket Analysis

This project applies Market Basket Analysis to real-world retail transaction data
to discover frequently purchased product combinations and generate actionable
cross-selling insights.

---

## Step 1: Data Cleaning

The raw retail dataset contained cancelled invoices, product returns, missing
product descriptions, and inconsistent product naming.

Cleaning steps performed:
- Removed cancelled transactions
- Filtered out returns and invalid quantities
- Handled missing product descriptions
- Normalized product names
- Removed duplicate records

This step ensures high-quality transactional data before association rule mining.
## Step 2: Transaction Encoding

Cleaned retail transactions were grouped by invoice number to create
product baskets. These baskets were transformed into a one-hot encoded
matrix using transaction encoding techniques.

Steps performed:
- Grouped products by transaction ID
- Removed single-item transactions
- Applied one-hot encoding for Apriori compatibility

This step prepares the dataset for frequent itemset mining and
association rule analysis.
## Step 3: Frequent Itemset Mining (Apriori)

The Apriori algorithm was applied to the one-hot encoded transaction
data to identify frequent itemsets based on minimum support thresholds.

Steps performed:
- Applied Apriori algorithm to encoded transactions
- Extracted frequent itemsets with support values
- Analyzed itemset sizes and frequency distribution

This step reveals commonly purchased product combinations.
