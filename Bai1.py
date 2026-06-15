# Việc lạm dụng from math import * được coi là một "Anti-pattern" vì nó gây lỗi namespace pollution và giảm khả năng đọc code
# Cách import an toàn: import math và gọi math.sqrt()
# Ta cần tệp __init__.py với vai trò thông báo cho trình thông dịch của Python biết thư mục chứa nó là package chứa các module

from datetime import datetime
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta
from utils.file_helper import create_log_dir

shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285, "from_lon": 105.8542,
        "to_lat": 10.8231, "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285, "from_lon": 105.8542,
        "to_lat": 16.0544, "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    },
]


def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
    log_dir = "logs"
    if create_log_dir(log_dir):
        print(f"[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    else:
        print(f"[WARN] Hệ thống lưu trữ log gặp sự cố.")

    print("-" * 75)

    time_format = "%Y-%m-%d %H:%M:%S"

    for s in shipments:
        distance = calculate_distance(
            s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])

        eta = predict_eta(s["depart"], distance, speed=60.0)

        deadline_dt = datetime.strptime(s["deadline"], time_format)

        if eta <= deadline_dt:
            status = "AN TOÀN (Kịp tiến độ trước deadline)"
        else:
            deadline_time_str = deadline_dt.strftime("%H:%M:%S")
            status = f"CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline_time_str})"

        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime(time_format)}")
        print(f" + Trạng thái: {status}\n")

    print("=" * 56)


if __name__ == "__main__":
    main()
