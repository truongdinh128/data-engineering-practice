import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

BASE_URL = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
TARGET_TIMESTAMP = "2024-01-19 10:27"  # Thời gian để khớp (mô phỏng yêu cầu bài)

def get_target_file_url():
    # Step 1: Pull page
    response = requests.get(BASE_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 2: Tìm file có timestamp phù hợp
    links = soup.find_all("tr")
    for row in links:
        cols = row.find_all("td")
        if len(cols) >= 2:
            timestamp = cols[1].text.strip()
            if timestamp == TARGET_TIMESTAMP:
                filename = cols[0].find("a").get("href")
                file_url = BASE_URL + filename
                print(f"✅ Found file: {filename}")
                return file_url
    raise ValueError("⚠️ Không tìm thấy file với timestamp yêu cầu.")

def download_file(url, dest_folder="downloads"):
    os.makedirs(dest_folder, exist_ok=True)
    local_filename = os.path.join(dest_folder, url.split("/")[-1])
    response = requests.get(url)
    response.raise_for_status()
    with open(local_filename, "wb") as f:
        f.write(response.content)
    print(f"📥 File downloaded: {local_filename}")
    return local_filename

def find_max_temperature_record(file_path):
    df = pd.read_csv(file_path)
    if 'HourlyDryBulbTemperature' not in df.columns:
        raise ValueError("❌ Column 'HourlyDryBulbTemperature' not found.")
    df_clean = df[pd.to_numeric(df["HourlyDryBulbTemperature"], errors="coerce").notnull()]
    df_clean["HourlyDryBulbTemperature"] = df_clean["HourlyDryBulbTemperature"].astype(float)
    max_temp = df_clean["HourlyDryBulbTemperature"].max()
    hottest = df_clean[df_clean["HourlyDryBulbTemperature"] == max_temp]
    print(f"\n🔥 Hottest record(s):\n{hottest}")

def main():
    try:
        file_url = get_target_file_url()
        file_path = download_file(file_url)
        find_max_temperature_record(file_path)
    except Exception as e:
        print(f"🚨 Error: {e}")

if __name__ == "__main__":
    main()
