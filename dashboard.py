from plotnine import ggplot, aes, geom_point, theme_minimal, labs
import matplotlib.pyplot as plt
from plotnine import ggplot, aes, geom_bar, theme_minimal, labs, theme, element_text
from plotnine import ggplot, aes, geom_boxplot, theme_minimal, labs, scale_fill_manual, theme, element_text
import pandas as pd

df = pd.read_csv('df_salaries.csv')


top_job_titles = df['job_title'].value_counts().nlargest(4).index
df['job_title_grouped'] = df['job_title'].apply(
    lambda x: x if x in top_job_titles else 'Other')

# Plotting using plotnine
plot = (
    ggplot(df, aes(x='job_title_grouped', y='salary_in_usd', fill='gender')) +
    geom_boxplot() +
    labs(title='Boxplot of Salary by Gender and Job Type', x='Job Type', y='Salary (USD)') +
    theme_minimal() +
    scale_fill_manual(values={'Male': 'blue', 'Female': 'pink'}) +
    # Set the angle to 45 degrees
    theme(axis_text_x=element_text(angle=45, hjust=1))
)

# Show the plot
print(plot)


top_job_titles = df['job_title'].value_counts().nlargest(4).index
df['job_title_grouped'] = df['job_title'].apply(
    lambda x: x if x in top_job_titles else 'Other')

# Plotting using plotnine
plot = (
    ggplot(df, aes(x='job_title_grouped', y='weekly_hours', fill='experience_level')) +
    geom_bar(stat='identity', position='dodge') +
    labs(title='Weekly Hours per Job Title and Experience Level',
         x='Job Title', y='Weekly Hours') +
    theme_minimal() +
    # Set the angle to 45 degrees
    theme(axis_text_x=element_text(angle=45, hjust=1))
)

# Show the plot
print(plot)


df['remote_category'] = df['remote_ratio'].map(
    {0: 'Face-to-Face (f2f)', 50: 'Hybrid', 100: 'Remote'})

# Count occurrences of each category
category_counts = df['remote_category'].value_counts()

# Plotting using matplotlib
plt.pie(category_counts, labels=category_counts.index,
        autopct='%1.1f%%', startangle=90, colors=['red', 'green', 'blue'])
plt.title('Remote Ratio Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()


plot = (
    ggplot(df, aes(x='company_size', y='salary_in_usd')) +
    geom_point() +
    labs(title='Company Size vs Salary',
         x='Company Size', y='Salary (USD)') +
    theme_minimal()
)

# Show the plot
print(plot)
