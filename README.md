# CDR Forensic Analysis Dashboard

## Overview

The CDR Forensic Analysis Dashboard is a Python-based forensic analysis system developed for analyzing Call Detail Records (CDRs) obtained from telecom billing data.

The project processes call and SMS records to identify communication patterns, active hours, frequently contacted numbers, suspicious behavior, and approximate location activity using data visualization and an interactive Flask dashboard.

The system combines forensic data analysis, telecom simulation, visualization, and dashboard integration to simplify communication trend analysis and forensic investigation workflows.

---

## Key Features

### Call Analysis
- Frequently contacted numbers
- Daily call activity trends
- Active communication hours

### SMS Analysis
- SMS activity patterns
- Top SMS contacts

### Suspicious Activity Detection
Detection based on:
- High call frequency
- Long-duration calls
- Late-night communication
- Repeated short-duration calls

### Telecom Data Simulation
- MCC
- MNC
- Operator identification
- Cell ID simulation
- LAC/TAC generation

### Interactive Dashboard
- Flask-based web interface
- Sidebar navigation
- Graph visualization
- Interactive map integration

### Map Visualization
Interactive telecom activity visualization using Folium maps.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend logic and forensic analysis |
| Pandas | Data processing and analysis |
| Matplotlib | Graph generation |
| Flask | Web dashboard integration |
| Folium | Map visualization |
| HTML/CSS | Frontend dashboard interface |

---

## Project Structure

```bash
CDR-Forensic-Analysis/
│
├── cdr_script.py
├── UI_script.py
├── web_page.html
├── map.html
├── requirements.txt
├── CDR_Report.pdf
├── README.md
├── LICENSE
├── .gitignore
│
├── graphs/
│
└── screenshots/
```

---

## Workflow

1. Collect telecom CDR data from billing records
2. Convert extracted records into CSV format
3. Process datasets using Python and Pandas
4. Generate communication analysis graphs
5. Detect suspicious communication behavior
6. Generate telecom simulation details
7. Display results through Flask dashboard and Folium maps

---

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Execution

Run the analysis script:

```bash
python cdr_script.py
```

Run the Flask dashboard:

```bash
python UI_script.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## Output

The system generates:
- Communication trend graphs
- SMS activity analysis
- Suspicious activity reports
- Telecom simulation details
- Interactive location mapping
- Flask-based forensic dashboard

---

## Dashboard Preview

### Main Dashboard

![Web Dashboard](screenshots/webpage.png)

### Map Visualization

![Map UI](screenshots/map_ui.png)

### Map Close-Up

![Map Closeup](screenshots/map_ui_closeup.png)

### Suspicious Activity Analysis

![Suspicious Analysis](screenshots/cmd_suspicious_analysis.png)

---

## Dataset Notice

The original CDR datasets used in this project are not included in the repository due to privacy and sensitive telecom data considerations.

All screenshots, outputs, and reports have been anonymized/masked for demonstration purposes.

---

## Privacy Note

Sensitive telecom data and phone numbers have been anonymized for privacy purposes. Raw datasets are excluded from this repository.

---

## Future Enhancements

- Real telecom API integration
- Automated PDF extraction
- Advanced anomaly detection
- Database integration
- Real-time monitoring dashboard

---

## Academic Purpose

Developed as part of Digital Forensics and Information Security (DFIS) practical forensic analysis and visualization work.
