# Section 1: Critical Thinking, Research and Analytical Skills Testing

**Steps to take to curate credible secondary datasets that support research work.**
1. Defining the Research objectives.
   First understanding the goal of the research then defining the research questions or hypothesis that will guide you. By defining the research objectives, it helps you to quickly and efficiently identify the data you might need to boost up and support the research work.

2. Identifying Potential Data Sources.
   Look for reputable data sources that are accurate, quality data and reliable. They can be from academic institutions, government agencies, international organizations and reliable journals and publications. The data obtained should be relevant to the research that is being carried out.


3. Evaluate the Credibility.
    One of the ways to evaluate the credibility of the data obtained is using the CRAAP test. It is an acronym for:    
   - **Currency** - Is the data up to date?
   - **Relevance** - Is the data related to your research question?
   - **Authority** - Who is the author or publisher? What is their reputation?
   - **Accuracy** - Is the data supported by evidence or peer-reviewed?
   - **Purpose** - Why is the data collected? Is there any potential bias?


4. Check the Data Quality:
    Check if the data has any missing information or incomplete data, if it is consistent, if it has anomalies, and if it is accurate. Check also if the data has proper documentation and metadata


5. Document and organize the Data:
    Have documentation for every dataset collected. It should contain the source of information, method of data collection and any analysis or transformations that may have been collected. This should help in maintaining transparency and reproducibility in the research.

6. Seek Expert Consultation
    If unsure about the dataset on how to interprate it you can get an expert to help you and give clarity and insights that will enhance the quality of your research.


**Extract Data from Identified Sources**

Before extracting data review the data format and Access Method. Different sources have their data in different format and not all data available is free to use. Some maybe available for public use others may have restrictions. 

Some of the ways to extract data are:

1. Downloading esp from the public datasets. You can get it as a csv, excel, json, or API endpoints
2. Web Scraping. Used when extracting data from websites. Some of the python libraries used eb scraping include BeautifulSoup, Scrapy and Selenium
3. API Intergration. Tools like requests in python help in pulling data from different APIs.
4. SQL Querying. This is for when you are extracting data from a relational database.
5. File parsing. For extracting data from text files, PDFs, and other document formats. 


**Clean and prepare the data for analysis**
Some of the ways to clean your data is
    1. Standardizing Formats. This includes but not limited to; converting date and time fields, unified location naming, currency and currency symbol, adresses, phone numbers, categorical values and when dealing with text data, inconsistencies in spelling, capitalization, and formatting

    2. Handling Missing Values. Some of the ways to handle the missing values are; droping them (especially if you feel it will have not impact on the data), impute data (you can either fill it with the mean, median, mode, or advanced algorithm technique) and you can treat the missing data as features that can help you in the analysis.

    3. Removing DUplicate and Inconsistencies. One of the mot common tool in python can can help in this is pandas. it helps in locating and removing any duplicates and invalid records epecially when working with structured data.

    4. Correct Formating. Ensuring that the data is represented in the correct format. Be it a Float, interger, boolean or date/time

    5. Handling Outliers. OUtliers can distort an analysis leading to mileading conclusions. it can be deteceted uing visualization tools such as boxplot, Interquartile Range (IQR) Method, or histogram. Outliers can also be removed/deleted, imputed, or do Standard Scaling to reduce the impact of the outliers.

    6. Feature Engineering - Deriving new features/fields form existing ones


