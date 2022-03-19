import argparse
import numpy as np
import pandas as pd


def get_data(path: str, name: str):
    '''Grabs stance and body csv files from original dataset and joins them
       to one dataframe.
    
    Args:
        path (str): parent folder of files
        name (str): type of csv to grab ('train' or 'test')
    
    Returns:
        pandas.core.frame.DataFrame of joined bodies and stances
    '''
    stances = pd.read_csv(f'{path}/{name}_stances.csv')
    bodies = pd.read_csv(f'{path}/{name}_bodies.csv')
    
    data = stances.join(bodies.set_index('Body ID'), on='Body ID')
    
    data['related'] = add_related_label(data)
    
    return data


def add_related_label(df: pandas.core.frame.DataFrame):
    '''Adds column to dataframe whether body is related to stance'''
    df['related'] = np.where(df['Stance']!= 'unrelated', True, False)
    return df


def save_data(output: str, train_df: pandas.core.frame.DataFrame,
              test_df: pandas.core.frame.DataFrame):
    '''Save csv to output directory
    
    Args:
        output (str): Output directory to save csv
        train_df(pandas.core.frame.DataFrame): dataframe of training set
        test_df(pandas.core.frame.DataFrame): dataframe of competition test set
    '''
    Path(output).mkdir(parents=True, exist_ok=True)

    train_df.to_csv(f'{output}/train.csv', index=False, encoding='utf-8')

    test_df.to_csv(f'{output}/test.csv', index=False, encoding='utf-8')


def main(input_dir: str, output_dir: str):
    train_df = get_data(input_dir, 'train')
    test_df = get_data(input_dir, 'competition_test')
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", help="path to input fake news challenge directory",
                        action="store")
    parser.add_argument("-o", "--output-dir", help="path to saved processed csvs",
                        action="store")

    args = parser.parse_args()
    
    main(input_dir=args.input_dir, output_dir=args.output_dir)
