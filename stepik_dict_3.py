import pandas as pd

def average_marks():
    df = pd.read_csv('C:\\Users\playboi carti\Downloads\dataset_3363_4.txt', sep=';', header=None)
    df.rename(columns={0: 'name', 1: 'math', 2: 'physics', 3: 'russian'}, inplace=True)
    df['Average'] = df.mean(axis=1)
    answer_df = df['Average']
    answer_df.to_csv(r'C:\\Users\playboi carti\Downloads\data.txt', header=None, index=None, sep=' ', mode='a')
    average_of_columns = df['math'].mean(), df['physics'].mean(), df['russian'].mean()
    average_mark = open('C:\\Users\playboi carti\Downloads\data.txt', 'a')
    average_mark.write(str(average_of_columns))
    average_mark.close()
average_marks()