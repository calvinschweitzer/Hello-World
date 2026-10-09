# Hello-World
My first practice repository
This repository is a small **professional portfolio** of work from my coursework. It includes a *multiple regression analysis* of Spotify song popularity in Excel, and a set of Python programs that practice core programming logic like conditionals and user input.

## Table of contents

- [Project Title](#project-title)
- [Description](#description)
- [Tools Used](#tools-used)
- [Files Used](#files-used)
- [How to Run Program](#how-to-run-program)
- [Additional Information](#additional-information)

## Project Title

*Hello World: My First Repository and Data Analytics Portfolio*

## Description

The main project in this repository is an **Excel analysis of Spotify song popularity**. Using a sample of roughly 1,100 songs, I cleaned the data, summarized it with descriptive statistics and pivot tables, tested whether high-energy and low-energy songs differ in popularity, and examined correlations between popularity and song features like age, duration, tempo, and danceability.

I then built a **multiple regression model** with genre dummy variables to predict popularity, checked for multicollinearity using VIF, and reviewed residual plots to assess model fit. The model explained only about 12% of the variation in popularity, which suggests that song popularity depends on many factors beyond the audio features in this dataset.

The repository also includes a **Python script** from my first homework, with four small programs that practice user input, calculations, and if/else logic: a sales tax calculator, a weekly pay calculator with overtime, a letter grade calculator, and a bonus eligibility checker.

## Tools Used

- **Excel**: pivot tables, descriptive statistics, t-test, correlation, regression, VIF, residual analysis
- **Python**: input handling, conditionals, and calculations
- **GitHub**: version control and portfolio hosting

## Files Used

| File | Description |
|------|-------------|
| `Spotify_Edited_Excel.xlsx` | Spotify song popularity analysis (data dictionary, raw and edited data, regression, and more) |
| `cjschweitzer_hw1.py` | Four beginner Python programs (tax, pay, grades, bonus) |

Spotify data adapted from [Kaggle](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs/).

## How to Run Program

1. Download both files from this repository.
2. **Excel:** Open `Spotify_Edited_Excel.xlsx` and review the tabs from left to right, starting with the Data Dictionary and ending with Regression and Residuals.
3. **Python:** Run the script in a terminal and answer the prompts:

```bash
python cjschweitzer_hw1.py
```

## Additional Information

> Created by **Calvin Schweitzer** for my BAIS Professional Preparation class.
