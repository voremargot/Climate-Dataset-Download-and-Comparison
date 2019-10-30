This repository contains predominatly Jupyter notebook files that can be used to download the following gridded meteorological datasets: 
1. ERA5-HRES single level datasets from https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&text=ERA5
2. PCIC- https://data.pacificclimate.org/portal/gridded_observations/map/
3. DayMet- https://daymet.ornl.gov/getdata

## ERA5-HRES
- Extent: Global
- Resolution: 0.25<sup>o</sup> {~28km}
- Variables: over 200 variables (see full list [here](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview))
- Timespan:1979-present
- Note: I have only worked with the Precipitation, temperature and evaporation datasets for this dataset. Tip of how to work specifically with these variables will be given

## PCIC {PNWNAmet}
- Extent: Northwest North America
- Resolution: 1/16<sup>o</sup> {~6km}
- Variables: Minimum Temperature, Maximum Temperature, Precipitation
- Timespan: 1945-2012

## DayMet
- Extent: North America, Hawaii, Puerto Rico
- Resolution: 1km x 1km
- Variables: Day lenght, Precipitation, Shortwave radiation, snow-water equivalent, Max air temperature, Min air temperature, Water Vapor Pressure
- Timespan: 1980-present

To use this repository it is best to work in the following order:
Downloading Data Sets --> Formatting Data into Rasters --> Climate Data Comparisons --> Trend Analysis





