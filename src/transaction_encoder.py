import pandas as pd

def create_basket(df):
    """
    Groups items by InvoiceNo to create transaction baskets.
    """
    basket = (
        df.groupby('InvoiceNo')['Description']
        .apply(list)
    )
    return basket


def one_hot_encode(basket_series):
    """
    Converts transaction baskets into one-hot encoded dataframe.
    """
    from mlxtend.preprocessing import TransactionEncoder

    te = TransactionEncoder()
    te_array = te.fit(basket_series).transform(basket_series)

    encoded_df = pd.DataFrame(
        te_array,
        columns=te.columns_
    )

    return encoded_df
