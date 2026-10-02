# https://s3.amazonaws.com/tripdata/JC-202608-citibike-tripdata.csv.zip
import requests
from pathlib import Path

### Set path to download data
raw_data_dir = Path("./data/raw")
raw_data_dir.mkdir(parents=True, exist_ok=True)
tripdata_JC_202608_path = Path(raw_data_dir / "JC-202608-citibike-tripdata.csv.zip")

### Check if data exist if not download new data


if not tripdata_JC_202608_path.exists():
    response = requests.get("https://s3.amazonaws.com/tripdata/JC-202608-citibike-tripdata.csv.zip")
    response.raise_for_status()
    print(response.status_code)
    chunk_size = 1024 * 1024
    
    with tripdata_JC_202608_path.open("wb") as file:
        for chunk in response.iter_content(chunk_size):
            file.write(chunk)
            print("Chunk saved")
    

    # bytes_written = tripdata_JC_202608_path.write_bytes(response.content)
    # print(f"Saved {bytes_written:,} bytes to {tripdata_JC_202608_path}")
else:
    print(f"File already exists: {tripdata_JC_202608_path}")
