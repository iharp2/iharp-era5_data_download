import argparse
import cdsapi

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-y", "--year", required=False, help="Year", default="2023")
    ap.add_argument("-v", "--variable", required=False, help="Variable", default="2m_temperature")
    ap.add_argument("-p", "--path", required=False, help="Path", default="download")
    args = ap.parse_args()

    year, variable, path = args.year, args.variable, args.path
    file_path = f"{path}/{variable}-{year}.nc"
    print("Downloading file to", file_path)

    c = cdsapi.Client()

    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "format": "netcdf",
            "variable": variable,
            "year": str(year),
            "month": [str(i).zfill(2) for i in range(1, 13)],
            "day": [str(i).zfill(2) for i in range(1, 32)],
            "time": [f"{str(i).zfill(2)}:00"for i in range(24)],
            'area': [90, -180, -90, 180,],
        },
        file_path,
    )
