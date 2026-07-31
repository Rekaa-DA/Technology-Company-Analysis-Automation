# 🤖 GitHub Repository Automation using n8n

## 📊 Workflow Preview

> *(Add your n8n Workflow Screenshot here)*

<img width="1000" alt="Workflow Screenshot" src="YOUR_WORKFLOW_SCREENSHOT_LINK_HERE"/>

---

# 📌 Project Summary

This phase automates the GitHub repository data collection process using n8n.

The workflow automatically retrieves live repository data from the GitHub REST API, transforms and cleans the data using JavaScript, updates Google Sheets, removes duplicate records, validates the final dataset, and sends an email notification after successful execution.

The updated Google Sheets dataset is then used as the data source for the Power BI dashboard, which is refreshed manually whenever new data is available.

---

# 🚀 Tech Stack

<p>
  <img src="https://img.shields.io/badge/n8n-EA4B71?logo=n8n&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub%20API-181717?logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/Google%20Sheets-34A853?logo=google-sheets&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gmail-EA4335?logo=gmail&logoColor=white"/>
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black"/>
</p>

---

# 🎯 Objectives

1. Automate GitHub repository data collection
2. Retrieve live repository information using GitHub REST API
3. Transform API response using JavaScript
4. Remove duplicate repositories
5. Clean and validate repository data
6. Automatically update Google Sheets
7. Send Gmail notification after successful execution
8. Provide updated data for manual Power BI dashboard refresh

---

# ⚙️ Workflow Steps

- Schedule Trigger starts the automation.
- JavaScript generates the list of GitHub organizations.
- HTTP Request collects repository data from GitHub REST API.
- JavaScript transforms the API response into a structured dataset.
- Google Sheets stores the collected repository data.
- JavaScript removes duplicate repositories.
- Google Sheets updates the cleaned dataset.
- JavaScript validates and formats the final dataset.
- Google Sheets stores the validated repository data.
- Gmail sends a success notification after workflow completion.

---

# 📂 Files Included

- workflow.json
- workflow_screenshot.png
- execution_screenshot.png
- workflow_demo.mp4
- README.md

---

# 📊 Workflow Output

> *(Add your Execution Screenshot here)*

<img width="1000" alt="Execution Screenshot" src="YOUR_EXECUTION_SCREENSHOT_LINK_HERE"/>

### Output

- Repository data collected successfully
- API response transformed using JavaScript
- Duplicate repositories removed
- Dataset cleaned and validated
- Google Sheets updated automatically
- Gmail notification sent successfully
- Updated dataset ready for manual Power BI dashboard refresh

---

# 🚀 Key Features

- Scheduled GitHub data collection
- GitHub REST API integration
- JavaScript-based data transformation
- Duplicate record removal
- Automatic Google Sheets update
- Gmail success notification
- Ready for manual Power BI dashboard refresh

---

# 📌 Conclusion

The n8n automation workflow successfully retrieves live GitHub repository data, processes and validates the dataset, removes duplicate records, updates Google Sheets automatically, and sends a Gmail notification after successful execution.

The updated Google Sheets dataset serves as the source for the Power BI dashboard, which can be manually refreshed to visualize the latest repository analytics.

---

# 👤 Author

**Rekaa**

📊 Aspiring Data Analyst  
🚀 Open to Data Analyst Opportunities
