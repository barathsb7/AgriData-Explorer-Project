# 🌾 AgriData Explorer Project

An end-to-end data cleaning, SQL engineering, and Power BI dashboard portfolio project analyzing historical crop production trends across India using the official **ICRISAT District-Level Dataset**.

## 📋 Project Architecture
* **Phase 1: Data Preprocessing (Python)**: Cleansed missing value placeholders (`-1` data encodings) and standardized regional text properties utilizing `pandas` and `numpy`.
* **Phase 2: Database Design (SQL)**: Built a local relational SQLite database schema (`agridata.db`) to extract deep agricultural trends via optimized queries.
* **Phase 3: Interactive Dashboards (Power BI)**: Deployed a 3-page business intelligence solution spanning 10 custom visual analytics elements, interactive treemaps, and live geographic spatial maps.

## 💻 Repository Structure
* `clean_data.py` - Source Python data scrubbing algorithm.
* `build_database.py` - Relational database compiler and schema mapper.
* `run_queries.py` - Production SQL analytics script running 10 distinct analytical extractions.
* `AgriData_Dashboard.pbix` - The complete interactive 3-page Power BI dashboard.
