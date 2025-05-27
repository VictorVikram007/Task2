import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv('/content/Titanic-Dataset.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Fare'].fillna(df['Fare'].median(), inplace=True)
df.drop(columns=['Cabin'], inplace=True)
df.dropna(inplace=True)

df.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

sns.boxplot(x='Survived', y='Age', data=df)
plt.show()

sns.boxplot(x='Pclass', y='Fare', data=df)
plt.show()

numeric_df = df.select_dtypes(include=['number'])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']])
plt.show()

fig = px.histogram(df, x='Age', nbins=30, title='Age Distribution of Passengers')
fig.show()
fig = px.box(df, x='Survived', y='Age', color='Survived', title='Age Distribution by Survival')
fig.show()


numeric_df = df.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr().round(2)

fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Viridis'))

fig.update_layout(title='Correlation Heatmap (Plotly)', xaxis_title="Features", yaxis_title="Features")
fig.show()
fig = px.scatter(df, x='Age', y='Fare', color='Survived', title='Fare vs Age Colored by Survival')
fig.show()



print(df.skew(numeric_only=True))
