import rioxarray
import xarray as xr

# Example of manual CRS assignment for NWM
ds = xr.open_dataset(my_bytes_io_buffer)
# NWM Retrospective 3.0 usually uses this projection:
nwm_crs = "+proj=lcc +lat_1=30 +lat_2=60 +lat_0=40 +lon_0=-97 +x_0=0 +y_0=0 +a=6370000 +b=6370000 +units=m +no_defs"
ds.rio.write_crs(nwm_crs, inplace=True)