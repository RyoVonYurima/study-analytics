from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

LOG_FILE = Path(r"C:\Users\ryovo\Documents\Obsidian\study-log.md")
OUTPUT_FILE = Path("study_weekday_time_heatmap.png")

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def parse_log():
    # 7 days × 24 hours
    matrix = np.zeros((7, 24), dtype=int)
    current_date = None

    for line in LOG_FILE.read_text().splitlines():
        if line.startswith("##"):
            current_date = datetime.strptime(line[3:], "%Y-%m-%d").date()
            continue

        if line.startswith("-") and current_date:
            try:
                time_part = line.split("|")[0].strip("- ").strip()

                if "→" in time_part:
                    start_str, end_str = time_part.split("→")
                else:
                    start_str, end_str = time_part.split("-")

                start = datetime.strptime(start_str, "%H:%M")
                end = datetime.strptime(end_str, "%H:%M")

                minutes = int((end - start).seconds // 60)

                weekday = current_date.weekday()  # 0 = Mon
                hour = start.hour

                matrix[weekday, hour] += minutes

            except Exception:
                continue

    return matrix


def generate_heatmap(matrix):
    if matrix.max() == 0:
        print("No data to plot.")
        return

    plt.figure(figsize=(14, 4))

    im = plt.imshow(
        matrix,
        aspect="auto",
        cmap="YlGn"
    )

    plt.colorbar(im, label="Minutes studied")

    plt.yticks(range(7), WEEKDAYS)
    plt.xticks(range(24), range(24))

    plt.xlabel("Hour of day")
    plt.ylabel("Weekday")
    plt.title("Study Rhythm by Weekday & Time")

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    plt.close()

    print(f"Heatmap saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    matrix = parse_log()
    generate_heatmap(matrix)
