# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
new_customers = dataiku.Dataset("new_customers")
new_customers_df = new_customers.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

out1_df = new_customers_df # For this sample code, simply copy input to output


# Write recipe outputs
out1 = dataiku.Dataset("out1")
out1.write_with_schema(out1_df)
