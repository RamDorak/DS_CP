import pandas as pd
file_path='F:\\DS_CP\\DS_Final_data.xlsx' #Change the file path according to your pc

# For Batsmen
sheet1='Batsmen'
column_sort1='Impact(Bat)'
corresponding_col1='Player(Bat)'
df1=pd.read_excel("DS_Final_data.xlsx", sheet_name=sheet1)
df1_filtered = df1[df1['Mat'] > 10]
df1_sorted = df1_filtered.sort_values(by='Mat')
df1_sorted.to_excel('sorted_data.xlsx', index=False)
sorted1=df1_sorted.sort_values(by=column_sort1, ascending=False)
first_five_batsmen= sorted1[column_sort1].head(5)
corresponding_batters = sorted1.loc[sorted1[column_sort1].isin(first_five_batsmen), corresponding_col1]

# For wicketkeepers
sheet2='Wicketkeeper'
column_sort2='Impact(wk)'
corresponding_col2='Player(wk)'
df2=pd.read_excel(file_path, sheet_name=sheet2)
df2_filtered = df2[df2['Mat'] > 10]
df2_sorted = df2_filtered.sort_values(by='Mat')
df2_sorted.to_excel('sorted_data.xlsx', index=False)
sorted2=df2_sorted.sort_values(by=column_sort2, ascending=False)
first_two_keepers= sorted2[column_sort2].head(2)
corresponding_keepers = sorted2.loc[sorted2[column_sort2].isin(first_two_keepers), corresponding_col2]

# For Pacers
sheet3='Pacers'
column_sort3='Impact(Pace)'
corresponding_col3='Player(Pace)'
df3=pd.read_excel(file_path, sheet_name=sheet3)
df3_filtered = df3[df3['Mat'] > 10]
df3_sorted = df3_filtered.sort_values(by='Mat')
df3_sorted.to_excel('sorted_data.xlsx', index=False)
sorted3=df3_sorted.sort_values(by=column_sort3, ascending=False)
first_four_pacers= sorted3[column_sort3].head(4)
corresponding_Pacers = sorted3.loc[sorted3[column_sort3].isin(first_four_pacers), corresponding_col3]

# For Spinners
sheet4='Spinners'
column_sort4='Impact(Spin)'
corresponding_col4='Player(Spin)'
df4=pd.read_excel(file_path, sheet_name=sheet4)
df4_filtered = df4[df4['Mat'] > 10]
df4_sorted = df4_filtered.sort_values(by='Mat')
df4_sorted.to_excel('sorted_data.xlsx', index=False)
sorted4=df4_sorted.sort_values(by=column_sort4, ascending=False)
first_two_spinners= sorted4[column_sort4].head(2)
corresponding_Spinners = sorted4.loc[sorted4[column_sort4].isin(first_two_spinners), corresponding_col4]

# For allrounders
sheet5='all_rounders'
column_sort5='Overall_impact'
corresponding_col5='Player(ar)'
df5=pd.read_excel(file_path, sheet_name=sheet5)
df5_filtered = df5[df5['Mat'] > 10]
df5_sorted = df5_filtered.sort_values(by='Mat')
df5_sorted.to_excel('sorted_data.xlsx', index=False)
sorted5=df5_sorted.sort_values(by=column_sort5, ascending=False)
first_two_allrounders= sorted5[column_sort5].head(2)
corresponding_allrounders = sorted5.loc[sorted5[column_sort5].isin(first_two_allrounders), corresponding_col5]

# For printing ideal Squad of 15
print()
print("The ideal squad of 15 should be as follows:")
print("---------------------------------------------------------------")
print("Batsmen:")
print(corresponding_batters)
print("---------------------------------------------------------------")
print("Wicketkeepers:")
print(corresponding_keepers)
print("---------------------------------------------------------------")
print("All Rounders:")
print(corresponding_allrounders)
print("---------------------------------------------------------------")
print("Spinners:")
print(corresponding_Spinners)
print("---------------------------------------------------------------")
print("Pacers:")
print(corresponding_Pacers)
print("---------------------------------------------------------------")
print()

