def create_progress_bar(current_day, max_days, bar_length=20):
    if max_days == 0:
        return "[--------------------] 0%"

    percentage = current_day / max_days

    filled_chars = int(percentage * bar_length)

    bar = "█" * filled_chars + "-" * (bar_length - filled_chars)

    percentage_int = int(percentage * 100)

    return f"[{bar}] {percentage_int}%"
