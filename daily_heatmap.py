from datetime import datetime, date, timedelta
from pathlib import Path
import matplotlib.pyplot as plt

LOG_FILE = Path(r"C:\Users\ryovo\Documents\Obsidian\study-log.md")
OUTPUT_FILE = Path("study_heatmap.png")

def parse_log():
    data = {}
    current_date = None

    for line in LOG_FILE.read_text().splitlines():
        if line.startswith("##"):
            current_date = datetime.strptime(line[3:], "%Y-%m-%d").date()
            data.setdefault(current_date, 0)
            continue

        if line.startswith("-") and current_date:
            try:
                time_part = line.split("|")[0].strip("- ").strip()
                start_str, end_str = time_part.split("-")

                start = datetime.strptime(start_str, "%H:%M")
                end = datetime.strptime(end_str, "%H:%M")

                minutes = (end - start).seconds // 60
                data[current_date] += minutes
            except Exception:
                continue

    return data

def generate_heatmap(data):
    if not data:
        print("No data to plot.")
        return

    start_date = min(data.keys())
    end_date = max(data.keys())

    # Align to Monday
    start_date -= timedelta(days=start_date.weekday())
    end_date += timedelta(days=(6 - end_date.weekday()))

    num_weeks = ((end_date - start_date).days + 1) // 7

    grid = [[0] * num_weeks for _ in range(7)]

    for d, minutes in data.items():
        week = (d - start_date).days // 7
        weekday = d.weekday()
        grid[weekday][week] = minutes

    plt.figure(figsize=(num_weeks * 0.3 + 2, 4))
    plt.imshow(grid, aspect="auto", cmap="Greens")
    plt.colorbar(label="Minutes studied")

    plt.yticks(range(7), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    plt.xticks([])

    plt.title("Study Heatmap")
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE)
    plt.close()

    print(f"Heatmap saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    data = parse_log()
    generate_heatmap(data)
