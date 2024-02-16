
## Problem Statement
The aim is to design a thorough data engineering solution capable of consolidating, organizing, and facilitating access to an extensive collection of finance professional development materials. This endeavor seeks to enrich the learning journey of finance professionals by introducing an intelligent application interface for seamless interaction with carefully curated finance resources.

## Project Goals
Your objective is to establish two core datasets derived from the 224 refresher readings cataloged on the CFA Institute’s website and the accompanying topic outlines (included as PDF files). These readings hold significant value for finance professionals seeking to refine their financial acumen. The resulting datasets will form the foundation for an intelligent application tailored specifically for these professionals.

## Technologies Used
Web Scraping: Beautiful Soup, Scrapy
PDF Extraction: PyPDF2, Grobid
Database Upload: SQLAlchemy, Snowflake
Cloud Storage Integration: AWS S3
Python
Data Sources


## Project Structure
```
.
├── README.md
├── Step 1
│   ├── ReadMe.md
│   ├── Scraper_cfainstitute-step-1.ipynb
│   ├── requirements.txt
│   └── scrapper.py
├── Step 2
│   ├── 2024-l1-topics-combined-2.pdf
│   ├── 2024-l2-topics-combined-2.pdf
│   ├── 2024-l3-topics-combined-2.pdf
│   ├── Big_Data_Assignment2_step2.ipynb
│   ├── Grobid
│   │   ├── Grobid_RR_2024_l1_combined.txt
│   │   ├── Grobid_RR_2024_l2_combined.txt
│   │   └── Grobid_RR_2024_l3_combined.txt
│   ├── Metadata
│   │   ├── Grobid_RR_2024_l1_combined_metadata.json
│   │   ├── Grobid_RR_2024_l2_combined_metadata.json
│   │   └── Grobid_RR_2024_l3_combined_metadata.json
│   ├── PyPDF
│   │   ├── PyPDF_RR_2024_l1_combined.txt
│   │   ├── PyPDF_RR_2024_l2_combined.txt
│   │   └── PyPDF_RR_2024_l3_combined.txt
│   ├── README.md
│   ├── config.json
│   ├── getting_metadata.py
│   ├── main.py
│   └── requirement.txt
├── Step 3
│   ├── README.md
│   ├── data_upload_to_snowflake__using_sqlalchemy 1.ipynb
│   └── snowflake.py
├── Step 4
│   ├── Big_Data_Assignment2_step4.ipynb
│   ├── CSV
│   │   └── refresher_readings.csv
│   ├── Grobid
│   │   ├── Grobid_RR_2024_l1_combined.txt
│   │   ├── Grobid_RR_2024_l2_combined.txt
│   │   └── Grobid_RR_2024_l3_combined.txt
│   ├── PyPDF
│   │   ├── PyPDF_RR_2024_l1_combined.txt
│   │   ├── PyPDF_RR_2024_l2_combined.txt
│   │   └── PyPDF_RR_2024_l3_combined.txt
│   ├── README.md
│   ├── requirement.txt
│   └── s3_upload.py
├── architecture.py
├── architecture_diagram.png
└── asset
    ├── csv-file-format8052.jpg
    ├── pdf_file.png
    └── txt-file.png
```

*You can generate the project tree using following tools*
*[Project Tree Generator](https://woochanleee.github.io/project-tree-generator)*
*[Generate from terminal](https://www.geeksforgeeks.org/tree-command-unixlinux/)*

## How to run Application locally

Execute the files as per step numbers

## References
•	https://www.cfainstitute.org/membership/professional-development/refresher-readings/time-series-analysis
•	https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending
•	https://www.snowflake.com/en/
     
## Learning Outcomes
Hands-on experience with Web Scraping Techniques
Proficiency in Data Extraction from PDFs
Understanding of Database Management and Integration
Familiarity with Cloud Storage Integration

## Team Information and Contribution 

Name | Contribution %| Contributions |
--- |--- | --- |
Aniket Giram    | 40% |Step 2, Step 4 |
Sudarshan Dudhe | 30% |Step 1 |
Rasika Kole     | 30% |Step 3 |