# Taking input from the user for the pitch type
print("Press 1 for flatrack pitch")
print("Press 2 for dry pitch")
print("Press 3 for wet pitch")
print("Press 4 for dusty pitch")
print("Press 5 for dead pitch")
print("Press 6 for green pitch")
print("---------------------------------------------------------------")
choice = int(input("Enter the Choice:"))

if choice==1:
    print("The ideal playing 11 should be as follows:")
    batsmen = sorted1[column_sort1].head(4)
    corresponding_batters = sorted1.loc[sorted1[column_sort1].isin(batsmen), corresponding_col1]
    print(corresponding_batters)
    print("---------------------------------------------------------------")
    keepers = sorted2[column_sort2].head(1)
    corresponding_keepers = sorted2.loc[sorted2[column_sort2].isin(keepers), corresponding_col2]
    print(corresponding_keepers)
    print("---------------------------------------------------------------")
    first_two_allrounders = sorted5[column_sort5].head(2)
    corresponding_allrounders = sorted5.loc[sorted5[column_sort5].isin(first_two_allrounders), corresponding_col5]
    print(corresponding_allrounders)
    print("---------------------------------------------------------------")
    first_two_spinners = sorted4[column_sort4].head(1)
    corresponding_Spinners = sorted4.loc[sorted4[column_sort4].isin(first_two_spinners), corresponding_col4]
    print(corresponding_Spinners)
    print("---------------------------------------------------------------")
    first_four_pacers = sorted3[column_sort3].head(3)
    corresponding_Pacers = sorted3.loc[sorted3[column_sort3].isin(first_four_pacers), corresponding_col3]
    print(corresponding_Pacers)
    print("---------------------------------------------------------------")
elif choice==2:
    print("The ideal playing 11 should be as follows")
    batsmen = sorted1[column_sort1].head(4)
    corresponding_batters = sorted1.loc[sorted1[column_sort1].isin(batsmen), corresponding_col1]
    print(corresponding_batters)
    print("---------------------------------------------------------------")
    keepers = sorted2[column_sort2].head(1)
    corresponding_keepers = sorted2.loc[sorted2[column_sort2].isin(keepers), corresponding_col2]
    print(corresponding_keepers)
    print("---------------------------------------------------------------")
    first_two_allrounders = sorted5[column_sort5].head(2)
    corresponding_allrounders = sorted5.loc[sorted5[column_sort5].isin(first_two_allrounders), corresponding_col5]
    print(corresponding_allrounders)
    print("---------------------------------------------------------------")
    first_two_spinners = sorted4[column_sort4].head(1)
    corresponding_Spinners = sorted4.loc[sorted4[column_sort4].isin(first_two_spinners), corresponding_col4]
    print(corresponding_Spinners)
    print("---------------------------------------------------------------")
    first_four_pacers = sorted3[column_sort3].head(3)
    corresponding_Pacers = sorted3.loc[sorted3[column_sort3].isin(first_four_pacers), corresponding_col3]
    print(corresponding_Pacers)
    print("---------------------------------------------------------------")
elif choice==3:
    print("If match occurs the playing 11 should be as follows:")
    batsmen = sorted1[column_sort1].head(4)
    corresponding_batters = sorted1.loc[sorted1[column_sort1].isin(batsmen), corresponding_col1]
    print(corresponding_batters)
    print("---------------------------------------------------------------")
    keepers = sorted2[column_sort2].head(1)
    corresponding_keepers = sorted2.loc[sorted2[column_sort2].isin(keepers), corresponding_col2]
    print(corresponding_keepers)
    print("---------------------------------------------------------------")
    first_two_allrounders = sorted5[column_sort5].head(2)
    corresponding_allrounders = sorted5.loc[sorted5[column_sort5].isin(first_two_allrounders), corresponding_col5]
    print(corresponding_allrounders)
    print("---------------------------------------------------------------")
    first_two_spinners = sorted4[column_sort4].head(2)
    corresponding_Spinners = sorted4.loc[sorted4[column_sort4].isin(first_two_spinners), corresponding_col4]
    print(corresponding_Spinners)
    print("---------------------------------------------------------------")
    first_four_pacers = sorted3[column_sort3].head(2)
    corresponding_Pacers = sorted3.loc[sorted3[column_sort3].isin(first_four_pacers), corresponding_col3]
    print(corresponding_Pacers)
    print("---------------------------------------------------------------")
