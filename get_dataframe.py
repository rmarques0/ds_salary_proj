#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:29:15 2020

@author: rodrigomarques
"""


import glassdoor_scraper as gs
import pandas as pd

path = "/Users/rodrigomarques/Downloads/ds_salary_proj/webscraper"

df = gs.get_jobs('data scientist', 15, False, path,15)