import requests
import time

API_URL = "http://127.0.0.1:8000"

LEADS = [
    {
        "email": "ceo@empresa1.com",
        "name": "Empresa 1",
        "company": "Empresa 1 SAC",
        "source": "LinkedIn",
        "industry": "Logística",
    },
    {
        "email": "ventas@empresa2.com",
        "name": "Empresa 2",
        "company": "Empresa 2 SAC",
        "source": "Web",
        "industry": "Finanzas",
    },
]


def ingest_leads():
    for lead in LEADS:
        response = requests.post(f"{API_URL}/leads/", json=lead)
        print("Created:", response.json())
        time.sleep(1)


if __name__ == "__main__":
    ingest_leads()
