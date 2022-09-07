import streamlit
streamlit.title('My Parents new Healthy Dinner')
   
    
streamlit.header('BreakFast Menu')
streamlit.text('omega3 & Blueberry oatmeal')
streamlit.text('kale spinach & rocket smootie')
streamlit.text('Hard_boiled  Free_range eggs')




import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
