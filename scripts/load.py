import pandas as pd
from sqlalchemy import create_engine

def load_movie_data(df):
    engine = create_engine("sqlite:///movies.db")

    df.to_sql("movies", con = engine, if_exists="replace", index=False)

    print("Data successfully loaded into database")

# Testing the function
if __name__ == "__main__":
    from transform import transform_movie_data
    from extract import extract_movie_data

    raw_data = extract_movie_data()
    transformed_data = transform_movie_data(raw_data)
    load_movie_data(transformed_data)