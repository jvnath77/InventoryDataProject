#import necessary packages
import pandas as pd
import streamlit as st
import sqlalchemy
cnt=0

columns = ["item","item_description","item_price","item_count","vendor","vendor_address"]
#Initialize DB connection
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format("root", "admin", 
                                                      "localhost", "mydatabase"))

#User to upload tsv file through web browser
user_file = st.file_uploader("Select tsv file Columns format:Item,Item_description,Item_price,Item_count,Vendor,Vendor_address")

if user_file is not None and str(user_file.name).endswith(".tsv"):

    #read .tsv file using pandas
    tmp_df = pd.read_csv(user_file, sep='\t')
    
    for itn in tmp_df.columns:
        if itn.lower()  in columns:
            cnt+=1
            continue
        else:
            cnt=0
            break
    #calculate total revenue from the uploaded .tsv file and error handling
    if cnt==6:
        if "object" in str(tmp_df["Item_price"].dtype) or "object" in str(tmp_df["Item_count"].dtype):
            st.write("file doesn't have valid data")
        else:

            #store data to mysql table
            tmp_df.to_sql(con=database_connection, name='products', if_exists='append')
            products_df = pd.read_sql("select Item_price,Item_count from products", con = database_connection)
            st.write(f'The Total Revenue of current file is {round(sum(tmp_df["Item_price"]*tmp_df["Item_count"]), 2)}')
            st.write(f'The Total Revenue is {round(sum(products_df["Item_price"]*products_df["Item_count"]), 2)}')
    else:
        st.write("file doesn't have required columns")

    print('done.!')
elif user_file is not None and not str(user_file.name).endswith(".tsv"):
    st.error('Please select a valid .tsv file')
