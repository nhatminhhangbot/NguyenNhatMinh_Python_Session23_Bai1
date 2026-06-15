from datetime import datetime, timedelta


def predict_eta(departure_str, distance_km, speed=60):
    """
    Tính toán thời gian dự kiến đến nơi (ETA)
    """
    time_format = "%Y-%m-%d %H:%M:%S"

    dep_time = datetime.strptime(departure_str, time_format)

    hours_needed = distance_km / speed

    eta = dep_time + timedelta(hours=hours_needed)
    return eta
