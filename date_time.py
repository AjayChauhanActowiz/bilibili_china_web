from datetime import datetime, timezone, timedelta

def timestamp_to_china_india(ts: int):
    # Step 1: Interpret ts as UTC (correct)
    utc_time = datetime.fromtimestamp(ts, tz=timezone.utc)

    # Step 2: Convert to China (UTC+8) and India (UTC+5:30)
    china_time = utc_time + timedelta(hours=8)
    india_time = utc_time + timedelta(hours=5, minutes=30)

    # Format without timezone info (as per your example)
    return {
        "china_time": china_time.strftime("%Y-%m-%d %H:%M:%S"),
        "india_time": india_time.strftime("%Y-%m-%d %H:%M:%S")
    }


if __name__ == "__main__":
    # ts = 1762599318
    ts = 1751888641
    res = timestamp_to_china_india(ts)
    print("China Time (CTC):", res["china_time"])  # → 2025-11-08 18:55:18
    print("India Time (IST):", res["india_time"])  # → 2025-11-08 16:25:18