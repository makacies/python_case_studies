import os
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

hamlets = pd.read_csv("./asset.csv", index_col=0)

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "\r", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    # text = ' '.join(text.split())
    word_counts = Counter(text.split(' '))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    data["count"] = counted_text.values()
    data["length"] = data["word"].apply(len)
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"

    sub_data = pd.DataFrame(columns = ("language", "frequency", "mean_word_length", "num_words"))
    sub_data["frequency"] = ["frequent", "infrequent", "unique"]
    sub_data["mean_word_length"] = data.groupby(['frequency']).mean()['length'].tolist()
    sub_data["num_words"] = data.groupby(['frequency']).size().tolist()
    sub_data["language"] = language

    return sub_data

def get_grouped_data():
    grouped_data = pd.DataFrame()

    for i in range(len(hamlets)) :
        language, text = hamlets.iloc[i]
        summarized_text = summarize_text(language, text)
        grouped_data = pd.concat([grouped_data, summarized_text], axis=0)
    return grouped_data

def plot_grouped_data():
    colors = {"Portuguese": "green", "English": "blue", "German": "red"}
    markers = {"frequent": "o","infrequent": "s", "unique": "^"}

    for i in range(grouped_data.shape[0]):
        row = grouped_data.iloc[i]
        plt.plot(row.mean_word_length, row.num_words,
            marker=markers[row.frequency],
            color = colors[row.language],
            markersize = 10
        )

    color_legend = []
    marker_legend = []
    for color in colors:
        color_legend.append(
            plt.plot([], [],
            color=colors[color],
            marker="o",
            label = color, markersize = 10, linestyle="None")
        )
    for marker in markers:
        marker_legend.append(
            plt.plot([], [],
            color="k",
            marker=markers[marker],
            label = marker, markersize = 10, linestyle="None")
        )
    plt.legend(numpoints=1, loc = "upper left")

    plt.xlabel("Mean Word Length")
    plt.ylabel("Number of Words")

    plt.show()

grouped_data = get_grouped_data()
print(plot_grouped_data())
