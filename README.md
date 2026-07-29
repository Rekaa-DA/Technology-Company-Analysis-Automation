# 🤖 GitHub Repository Data Automation using n8n

## Workflow 

<img width="1652" height="700" alt="Workflow Screenshot" src="https://github.com/user-attachments/assets/997499eb-4a35-47c5-8e76-33a74698c2f3" />

## Dashboard Preview
<img width="974" height="525" alt="image" src="https://github.com/user-attachments/assets/2fed3121-8464-421d-a39e-2a316f019b0f" />

# 📌 Project Summary

📊 This project automates GitHub repository data collection from leading technology companies using the GitHub REST API.

🎯 The project combines **Python**, **MySQL**, **n8n**, **Google Sheets**, and **Power BI** to demonstrate a complete data analytics automation pipeline.

The workflow includes:

* GitHub API data collection
* Python data cleaning
* SQL database storage
* Automated workflow using n8n
* Google Sheets integration
* Automatic Power BI dashboard updates

# 🚀 Tech Stack

<p>
<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/n8n-EA4B71?logo=n8n&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub%20API-181717?logo=github&logoColor=white"/>
<img src="https://img.shields.io/badge/Google%20Sheets-34A853?logo=google-sheets&logoColor=white"/>
<img src="https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black"/>
</p>

---

# 🎯 Project Objectives

1. Automate GitHub repository data collection.
2. Clean and standardize repository data.
3. Store structured repository information.
4. Build an automated data pipeline.
5. Automatically update reporting dashboards.
6. Reduce manual data processing.
7. Demonstrate end-to-end analytics automation.

---

# ⚙️ Project Workflow

```
GitHub REST API
        │
        ▼
Python Data Collection
        │
        ▼
Python Data Cleaning
        │
        ▼
MySQL Database Storage
        │
        ▼
n8n Automation Workflow
        │
        ▼
Google Sheets
        │
        ▼
Power BI Dashboard
```

---

# 🐍 Phase 1 – GitHub API Data Collection (Python)

Python was used to connect to the GitHub REST API and collect repository information from multiple technology companies.

### Tasks Performed

- Connected to GitHub REST API using Personal Access Token
- Retrieved repository information
- Collected repository metadata
- Stored raw repository dataset

### Companies Collected

- Microsoft
- Google
- Oracle
- IBM
- SAP
- Salesforce
- Snowflake
- SAS

---

# 🧹 Phase 2 – Data Cleaning (Python)

Python was used to prepare the raw dataset before automation.

### Cleaning Steps

✔ Removed duplicate repositories

✔ Handled missing values

✔ Standardized column names

✔ Converted data types

✔ Formatted date columns

✔ Exported clean CSV

✔ Generated Excel dataset

✔ Created SQL insert script

---

# 🗄️ Phase 3 – SQL Database

MySQL was used as the structured storage layer.

### Database Activities

- Created `github_repositories` table
- Imported cleaned repository data
- Executed SQL validation queries
- Verified row counts
- Used SQL for structured storage

### Example Query

```sql
SELECT COUNT(*) FROM github_repositories;
```

> **Note**
>
> The MySQL server is hosted locally (localhost). Since this automation runs on **n8n Cloud**, a live connection between n8n Cloud and the local MySQL server could not be established. Therefore, Google Sheets is used as the cloud-based storage layer in the automated workflow.

---

# 🔄 Phase 4 – Automation using n8n

The automation workflow was built using n8n.

### Workflow Steps

1. Schedule Trigger
2. Fetch GitHub repositories
3. JavaScript data cleaning
4. Remove duplicate repositories
5. Transform repository fields
6. Append cleaned data to Google Sheets

---

# ☁️ Phase 5 – Google Sheets Storage

Google Sheets acts as the cloud storage layer.

The workflow automatically:

- Stores cleaned repository data
- Appends newly collected repositories
- Serves as the Power BI data source

---

# 📊 Phase 6 – Power BI Dashboard

Power BI is connected to Google Sheets.

Whenever the n8n workflow executes:

✔ New GitHub repositories are collected

✔ Google Sheets is updated automatically

✔ Power BI displays the latest repository information after refresh

---

# 📊 Dashboard Features

- Total Repositories
- Total Stars
- Total Forks
- Total Watchers
- Total Open Issues
- Repository Distribution by Company
- Programming Language Analysis
- Top Repositories by Stars
- Active vs Archived Repositories
- Interactive Filters

---

# ⚡ Key Features

- GitHub API Integration
- Python Data Collection
- Python Data Cleaning
- SQL Database Design
- n8n Workflow Automation
- Google Sheets Integration
- Power BI Dashboard
- Automatic Data Refresh

---

# 📈 Results

- Automated GitHub repository collection
- Cleaned and standardized repository data
- Structured SQL storage
- Cloud-based automated workflow
- Automatic Google Sheets update
- Automatic Power BI dashboard refresh
- Reduced manual effort

---

# 🔮 Future Enhancements

- Cloud MySQL Integration
- Email Notifications
- Telegram Notifications
- Incremental Repository Updates
- Automated Power BI Refresh
- Cloud Database Deployment

---

# 🛠️ Tools Used

- Python
- GitHub REST API
- MySQL
- n8n
- JavaScript
- Google Sheets
- Power BI

---

# 👤 Author

**S. Rekaa**

📊 Aspiring Data Analyst

🚀 Open to Data Analyst Opportunities
