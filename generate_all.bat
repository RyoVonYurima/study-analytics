@echo off
cd /d C:\Users\ryovo\Documents\Projects\study-analytics

REM Generate daily heatmap
py heatmap.py

REM Generate weekday/time heatmap
py timeofday_heatmap.py

REM Commit and push
git add *.png
git commit -m "auto: update study heatmaps"
git push
