import pandas as pd


def calculate_ranking(df):
    ranking = df[['restaurant', 'score']].groupby('restaurant').mean()['score']
    ranking = ranking.sort_values(ascending=False).reset_index()

    ranking['score'] = round(ranking['score'], 1)
    ranking['Rank'] = range(1, len(ranking) + 1)
    ranking = ranking.reindex(columns=['Rank', 'restaurant', 'score'])
    ranking = ranking.rename(columns={'restaurant': 'Restaurant', 'score': 'Final Score'})

    return ranking.head(5)


def count_unique_votes(df):
    return df['name'].nunique()
