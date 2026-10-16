"""Demonstrate detecting and imputing missing port-operation values."""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

REQUIRED_COLUMNS = (
    "Port_Name",
    "Avg_Vessel_Wait_Time_Hours",
    "Labor_Availability_Percent",
)


def demonstrate_missing_value_handling(ports: pd.DataFrame) -> pd.DataFrame:
    """Create missing values in a copy, report them, and fill numeric gaps."""
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in ports]
    if missing_columns:
        raise ValueError(f"Input is missing required columns: {', '.join(missing_columns)}")
    if ports.empty:
        raise ValueError("Input data must contain at least one port.")

    demo_missing = ports.loc[:, REQUIRED_COLUMNS].copy()
    demo_missing.loc[demo_missing.index[:3], "Avg_Vessel_Wait_Time_Hours"] = np.nan
    demo_missing.loc[demo_missing.index[3:5], "Labor_Availability_Percent"] = np.nan

    print("Before handling:")
    print(demo_missing.head(7).to_string(index=False))
    print("\nMissing values before imputation:")
    print(demo_missing.isna().sum().to_string())

    for column in REQUIRED_COLUMNS[1:]:
        demo_missing[column] = demo_missing[column].fillna(demo_missing[column].median())

    print("\nAfter median imputation:")
    print(demo_missing.head(7).to_string(index=False))
    print("\nMissing values after imputation:")
    print(demo_missing.isna().sum().to_string())
    return demo_missing


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Demonstrate missing-value handling on a port CSV file."
    )
    parser.add_argument(
        "csv_path",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("sample_ports.csv"),
        help="path to a CSV containing the required port columns (default: sample_ports.csv)",
    )
    args = parser.parse_args()

    ports = pd.read_csv(args.csv_path)
    demonstrate_missing_value_handling(ports)


if __name__ == "__main__":
    main()
