"""CSV Diff Studio — Compare two CSV files by a primary key, show added, removed, and changed rows, and export a clean report."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='csv_diff_studio',
        description='Compare two CSV files by a primary key, show added, removed, and changed rows, and export a clean report.',
    )
    parser.add_argument('left', nargs='?', help='First CSV')
    parser.add_argument('right', nargs='?', help='Second CSV')
    parser.add_argument('--key', help='Primary key column')
    args = parser.parse_args()
    print('CSV Diff Studio')
    print('Row-level diffs for CSV exports from sheets, CRMs, and databases.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
