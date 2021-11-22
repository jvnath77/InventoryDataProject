# InventoryDataProject

**Overview**

------------
This application is designed to ingest inventory data using web interface, the application validates data before persisting and display the total revenue of all the products in the inventory.
The application has three tiers, streamlit is used for frontend tier, python for application logic and mysql for persisting data.

------------



**Pre Requisites:**
- Python 3.0 or later
- Anaconda 3 or later
- Mysql 8.0 or later

**Deployment:**
- Install anaconda for package manager


**Anaconda:**

Anaconda is a Python library for scientific computing, that aims to simplify package management and deployment.Use the link https://www.anaconda.com/products/individual to install Anaconda.

**Streamlit:**

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

- Go to anaconda prompt and install the packages that are needed
            pip install mysql-connector-python
            pip install streamlit
			
**Setup MySql :**

MySQL is an open-source relational database management system and MySQL is the de-facto standard database system for web sites with HUGE volumes of both data and end-users (like Facebook, Twitter, and Wikipedia).Use the link to download and install mysql https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/.

- Create database using python
           python <location of db python app>

- Run your application using anaconda prompt
          streamlit run <location of main python app>

**Test Cases:**

------------

**Success Test Suite:**

1.Click on browsefile and upload the given data.tsv to start a run. 

2.Verify the total be $114802.93.

3.Repeat step 1 to verify persistent system to hold the data.

4.Now the Total Revenue is 229605.86. 

**Error Handling Test Suite:**

1.Click on browsefile and upload bad data file i.e. data1.tsv to start a run.

2.Verify the error handled gracefully with a message "file doesn't have required columns".

3.Click on browsefile and upload a non .tsv file.

4.Verify the error handled gracefully with a message "Please select a valid .tsv file".

5.Click on browsefile and upload bad data file i.e. data3.tsv to start a run "file contains bad data".

