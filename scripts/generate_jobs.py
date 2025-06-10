import pandas as pd
import random
from datetime import datetime, timedelta

roles = ["Software Engineer", "Data Scientist", "DevOps Engineer", "Frontend Developer", "Backend Developer"]
companies = ["Google", "Amazon", "Microsoft", "TCS", "Infosys", "Wipro", "Capgemini", "Accenture"]
skills = ["Python", "Java", "C++", "AWS", "Docker", "Kubernetes", "SQL", "React", "Node.js"]
locations = ["Remote", "Bangalore", "Hyderabad", "Delhi", "Chennai", "Pune", "Mumbai"]

def generate_fake_jobs(n=300):
    data = []
    for _ in range(n):
        job = {
            "Job Title": random.choice(roles),
            "Company": random.choice(companies),
            "Skills": ", ".join(random.sample(skills, k=random.randint(2, 5))),
            "Posted Date": (datetime.today() - timedelta(days=random.randint(0, 60))).strftime("%Y-%m-%d"),
            "Location": random.choice(locations)
        }
        data.append(job)
    return pd.DataFrame(data)

df = generate_fake_jobs()
df.to_csv("data/job_data.csv", index=False)
print("✅ job_data.csv generated in data/ folder.")
