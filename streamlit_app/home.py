import pandas as pd
import streamlit as st

from config import datafields, home_image

#page functioning
def app():

    #heading and text information
    html1 = '''
    <style>
    #pred_image{
      
     }
    #heading{
      color: #E65142;
      text-align:top-left;
      font-size: 45px;
    }
    #sub_heading1{
    color: #E65142;
    text-align: right;
    font-size: 30px;
    }
    #sub_heading2{
    color: #E65142;
    text-align: left;
    font-size: 30px;
      }
    #usage_instruction{
    text-align: right;
    font-size : 15px;
    }
    #data_info{
    text-align : left;
    font-sixe : 15px;
    }
    /* Rounded border */
    hr.rounded {
        border-top: 6px solid #E65142;
        border-radius: 5px;
    }
    </style>
    <h1 id = "heading"> Sales Analysis </h1>
    <h3>The company operates over 1,000 stores in 3 countries.<br>
    </h3>
    '''
    st.markdown(html1, unsafe_allow_html=True)
    st.image(home_image, width=700, output_format="PNG")
    html2 = '''
    <hr class="rounded">
    
    <h3 id ="sub_heading2">Description&emsp;&emsp;&emsp;</h3>
    <b>1. Sales Analyses using <i> Data Visulations</i> based on <i>Seaborn</i><br>
    <b>2. Future Sale Prediction using <i>Decision Tree Algorithm</i>&emsp;&emsp;<br>
    <b>3. The data is the <i>sales data</i> for the <b>financial year 2021</b>. The data is divided and analysed into <b> financial quaters</b>  for&nbsp;&nbsp;&nbsp;<br>  
    better analyses and assesment of the sales.<br>
    '''
    st.markdown(html2, unsafe_allow_html=True)

    df = pd.read_csv(datafields)
    data = [["Quarter1", "Jan, 2021 - Mar, 2021"], ["Quarter2", "Apr, 2021 - Jun, 2021"],["Quarter3", "Jul, 2021 - Sep, 2021"], 
    ["Quarter4", "Oct, 2021 - Dec, 2021"]]
    df2 = pd.DataFrame(data, columns=["Quarters", "Range"])

    #data description
    col1, col2 = st.columns(2)
    
    button1 = col1.button("Data Fields")
    if(button1):
        st.table(df)
    button2 = col2.button("Data Breakup")
    if(button2):
      st.table(df2)

    
