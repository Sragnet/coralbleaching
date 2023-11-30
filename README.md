
# Investigating Coral Bleaching Severity

## About the Project

Our project is looking at the severity of coral bleaching over time with respect to distance from the equator. 
This is important as it investiagtes a critical environmental issue and explores some potential influencing factors.

## Data Sourcing

The data used is from 'dataverse.harvard.edu/' and can be found by searching "Coral Bleaching". It is by WorldFish Dataverse from Jan 8, 2016.
The data was last pulled for analysis 03/15/2022.

## Reproducing Results

To reproduce the results discussed in our analysis, 
1. Download `CoralBleaching.xlsx` from [Harvard's website](https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/KUVQKY/PAMLRZ&version=1.3)
2. Verify that this data matches that which can be found in our project directory (SHA256 `b244b954acced13f0b9cc2c7af1d3067856ea3fd391014fad16c4004bcc09a3c`)
3. Run the 'analysis.ipynb'

## Directory Structure

`.`: In the root we have the main analysis notebook, the Dockerfile used to define the Deepnote environment, the README and requirements

`./animation`: The code used to produce the animated version of the first geopandas plot and the resulting mp4

`./datasets`: This includes `CoralBleaching.xlsx`

`./exported_notebook`: The exported notebook as PDF/HTML as produced by our script

`./images`: Images embedded in our analysis

`./old files - ignore`: Old, irrelevant files kept for posterity and future reference

`./scripts`: Small, helpful scripts used in project management

`./styles`: Exploring custom matplotlib colour schemes

## Notes

_Sliders in the notebook_  
Deepnote does not currently support sliders, and geopandas is temperamental in its installation process ergo inadvisable to run on a local machine. 
To use the sliders, we recommend changing the variable value to the year you want to view.  
Alternatively, we have created a [notebook](animation/animation_coding.ipynb) to produce an [animation](animation/animation.mp4) 
of the first geopandas plot showing severity codes over time. 

_Time to run notebook_  
'analysis.ipynb' takes approximately 12 minutes to run. This can be reduced to 5 minutes by changing line 1 in the penultimate code block (above the conclusion) to 1,000.

_Exporting to PDF_  
In order to use the exporting function, you must have pandoc and xelatex installed. The use of our Dockerfile ensures this.  
Exporting to PDF is an optional function that you can opt to enable at the end of the notebook.  
(Note; the notebook may contain content unsuitable for a PDF at which point the script defaults to HTML) 

