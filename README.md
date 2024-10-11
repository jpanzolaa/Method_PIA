# Method_PIA
Method Based on Perceived Information Asymmetry

This section outlines a data mining approach to develop a model for electric vehicle depreciation. By collecting and refining data from resale markets and launch prices, the model addresses information asymmetry between buyers and sellers. It calculates buyer and seller utility to provide an accurate vehicle depreciation estimator.

![Alt text](https://github.com/jpanzolaa/Method_PIA/blob/main/img/Fig01.png)

The script that is responsible for carrying out the scraping process is with the data source: scraping.py

This script generates a collection of data in the file SourceRAW.csv. This file is manually transformed into SourceRAW.xlsx for manual data cleaning.

As a use case, Mercadolibre was used for the webscraping process and to obtain the prices of the vehicles manually, the data obtained from the Motor Magazine was used, all within the Colombian context.

The data path is located at mnt/data/.

