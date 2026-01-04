import os
import time
import pandas as pd
from transformers import pipeline
from datetime import datetime

# Initialize the lightweight sentiment model
print("--- Initializing Sentiment-Guard Engine ---")
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Configuration
INBOX = "./data_inbox"
OUTBOX = "./reports"
ALERT_LOG = "reputation_alerts.txt"
THRESHOLD = 0.6  # Alert if average confidence of positive reviews is low

os.makedirs(INBOX, exist_ok=True)
os.makedirs(OUTBOX, exist_ok=True)

def process_file(file_path):
    filename = os.path.basename(file_path)
    print(f"New Data Detected: {filename}")
    
    try:
        # 1. Ingest
        df = pd.read_csv(file_path)
        if 'text' not in df.columns:
            print(f"Error: {filename} missing 'text' column. Skipping.")
            return

        # 2. Inference
        print(f" Running AI Analysis on {len(df)} reviews...")
        results = analyzer(df['text'].tolist())
        
        df['sentiment'] = [r['label'] for r in results]
        df['confidence'] = [r['score'] for r in results]

        # 3. Analytics
        pos_count = len(df[df['sentiment'] == 'POSITIVE'])
        neg_count = len(df[df['sentiment'] == 'NEGATIVE'])
        avg_pos_conf = df[df['sentiment'] == 'POSITIVE']['confidence'].mean() or 0

        # 4. Reporting
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_name = f"analysis_{timestamp}_{filename}"
        df.to_csv(os.path.join(OUTBOX, report_name), index=False)

        # 5. Alerting Logic
        if avg_pos_conf < THRESHOLD or neg_count > pos_count:
            with open(ALERT_LOG, "a") as log:
                log.write(f"[{datetime.now()}] ALERT in {filename}: High Negative Volume detected.\n")
            print(" ALERT: Sentiment threshold breached. Logged to alerts.")

        print(f" Processing Complete. Report saved to {OUTBOX}")
        os.remove(file_path) # Clean up inbox
        
    except Exception as e:
        print(f" Critical Error processing {filename}: {e}")

if __name__ == "__main__":
    print(f"System Live. Drop CSV files into {INBOX} to begin.")
    try:
        while True:
            files = [f for f in os.listdir(INBOX) if f.endswith('.csv')]
            for f in files:
                process_file(os.path.join(INBOX, f))
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nStopping Sentiment-Guard...")