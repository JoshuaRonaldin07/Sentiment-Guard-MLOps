# Sentiment-Guard-MLOps
# Sentiment-Guard: Automated MLOps Monitoring Pipeline

A production-ready monitoring system designed to automate the lifecycle of sentiment analysis. This project demonstrates **MLOps principles** by transforming a static Transformer model into a dynamic, event-driven automation engine.



##  Business Case
Companies receive thousands of feedback entries daily. Manual review is impossible. **Sentiment-Guard** acts as a "digital watchtower," automatically flagging negative sentiment spikes and generating brand health reports without human intervention.

##  Key Features
- **Event-Driven Ingestion:** Uses a custom polling engine to monitor a `data_inbox` for new batch files (.csv).
- **Local Transformer Inference:** Powered by **DistilBERT** for high-accuracy sentiment scoring on local CPU.
- **Brand Health Indexing (BHI):** Aggregates sentiment scores to calculate a real-time health metric for every batch.
- **Threshold Alerting:** Automatically triggers an audit trail entry in `reputation_alerts.txt` if the sentiment drops below a safety threshold (0.6).
- **Audit-Ready Reporting:** Generates timestamped CSV reports for stakeholders in the `reports/` directory.

##  Technical Stack
- **AI Engine:** Hugging Face `transformers` (DistilBERT-SST2)
- **Data Engineering:** `pandas`
- **Orchestration:** Python Polling Loop (Watchdog simulation)
- **Environment:** Localized MLOps Architecture



##  Project Structure
```text
Project3_MLOps/
├── data_inbox/         # Source: Simulated incoming customer feedback
├── reports/            # Sink: Processed AI reports with sentiment labels
├── monitor.py          # The Core Logic: Ingestion, Inference, & Alerting
├── generate_data.py    # Mock Data: Script to simulate high-volume feedback
└── README.md           # Documentation
