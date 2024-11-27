# Movie Data ETL Pipeline using TMDB API


## Project Overview
The pipeline is designed to automate the retrieval and processing of movie data, making it easy to analyze and query. Apache Airflow is used for scheduling and managing the ETL workflow, ensuring efficient data processing and automation.

### Key Features 
- **Data Extraction**: Uses the `requests` library to fetch movie data from TMDB API.
- **Data Transformation**: Cleans and processes the raw data using `pandas`, handling missing values and formatting data types.
- **Data Loading**: Stores the cleaned data into an SQLite database using `SQLAlchemy`.
- **Workflow Automation**: Apache Airflow orchestrates the ETL process, running it on a scheduled basis.

## Technologies Used
- **Python**: Core programming language for the ETL pipeline.
- **TMDB API**: Data source for fetching movie information.
- **Pandas**: Used for data manipulation and cleaning.
- **SQLAlchemy**: Database toolkit for loading and managing data.
- **Apache Airflow**: Orchestration tool for automating and scheduling the ETL process.
- **dotenv**: Manages environment variables to keep sensitive information secure.

## Project Structure
```{bash}
movie-etl-pipeline/
│
├── dags/
│   └── movie_etl_dag.py      # Airflow DAG for the ETL process
│
├── scripts/
│   ├── extract.py            # Script to handle data extraction
│   ├── transform.py          # Script to handle data transformation
│   └── load.py               # Script to handle data loading
│
├── config/
│   └── config.py             # Configuration file for environment variables
│
├── .env                      # Environment file (not uploaded to GitHub)
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## Setup
1. **Clone the repository**:
   ```{bash}
    git clone https://github.com/Moonyar/TMDB_ETL.git
    cd TMDB_ETL
   ```
2. **Set up a virtual environment**:
    ```{bash}
   python -m venv venv
   venv\Scripts\activate  # for Windows
   source venv/bin/activate # for MacOS/Linux
    ```
3. **Install dependencies**:
    ```{bash}
   pip install -r requirements.txt
    ```
4. **Set up your TMDB API key**:
    - create a .env file in the root directory and add your TMDB API key like so:
   ```{dotenv}
   TMDB_API_KEY=INSTERT YOUR API KEY HERE
   ```
5. **initialize Airflow**:
    ```{bash}
   set AIRFLOW_HOME=~/airflow  # (use 'export' for Linux)
   airflow db init
   #### Fill out the following with your information #####
   airflow users create --username admin --firstname YourName --lastname YourLastName --role Admin --email email@example.com
    ```
6. **Run the Airflow web server and scheduler**:
    ```{bash}
    airflow webserver --port 8080
    airflow scheduler 
    ```
7. **Trigger the ETL Pipeline**:
    - open Airflow web interface at http://localhost:8080
    - either trigger DAG manually or wait for it to run on the scheduled interval

## Usage
- Analyze movie data: using the data we can do various analyses. such as finding popular movies, analyzing trends, or creating visuals

## Future Enhancements
- Add support for more TMDB API endpoints like trendings movies and TV shows
- Implement data quality checks and more error handling to improve readability
- visualize movie insights using Matplotlib and Tableau
- Deploy the pipeline using a cloud-based solution for scalability


## License 
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Thanks to The Movie Database (TMDB) for providing the API.
- Apache Airflow community for providing excellent documentation and resources.



This project uses TMDB and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.
