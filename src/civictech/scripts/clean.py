import os
import re
import yaml
import logging
import pandas as pd
from typing import List, Dict
from civictech.scripts import logger

def load_config(path: str) -> Dict:
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load config file at {path}: {e}")
        raise

def load_data(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        logger.error(f"Data file not found at path: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading data file: {e}")
        raise

def clean_text_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    for col in columns:
        df[col] = df[col].astype(str).str.strip().str.replace(r'[\n\r]+', ' ', regex=True)
    return df

def standardize_capitalization(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    for col in columns:
        df[col] = df[col].str.title()
    return df

def clean_time_span(span: str) -> str:
    try:
        if pd.isna(span) or span.lower() in ['nan', 'none']:
            return 'Not specified'
        span = span.strip()
        if re.fullmatch(r'\d{4}-', span):
            return span.replace('-', ' to present')
        if re.fullmatch(r'\d{4}-\d{4}', span):
            return span.replace('-', ' to ')
        return span
    except Exception:
        return 'Not specified'

def clean_dataframe(df: pd.DataFrame, config: Dict) -> pd.DataFrame:
    df.drop(columns=config['columns']['drop'], inplace=True, errors='ignore')

    for col, fill_value in config['fillna'].items():
        df[col] = df[col].fillna(fill_value)

    text_columns = list(config['fillna'].keys())
    df = clean_text_columns(df, text_columns)

    df = standardize_capitalization(df, ['Home_Department', 'Home_Department_Division', 'Data_Source', 'Data_Format'])

    df['Time_Span'] = df['Time_Span'].apply(clean_time_span)
    
    return df

def save_dataframe(df: pd.DataFrame, output_path: str) -> None:
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info(f"Cleaned CSV saved to: {output_path}")
    except Exception as e:
        logger.error(f"Error saving cleaned CSV: {e}")
        raise

def main():
    try:
        config_path = os.path.join("src", "civictech", "scripts", "config.yaml")
        config = load_config(config_path)

        raw_csv_path = config['data']['raw_csv_path']
        output_path = config['data']['cleaned_csv_path']

        df = load_data(raw_csv_path)
        df = clean_dataframe(df, config)
        save_dataframe(df, output_path)
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
