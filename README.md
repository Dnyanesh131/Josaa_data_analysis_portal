# Project Name: JOSAA Data Analysis Portal

This project aims to develop a web portal for exploring JOSAA (Joint Seat Allocation Authority) seat allotment statistics. The portal utilizes Python web scraping libraries to extract data from the JOSAA website. The data is then cleaned using NumPy and Pandas, and a database is created for efficient querying and analysis. The portal presents insightful observations through Exploratory Data Analysis (EDA) using Matplotlib and Seaborn. Interactive charts and tables are used to visualize trends such as branch opening and closing, as well as gender flow among IITs.

## Project Overview

The project includes the following key features:

- Web scraping JOSAA data using Python libraries.
- Cleaning the extracted data using NumPy and Pandas.
- Creating a database for efficient querying and analysis.
- Performing Exploratory Data Analysis (EDA) using Matplotlib and Seaborn.
- Presenting insightful observations through interactive charts and tables on the web portal using Chart.js.

## Tech Stack/Frameworks

The project utilizes the following technologies:

- Frontend: HTML, CSS, JavaScript
- Backend: Django, SQLite
- Data Scraping: Beautiful Soup, Selenium
- Data Cleaning: NumPy, Pandas
- Data Visualization: Matplotlib, Seaborn, Chart.js

## Project Files

The project includes the following files:

- `django_Josaa`: Contains the Django project files.
- `josaa_portal`: Includes the code for applying queries, data cleaning, and web portal frontend.
- `.gitignore`: Specifies which files and directories should be ignored by version control.
- `db.sqlite3`: The SQLite database file.
- `manage.py`: The Django project management script.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/your-repository.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Start the Django development server: `python manage.py runserver`
4. Access the portal in your web browser at: `http://localhost:8000`
