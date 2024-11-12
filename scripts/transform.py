import pandas as pd

def transform_movie_data(movies):
    df = pd.DataFrame(movies)

    df = df[['id', 'title', 'release_date', 'vote_average', 'vote_count', 'popularity', 'overview', 'genre_ids']]

    # drop the rows where title or release_date are missing
    df = df.dropna(subset=['title', 'release_date'])

    # convert the release_date column to datetime format
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    # make sure numeric columns have the right type
    df[['vote_average', 'vote_count', 'popularity']] = df[['vote_average', 'vote_count', 'popularity']].apply(pd.to_numeric, errors='coerce')

    # have to convert the genre_ids list to a string to be able to store it in the database
    df['genre_ids'] = df['genre_ids'].apply(lambda x: ','.join(map(str, x)) if isinstance(x, list) else '')

    # drop the rows with invalid release_dates or numeric values
    df = df.dropna().reset_index(drop=True)

    return df


# Testing the function
if __name__ == "__main__":
    from extract import extract_movie_data
    raw_data = extract_movie_data()
    transformed_data = transform_movie_data(raw_data)
    pd.set_option('display.max_columns', None)
    print(transformed_data.head(3))
    pd.reset_option('display.max_columns')