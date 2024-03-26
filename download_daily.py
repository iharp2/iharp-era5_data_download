import argparse
import cdsapi

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-y", "--year", required=False, help="Year", default="2023")
    ap.add_argument("-m", "--month", required=False, help="Month", default="01")
    ap.add_argument("-d", "--day", required=False, help="Day", default="01")
    ap.add_argument(
        "-v", "--variable", required=False, help="Variable", default="2m_temperature"
    )
    ap.add_argument("-p", "--path", required=False, help="Path", default="download")
    args = ap.parse_args()

    year, month, day, variable, path = (
        args.year,
        args.month,
        args.day,
        args.variable,
        args.path,
    )
    month = month.zfill(2)
    day = day.zfill(2)
    file_path = f"{path}/{variable}-{year}-{month}-{day}.nc"
    print("Downloading file to", file_path)

    c = cdsapi.Client()

    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "format": "netcdf",
            "variable": variable,
            "year": str(year),
            "month": [month],
            "day": [day],
            "time": [f"{str(i).zfill(2)}:00" for i in range(24)],
        },
        file_path,
    )
