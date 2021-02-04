# ETL-project

Data Cleaning 
    1. hard to pull all the full titles from the tables, so I just hard coded it (only five items).
        if it was a lot, could have used an if statement with find_next(). if it exists (comes back as true), add the info to the string
    
    2. there were a lot of new line characters in the html. got rid of some of them using the .strip() when pulling the text in BeautifulSoup
        the rest needed replaced with '-' so we looped through the dataframes looking for '\n' and replacing