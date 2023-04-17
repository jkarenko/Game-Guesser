import os
import gzip
import urllib.request
import pandas as pd


class IMDBReader:
    def __init__(self, files, type):
        self.titles = self.read_imdb_data(files, type)

    def read_imdb_data(self, file_names, type):
        for file_name in file_names:
            if not os.path.exists(file_name):
                self.download_file(file_name)

        basics_file_name = file_names[0]
        ratings_file_name = file_names[1]
        # akas_file_name = file_names[2]

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

        df_basics = pd.read_csv(basics_file_name, dtype=dtype, sep="\t", low_memory=False, na_values="\\N")
        df_basics["genres"] = df_basics["genres"].str.split(',')
        df_ratings = pd.read_csv(ratings_file_name, sep="\t", na_values="\\N")
        # df_akas = pd.read_csv(akas_file_name, sep="\t", na_values="\\N")
        df = pd.merge(df_basics, df_ratings, on='tconst')
        print(f"type: {type}")
        filtered_df = df[
            (df["startYear"] > 1975) & (
                    df["titleType"] == type) & (
                    df["averageRating"] > 8.0) & (
                    df["numVotes"] > 100)
            ]
        print(f"Found {len(filtered_df)} titles matching the criteria...")
        return filtered_df[["originalTitle", "startYear", "genres", "averageRating", "numVotes", "titleType"]]

    def get_titles(self):
        print("Getting 5 random titles from the dataset...")
        sample_5 = self.titles.sample(5)
        return [f"{row.originalTitle} ({row.startYear})" for _, row in sample_5.iterrows()]

    @staticmethod
    def download_file(file_name):
        url = f"https://datasets.imdbws.com/{file_name}.gz"
        print(f"Downloading and unzipping {url}...")
        gz_file_name = "title.basics.tsv.gz"
        urllib.request.urlretrieve(url, gz_file_name)

        with gzip.open(gz_file_name, 'rb') as gz_file:
            with open(file_name, 'wb') as tsv_file:
                tsv_file.write(gz_file.read())

        os.remove(gz_file_name)
