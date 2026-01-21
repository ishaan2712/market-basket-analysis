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
