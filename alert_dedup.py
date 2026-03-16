from time import time

recent_alerts = {}
DEDUP_WINDOW = 10

def is_duplicate(src, dst, attack_type):
    key = f"{src}-{dst}-{attack_type}"
    now = time()

    if key in recent_alerts:
        if now - recent_alerts[key] < DEDUP_WINDOW:
            return True

    recent_alerts[key] = now
    return False