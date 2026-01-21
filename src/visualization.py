import matplotlib.pyplot as plt
import networkx as nx

def plot_lift_confidence(rules):
    plt.figure(figsize=(8, 6))
    plt.scatter(
        rules['confidence'],
        rules['lift'],
        alpha=0.6
    )
    plt.xlabel("Confidence")
    plt.ylabel("Lift")
    plt.title("Confidence vs Lift of Association Rules")
    plt.grid(True)
    plt.show()


def plot_association_network(rules, top_n=15):
    top_rules = rules.head(top_n)

    G = nx.DiGraph()

    for _, row in top_rules.iterrows():
        for antecedent in row['antecedents']:
            for consequent in row['consequents']:
                G.add_edge(
                    antecedent,
                    consequent,
                    weight=row['lift']
                )

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.5)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        font_size=9,
        alpha=0.8
    )
    plt.title("Product Association Network (Top Rules)")
    plt.show()
