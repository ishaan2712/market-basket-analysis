import pandas as pd
from mlxtend.frequent_patterns import apriori

def run_apriori(encoded_df, min_support=0.01):
    """
    Runs Apriori algorithm on one-hot encoded transaction data.
    """
    frequent_itemsets = apriori(
        encoded_df,
        min_support=min_support,
        use_colnames=True
    )

    frequent_itemsets['itemset_size'] = frequent_itemsets['itemsets'].apply(len)

    return frequent_itemsets.sort_values(
        by='support',
        ascending=False
    ).reset_index(drop=True)
