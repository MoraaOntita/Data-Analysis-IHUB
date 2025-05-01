import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
from typing import Optional
from civictech.scripts import logger

def load_config(path: str = "src/civictech/scripts/config.yaml") -> dict:
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading config file: {e}")
        raise

def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

def save_plot(fig, filename: str, output_dir: str) -> None:
    try:
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, filename)
        fig.savefig(save_path, bbox_inches='tight')
        logger.info(f"Plot saved to {save_path}")
    except Exception as e:
        logger.error(f"Failed to save plot {filename}: {e}")
        raise

def plot_datasets_by_department(df: pd.DataFrame, output_dir: str) -> None:
    try:
        fig, ax = plt.subplots()
        df['Home_Department'].value_counts().plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title("Datasets by Department")
        ax.set_xlabel("Department")
        ax.set_ylabel("Number of Datasets")
        plt.xticks(rotation=45, ha='right')
        save_plot(fig, "datasets_by_department.png", output_dir)
        plt.close()
    except Exception as e:
        logger.error(f"Failed to plot datasets by department: {e}")

def plot_data_classification(df: pd.DataFrame, output_dir: str) -> None:
    try:
        fig, ax = plt.subplots()
        df['Data_Classification'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        ax.set_title("Data Classification")
        ax.set_ylabel('')
        save_plot(fig, "data_classification.png", output_dir)
        plt.close()
    except Exception as e:
        logger.error(f"Failed to plot data classification: {e}")

def plot_format_distribution(df: pd.DataFrame, output_dir: str) -> None:
    try:
        fig, ax = plt.subplots()
        sns.barplot(x=df['Data_Format'].value_counts().values,
                    y=df['Data_Format'].value_counts().index,
                    ax=ax, palette='pastel')
        ax.set_title("Data Format Distribution")
        ax.set_xlabel("Number of Datasets")
        ax.set_ylabel("Data Format")
        save_plot(fig, "data_format_distribution.png", output_dir)
        plt.close()
    except Exception as e:
        logger.error(f"Failed to plot format distribution: {e}")

def plot_update_frequency(df: pd.DataFrame, output_dir: str) -> None:
    try:
        fig, ax = plt.subplots()
        sns.barplot(x=df['Frequency_of_Data_Change'].value_counts().values,
                    y=df['Frequency_of_Data_Change'].value_counts().index,
                    ax=ax, palette='muted')
        ax.set_title("Frequency of Data Updates")
        ax.set_xlabel("Number of Datasets")
        ax.set_ylabel("Update Frequency")
        save_plot(fig, "update_frequency.png", output_dir)
        plt.close()
    except Exception as e:
        logger.error(f"Failed to plot update frequency: {e}")

def plot_geo_coordinates(df: pd.DataFrame, output_dir: str) -> None:
    try:
        geo_coord = df['Geographic_Granularity'].fillna('').apply(
            lambda x: 'Includes Coordinates' if 'latitude' in x.lower() or 'longitude' in x.lower() else 'No Coordinates'
        )
        fig, ax = plt.subplots()
        geo_coord.value_counts().plot(kind='bar', ax=ax, color='green')
        ax.set_title("Geographic Coordinate Availability")
        ax.set_xlabel("Geo Coordinate Presence")
        ax.set_ylabel("Number of Datasets")
        save_plot(fig, "geo_coordinates.png", output_dir)
        plt.close()
    except Exception as e:
        logger.error(f"Failed to plot geographic coordinates: {e}")

def plot_missing_metadata(df: pd.DataFrame, output_dir: str) -> None:
    try:
        missing_desc = df['Brief_Description_of_Data'].str.lower().str.contains('no description', na=True)
        missing_link = df['Link_to_Existing_Publication'].str.lower().str.contains('no link', na=True)
        missing_summary = pd.Series({
            'Missing Description': missing_desc.sum(),
            'Missing Link': missing_link.sum()
        })
        fig, ax = plt.subplots()
        missing_summary.plot(kind='bar', ax=ax, color='salmon')
        ax.set_title("Datasets Missing Metadata")
        ax.set_ylabel("Number of Datasets")
        save_plot(fig, "missing_metadata.png", output_dir)
        plt.close()
    except Exception as e:
        logger.error(f"Failed to plot missing metadata: {e}")

def plot_time_span(df: pd.DataFrame, output_dir: str) -> None:
    try:
        fig, ax = plt.subplots()
        time_span_counts = df['Time_Span'].fillna('Unknown').value_counts()
        sns.barplot(x=time_span_counts.values, y=time_span_counts.index, ax=ax, palette='coolwarm')
        ax.set_title("Time Span Coverage")
        ax.set_xlabel("Number of Datasets")
        ax.set_ylabel("Time Span")
        save_plot(fig, "time_span_coverage.png", output_dir)
        plt.close()
    except Exception as e:
        logger.error(f"Failed to plot time span: {e}")

def main() -> None:
    sns.set(style="whitegrid")
    config = load_config()
    try:
        input_path = config['analysis']['input_path']
        output_dir = config['analysis']['visuals_output_dir']
        df = load_data(input_path)

        plot_datasets_by_department(df, output_dir)
        plot_data_classification(df, output_dir)
        plot_format_distribution(df, output_dir)
        plot_update_frequency(df, output_dir)
        plot_geo_coordinates(df, output_dir)
        plot_missing_metadata(df, output_dir)
        plot_time_span(df, output_dir)

    except Exception as e:
        logger.error(f"Analysis failed: {e}")

if __name__ == "__main__":
    main()
