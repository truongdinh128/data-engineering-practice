import os
import requests
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  # link có thể sai
]

def main():
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    for url in download_uris:
        filename = os.path.basename(url)
        zip_path = os.path.join(download_dir, filename)

        try:
            print(f"Đang tải {url}...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            with open(zip_path, "wb") as f:
                f.write(response.content)
            print(f"Đã lưu: {zip_path}")

            # Giải nén
            print(f"Đang giải nén {zip_path}...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir)
            print(f"Đã giải nén vào: {download_dir}")

            # Xóa file zip
            os.remove(zip_path)
            print(f"Đã xoá: {zip_path}\n")

        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi tải {url}: {e}")
        except zipfile.BadZipFile:
            print(f"File không hợp lệ hoặc bị lỗi: {zip_path}")
            if os.path.exists(zip_path):
                os.remove(zip_path)

if __name__ == "__main__":
    main()
