import os
import gzip
import urllib.request
import pandas as pd


def imdb_reader(file_name):
    if not os.path.exists(file_name):
        download_file(file_name)

    dtype = {
        "tconst": str,
        "titleType": str,
        "primaryTitle": str,
        "originalTitle": str,
        "isAdult": 'Int64',
        "startYear": 'Int64',
        "endYear": 'Int64',
        "genres": str
    }

    df = pd.read_csv(file_name, dtype=dtype, sep="\t", low_memory=False, na_values="\\N")
    df["genres"] = df["genres"].str.split(',')
    filtered_df = df[(df["startYear"] > 1980) & (df["titleType"] == "movie")]
    titles = filtered_df[["originalTitle", "startYear", "genres"]]
    sample_5 = titles.sample(5)
    return [f"{row.originalTitle} ({row.startYear})" for _, row in sample_5.iterrows()]


def download_file(file_name):
    url = f"https://datasets.imdbws.com/{file_name}.gz"
    print(f"Downloading and unzipping {url}...")
    gz_file_name = "title.basics.tsv.gz"
    urllib.request.urlretrieve(url, gz_file_name)

    with gzip.open(gz_file_name, 'rb') as gz_file:
        with open(file_name, 'wb') as tsv_file:
            tsv_file.write(gz_file.read())

    os.remove(gz_file_name)
