# FTIR_Mapping
Attempt to automate FT-IR Mapping by combining mainly https://github.com/liljerri/ftir_data_analytics from KBI Pharma and OPUSFC to process FT-IR data arrays collected using
a Bruker Hyperion 2000 microscope, and display results using heatmaps (since spectral FT-IR data is not readily comparible spatially). 

Note: Most datapoints were measured using ATR contact mode, though optical mode should work as well. 

Currently in process of making more user friendly

As of now, workflow involves:
-uploading data exported from OPUS as .csv, .dpt, or .xy (has no filetype in file explorer), and can be multiple files, single data points, or single file with table of datapoints
-specifying if it's a single data point or an array of images
-processing data from raw (not baseline corrected, etc.) to just the Amide I (or Amide I + II regions)
-running peak fitting based on Amide I and fitting parameters (this is the heart of the program); custom peak fitting parameters may be needed, using literature as a reference point
-Using results of peak fitting to produce heatmaps of secondary structure
