def CreateRaster(lon,lat,data,resx,resy,save_directory):
    from osgeo import gdal
    from osgeo import gdal_array
    from osgeo import osr,ogr

    xmin,ymin,xmax,ymax = [lon.min(),lat.min(),lon.max(),lat.max()]
    nrows,ncols = np.shape(data)
    geotransform=(xmin-resy,resy,0,ymax+resx,0, -resx)  

    output_raster = gdal.GetDriverByName('GTiff').Create(save_directory,ncols, nrows, 1 ,gdal.GDT_Float32)  # Open the file

    output_raster.SetGeoTransform(geotransform)  # Specify its coordinates
    srs = osr.SpatialReference()                 # Establish its coordinate encoding
    srs.ImportFromEPSG(3005)                     # This one specifies WGS84 lat long.
                                                 # Anyone know how to specify the 
                                                 # IAU2000:49900 Mars encoding?
    output_raster.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system                                         
    output_raster.GetRasterBand(1).WriteArray(data)   # Writes my array to the raster
    output_raster.FlushCache()

    return
