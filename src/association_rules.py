import pandas as pd
from mlxtend.frequent_patterns import association_rules

def generate_rules(frequent_itemsets, metric="lift", min_threshold=1.0):
    """
    Generates association rules from frequent itemsets.
    """
    rules = association_rules(
        frequent_itemsets,
        metric=metric,
        min_threshold=min_threshold
    )

    rules = rules.sort_values(
        by=["lift", "confidence"],
        ascending=False
    ).reset_index(drop=True)

    return rules
