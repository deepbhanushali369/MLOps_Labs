# Lab 03 – Apache Beam Word Count Project

## Overview
This lab demonstrates how to build a data processing pipeline using Apache Beam in Python.  
The goal was to read a dataset of product reviews, process the text, and count the frequency of words for each product category.

## Dataset
A custom CSV file containing 500 product reviews was used.  
The dataset includes reviews for the following products:
- Headphones  
- Charger  
- Laptop  
- Desk  
- Lights  

Each record contains:
- Product name  
- Review text  
- Rating  

The CSV file is stored in the `data` folder.

## Objective
To analyze customer reviews by counting how often each word appears for each product.  
This helps identify common keywords and patterns in customer feedback.

## Steps Performed
1. Created a synthetic dataset of 500 product reviews.  
2. Built an Apache Beam pipeline using the **DirectRunner** for local execution.  
3. Read data from the CSV file using `ReadFromText`.  
4. Parsed each line and extracted the product name and review text.  
5. Tokenized the review text into individual words using regular expressions.  
6. Mapped each word with its respective product.  
7. Counted word occurrences per product using `CombinePerKey(sum)`.  
8. Wrote the output to text files in the `outputs` folder.

## Output
The final output shows how many times each word occurred for each product.  
Example:
Headphones - comfortable: 11
Laptop - works: 19
Lights - comfortable: 10
Desk - decent: 14
Charger - excellent: 13

Lab03_Apache_Beam/
├── data/ # Input dataset (product_reviews.csv)
├── outputs/ # Word count results
├── new_dataset.ipynb # Script to generate the dataset
├── Try_Apache_Beam_Python.ipynb # Apache Beam pipeline
└── README.md
