# Import python packages
import streamlit as st

from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customise Your Smoothie :cup_with_straw:")
st.write(
    """
    Step-1 : Choose the base
    """
)

option = st.selectbox(
    "What type of milk would you like us to add?",
    ("Regular", "Skimmed", "Soy milk","Almond Milk","Oat milk"))

st.write("You selected:", option)


import streamlit as st

name_on_order = st.text_input("Name on Smoothie")
st.write("The name on your smoothie will be ",'"',name_on_order,'"')
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('Step-2 : choose upto five ingredients:',my_dataframe)

if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)
    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ''
    # st.write(ingredients_string) 
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""
    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()

        st.success('Your Smoothie is ordered', icon="✅")

    # st.write(my_insert_stmt)
    st.stop()





st.write(
    """
    Step-3 : Do not shy away for some add-ons\n

""")
option = st.selectbox(
    "Why not some add-ons ?",
    ("Nuts", "Peanut Butter", "Strawberry Squash","Caramel","Orange squash"))

st.write("You selected:", option)

st.write(
    """
    -------Hola ! Enjoy your beverage-------
""")
    

