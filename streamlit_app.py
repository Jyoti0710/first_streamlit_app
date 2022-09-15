import streamlit
streamlit.title('My Parents new Healthy Dinner')
   
    
streamlit.header(' BreakFast Menu')
streamlit.text(' 🥣 omega3 & Blueberry oatmeal')
streamlit.text(' 🥗 kale spinach & rocket smootie')
streamlit.text(' 🐔 Hard_boiled  Free_range eggs')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')





import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc['Avocado','Strawberry']


# Display the table on the page.
streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)


