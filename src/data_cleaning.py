import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, encoding="ISO-8859-1")

    # Remove cancelled invoices
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

    # Remove negative or zero quantities
    df = df[df['Quantity'] > 0]

    # Drop missing product descriptions
    df = df.dropna(subset=['Description'])

    # Normalize product names
    df['Description'] = df['Description'].str.strip().str.lower()

    # Remove duplicates
    df = df.drop_duplicates()

    return df
