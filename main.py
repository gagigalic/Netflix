import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

netflix_data = pd.read_csv("netflix_titles.csv")
print(netflix_data.head())

#shape
shape = netflix_data.shape
print(shape)

#columns
columns = netflix_data.columns
print(columns)

#info
info = netflix_data.info()
print(info)

#describe
describe = netflix_data.describe()

#checking if there any Null value
print(netflix_data.isnull().sum())

sns.heatmap(netflix_data.isnull())
plt.savefig("heatmap.png")
plt.close()

#checking if there anu duplicate values
print(netflix_data.duplicated().sum())

#unique values
type = netflix_data["type"].unique()
print(type)

ratings = netflix_data["rating"].unique()
print(ratings)

release_year = netflix_data["release_year"].unique()
print(ratings)

listed_in = netflix_data["listed_in"].nunique()
print(listed_in)

type_numbers = netflix_data["type"].value_counts()
print(type_numbers)

#numbers movies vs tv shows
sns.countplot(data=netflix_data, x="type")
plt.savefig("plot.png")
plt.close()

netflix_data["type"].value_counts().plot(kind = "pie", autopct = "%.2f")
plt.savefig("pie.png")
plt.close()

#ratings in each category
plt.figure(figsize = (20, 5))
plt.style.use('seaborn-whitegrid')
ax = sns.countplot(x = 'rating', data = netflix_data)
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation = 45)
plt.savefig("plot2.png")
plt.close()

#checking how many movies/tv shows relase each year
plt.figure(figsize = (25, 8))
plt.style.use('seaborn-whitegrid')
ax = sns.countplot(x = 'release_year', data = netflix_data, palette = "Accent")
plt.xlabel('Year of Release')
plt.ylabel('Count')
plt.xticks(rotation = 45)
plt.savefig("plot3.png")
plt.close()

#Changing "date_added" column type from object to datetime

netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'])
print(netflix_data.dtypes)

#histogram of how many movies/tv shows added in netflix each year
netflix_data["date_added"].hist()
plt.savefig("plot4.png")
plt.close()

#how many tv shows released in 1995
tvshow_1995  = netflix_data[(netflix_data["type"] == "TV Show") & (netflix_data["release_year"] == 1995)]
print(tvshow_1995)

#histogram of how many movies/tv shows released each year
netflix_data["release_year"].hist()
plt.savefig("plot5.png")
plt.close()

#what is the number of movies made in japan
movies_only_in_japan = netflix_data[(netflix_data["type"] == "Movie") & (netflix_data["country"] == "Japan")]["title"]
print(movies_only_in_japan.count())

#Working with Date
netflix_data["date_added_month"] = netflix_data["date_added"].dt.month.fillna(-1)
print(netflix_data.columns)
print(netflix_data["date_added_month"])

#checking the number of content added month-wise
plt.figure(figsize = (15, 5))
ax = sns.countplot(x = 'date_added_month', data = netflix_data)
plt.xlabel('Month Content Added')
plt.ylabel('Count')
plt.savefig("plot6.png")
plt.close()

netflix_data["date_added_day"] = netflix_data["date_added"].dt.day.fillna(-1)
print(netflix_data.columns)
print(netflix_data["date_added_day"])

#checking the number of content added day-wise
plt.figure(figsize = (18, 6))
ax = sns.countplot(x = 'date_added_day', data = netflix_data)
plt.xlabel('Day Content Added')
plt.ylabel('Count')
plt.savefig("plot7.png")
plt.close()

#scatter plot for content released per year vs month
sns.scatterplot(data = netflix_data, x = "release_year", y = "date_added_month", hue = "type")
plt.savefig("plot8.png")
plt.close()

#Working with Country

country_count = netflix_data.copy()
country_count = pd.concat([country_count, netflix_data["country"].str.split(",", expand = True)], axis = 1)

country_count = country_count.melt(id_vars = ["type", "title"], value_vars = range(12), value_name = "country")
country_count = country_count[country_count["country"].notna()]
print(country_count)

#unique
print(country_count["country"].nunique())

country_count["country"] = country_count["country"].str.strip()

#top 30 Countries where most of the movies and tv show are produced
plt.figure(figsize = (15, 7))
country = country_count["country"].value_counts()[:30]
sns.barplot(x = country, y = country.index, palette = "Accent")
plt.xlabel("Count")
plt.savefig("plot9.png")
plt.close()


#plotting heatmap between content rating vs type
colormap = plt.cm.plasma
sns.heatmap(pd.crosstab(netflix_data["rating"], netflix_data["type"]), cmap = colormap)
plt.savefig("heatmap2.png")
plt.close()

#clustermap
sns.clustermap(pd.crosstab(netflix_data["rating"], netflix_data["type"]))
plt.savefig("clustermap.png")
plt.close()

#Working with Cast
cast_count = netflix_data.copy()
cast_count = pd.concat([cast_count, netflix_data["cast"].str.split(",", expand = True)], axis = 1)

cast_count = cast_count.melt(id_vars = ["type", "title"], value_vars = range(50), value_name = "cast")
cast_count = cast_count[cast_count["cast"].notna()]

print(cast_count)

#unique
print(cast_count["cast"].nunique())

#top 20 actors who involved in most number of Movies/Tv show
plt.figure(figsize = (20, 12))
cast = cast_count["cast"].value_counts()[:20]
sns.barplot(x = cast, y = cast.index, palette = "gist_ncar")
plt.savefig("plot10.png")
plt.close()

#number of movies where Robert De Niro acted
new = netflix_data.dropna()
x = new[new["cast"].str.contains("Robert De Niro")]
print(x["title"].count())
