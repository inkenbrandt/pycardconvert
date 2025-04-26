"""Console script for pycardconvert."""

import typer
import argparse
import os

from pycardconvert import convert_file
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    parser = argparse.ArgumentParser(
        description="Convert Campbell Scientific data files using csidft_convert.exe"
    )
    parser.add_argument("input_file", help="Input file name")
    parser.add_argument("output_file", help="Output file name")
    parser.add_argument(
        "output_format",
        choices=["toaci1", "toa5", "tob1", "csixml", "custom-csv", "no-header"],
        help="Output format",
    )
    parser.add_argument("--fsl", help="FSL file for array-based input files")
    parser.add_argument("--array", help="Array ID for array-based input files")
    parser.add_argument(
        "--format-options", type=int, help="Format options (integer value)"
    )

    args = parser.parse_args()

    # Check if input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        return

    convert_file(
        args.input_file,
        args.output_file,
        args.output_format,
        args.fsl,
        args.array,
        args.format_options,
    )


if __name__ == "__main__":
    app()
