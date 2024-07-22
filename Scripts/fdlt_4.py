import pandas as pd

# Reading the Excel file
stem_data = pd.read_excel("./Data/Matand_2020_Stem_Data.xlsx")

# Converting 'Treatment' to a categorical type with specified order
stem_data['Treatment'] = pd.Categorical(stem_data['Treatment'], categories=["T1", "T5", "T10"], ordered=True)

# Filtering rows where 'Variety' contains "Alias", "Bright", or "Rococo"
stem_data2 = stem_data[stem_data['Variety'].str.contains("Alias|Bright|Rococo")]

# Displaying the first few rows of the original DataFrame
print(stem_data.head())