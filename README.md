# Study Analytics

A lightweight, no-BS study tracking and visualization system.

This project turns raw study logs into **daily consistency** and **weekly time-of-day heatmaps**, so I can see *when* and *how consistently* I actually study — not when I think I do.

No timers running in the background.
No bloated productivity apps.
Just data that reflects reality.

---

## What this does

This repo **does not track study sessions directly**.

Instead, it:
- Reads an existing Markdown study log
- Generates visual analytics
- Auto-updates the results to GitHub

### Currently generated analytics

#### 1. Daily Study Consistency
Shows how close each day was to the daily study target.

- Rows: Weekdays (Mon–Sun)
- Columns: Weeks
- Color scale: Minutes studied (0 → daily target)

File: study_daily_heatmap.png


#### 2. Study Rhythm by Weekday & Time
Shows *when* during the day studying actually happens.

- Rows: Weekdays (Mon–Sun)
- Columns: Hour of day (0–23)
- Color scale: Minutes studied in that hour

File: study_weekday_time_heatmap.png


---

## Data source

This project reads from a Markdown log file with the format:

```markdown
## 2026-02-02
- 11:13-12:20 | Pharmacology | pc


