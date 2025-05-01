import subprocess
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_cleaning_pipeline():
    """Run the cleaning pipeline."""
    try:
        logger.info("Starting data cleaning...")
        subprocess.run(["python", "src/civictech/scripts/clean.py"], check=True)
        logger.info("Data cleaning completed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Cleaning pipeline failed: {e}")
        raise

def run_analysis_pipeline():
    """Run the analysis pipeline."""
    try:
        logger.info("Starting data analysis...")
        subprocess.run(["python", "src/civictech/scripts/analysis.py"], check=True)
        logger.info("Data analysis completed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Analysis pipeline failed: {e}")
        raise

def main():
    """Run the full pipeline: clean and then analyze."""
    try:
        run_cleaning_pipeline()
        run_analysis_pipeline()
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        raise

if __name__ == "__main__":
    main()