elif choice==4:
    print("The ideal playing 11 should be as follows")
    batsmen = sorted1[column_sort1].head(4)
    corresponding_batters = sorted1.loc[sorted1[column_sort1].isin(batsmen), corresponding_col1]
    print(corresponding_batters)
    print("---------------------------------------------------------------")
    keepers = sorted2[column_sort2].head(1)
    corresponding_keepers = sorted2.loc[sorted2[column_sort2].isin(keepers), corresponding_col2]
    print(corresponding_keepers)
    print("---------------------------------------------------------------")
    first_two_allrounders = sorted5[column_sort5].head(2)
    corresponding_allrounders = sorted5.loc[sorted5[column_sort5].isin(first_two_allrounders), corresponding_col5]
    print(corresponding_allrounders)
    print("---------------------------------------------------------------")
    first_two_spinners = sorted4[column_sort4].head(2)
    corresponding_Spinners = sorted4.loc[sorted4[column_sort4].isin(first_two_spinners), corresponding_col4]
    print(corresponding_Spinners)
    print("---------------------------------------------------------------")
    first_four_pacers = sorted3[column_sort3].head(2)
    corresponding_Pacers = sorted3.loc[sorted3[column_sort3].isin(first_four_pacers), corresponding_col3]
    print(corresponding_Pacers)
    print("---------------------------------------------------------------")
elif choice==5:
    print("The ideal playing 11 should be as follows:")
    batsmen = sorted1[column_sort1].head(4)
    corresponding_batters = sorted1.loc[sorted1[column_sort1].isin(batsmen), corresponding_col1]
    print(corresponding_batters)
    print("---------------------------------------------------------------")
    keepers = sorted2[column_sort2].head(1)
    corresponding_keepers = sorted2.loc[sorted2[column_sort2].isin(keepers), corresponding_col2]
    print(corresponding_keepers)
    print("---------------------------------------------------------------")
    first_two_allrounders = sorted5[column_sort5].head(2)
    corresponding_allrounders = sorted5.loc[sorted5[column_sort5].isin(first_two_allrounders), corresponding_col5]
    print(corresponding_allrounders)
    print("---------------------------------------------------------------")
    first_two_spinners = sorted4[column_sort4].head(1)
    corresponding_Spinners = sorted4.loc[sorted4[column_sort4].isin(first_two_spinners), corresponding_col4]
    print(corresponding_Spinners)
    print("---------------------------------------------------------------")
    first_four_pacers = sorted3[column_sort3].head(3)
    corresponding_Pacers = sorted3.loc[sorted3[column_sort3].isin(first_four_pacers), corresponding_col3]
    print(corresponding_Pacers)
    print("---------------------------------------------------------------")
elif choice==6:
    print("The ideal playing 11 should be as follows:")
    batsmen = sorted1[column_sort1].head(4)
    corresponding_batters = sorted1.loc[sorted1[column_sort1].isin(batsmen), corresponding_col1]
    print(corresponding_batters)
    print("---------------------------------------------------------------")
    keepers = sorted2[column_sort2].head(1)
    corresponding_keepers = sorted2.loc[sorted2[column_sort2].isin(keepers), corresponding_col2]
    print(corresponding_keepers)
    print("---------------------------------------------------------------")
    first_two_allrounders = sorted5[column_sort5].head(2)
    corresponding_allrounders = sorted5.loc[sorted5[column_sort5].isin(first_two_allrounders), corresponding_col5]
    print(corresponding_allrounders)
    print("---------------------------------------------------------------")
    first_four_pacers = sorted3[column_sort3].head(4)
    corresponding_Pacers = sorted3.loc[sorted3[column_sort3].isin(first_four_pacers), corresponding_col3]
    print(corresponding_Pacers)
    print("---------------------------------------------------------------")
else:
    print("Invalid input try again")