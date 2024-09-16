# North Korea provocations database
Fetching and analyzing hundreds of ballistic missile launches, nuclear tests and other provocative actions by North Korea since 1958.

## Overview

This repository contains a regularly updated database of North Korean provocations sourced from the [Center for International and Strategic Studies' (CSIS) Beyond Parallel project](https://beyondparallel.csis.org/database-north-korean-provocations/). The database includes events such as missile launches, military exercises and other activities perceived as provocations by North Korea. 

The data is collected using a simple Python script that scrapes the CSIS website daily using a GitHub Actions workflow. The collected data is then processed and saved in multiple formats for ease of access and analysis.

## Data collection

### Source

The data is sourced from the "[Database of North Korean Provocations](https://beyondparallel.csis.org/database-north-korean-provocations/)" by CSIS's Beyond Parallel project. The table on the CSIS website contains detailed records of North Korean provocations dating back to 1958. Each record includes information such as the date of the provocation, the type of event, a description and external resources for further reading.

### Collection method

The collection process is automated using a Python script (`fetch_database.py`). The script uses the `requests` library to fetch the HTML content of the source webpage and `BeautifulSoup` to parse the table data into a structured format. This data is then saved in both raw and processed forms in JSON and CSV formats.

A GitHub Actions workflow runs the script daily to keep the dataset current. The raw and processed data files are stored in the `data` directory, organized into `raw` and `processed` subdirectories.

## Data structure

### Raw data

The raw data extracted from the CSIS website is stored in JSON and CSV formats in the `data/raw` directory. Each entry in the dataset contains the following fields:

- `date`: The date of the provocation (e.g., "2024-09-06").
- `type`: The type of provocation (e.g., "Missile Provocation", "Other Provocation").
- `event`: A brief description of the event (e.g., "Short-range Missile Launch").
- `description`: A detailed description of the provocation.
- `resources`: Links to external resources for further information.

### Processed data

The processed data adds additional fields for analysis purposes. The processed dataset is saved in the `data/processed` directory and includes the following fields:

- `date`: The date of the provocation.
- `type`: The type of provocation.
- `event`: A brief description of the event.
- `description`: A detailed description of the provocation.
- `resources`: Links to external resources for further information.
- `year`: The year of the event (extracted from `date`).
- `week_number`: The week number of the event (extracted from `date`).
- `month_year`: The month and year of the event (formatted as MM-YYYY).
- `weekday`: The day of the week on which the event occurred.
- `mentions_kim`: A boolean field indicating if "Kim Jong Un" or "Kim Jong-un" is mentioned in the description.

### Example JSON structure

An example of a single entry in the JSON file looks like this:

```json
{
    "date": "2024-09-06",
    "type": "Other Provocation",
    "event": "Balloon-floating Trash",
    "description": "North Korea has resumed their trash balloon campaign Friday evening, marking the latest in the North's back-to-back balloon launches in the past three days. JCS notified reporters at 6:39 pm Friday that it detected the launch of suspected trash balloons and warned they may move toward northern Gyeonggi Province depending on wind direction. This batch is the North's fourth launch since Wednesday. Earlier in the day, the JCS said it detected the launch of some 260 trash balloons from Thursday night to early Friday, including around 140 trash bundles which were found in Seoul and parts of Gyeonggi Province around the capital. The bundles held paper and plastic bottles, without any hazardous substances.",
    "resources": "https://en.yna.co.kr/view/AEN20240906003551315?section=search",
    "year": "2024",
    "week_number": "35",
    "month_year": "09-2024",
    "weekday": "Friday",
    "mentions_kim": false
}
```

### Repository structure

```csharp
.
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── data
│   ├── processed
│   │   ├── north_korea_provocations_1958_present.csv
│   │   └── north_korea_provocations_1958_present.json
│   └── raw
│       ├── north_korea_provocations_1958_present.csv
│       └── north_korea_provocations_1958_present.json
├── fetch_database.py
└── visuals
```

- `fetch_database.py`: The main script used to collect and process the data.
- `data/raw`: Directory containing the raw data files in CSV and JSON formats.
- `data/processed`: Directory containing the processed data files in CSV and JSON formats.
- `visuals`: Placeholder directory for any visualizations or analysis outputs.

## Usage

1. **Data collection:** Run the `fetch_database.py` script to collect the latest data from the CSIS website. The data will be saved in both raw and processed formats in the data directory.

2. **Automation:** The GitHub Actions workflow automatically runs the data collection script daily, ensuring that the database is up-to-date.

3. **Data access:** Access the raw and processed data files in the data directory for analysis, visualization, or reporting purposes.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.