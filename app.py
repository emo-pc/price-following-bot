import streamlit as st
import database as db
from scraper import get_data
st.set_page_config(page_title="Amazon Price Tracker",page_icon="🛒",layout="wide")
db.create_table()
st.title("🛒 Amazon Price Tracker Dashboard")
st.markdown("Enter the url and target price of the products that you wanna track")
st.divider()

st.subheader("Add new product")
with st.form("add_product_form"):
    col1,col2=st.columns([3,1])
    with col1:
        url_input=st.text_input("Amazon url")
    with col2:
        target_price_input=st.number_input("Target Price",min_value=1.0,step=10.0)

    submit_button=st.form_submit_button("Track the product")

if submit_button:
    if url_input:
        with st.spinner("processing"):
            result=get_data(url_input)
            if "error" not in result:
                product_name=result["title"]
                current_price=result["price"]

                add=db.add_product(product_name,url_input,target_price_input,current_price)

                if add:
                    st.success(f"Completed you are tracking the {product_name[:40]} . Current Price: {current_price}")
                else:
                    st.warning("You are already tracking this product")
            else:
                st.error(f"ERROR")
    else:
        st.error("please enter a valid url")

st.divider()

st.subheader("Products that are in track")
df=db.get_all_products()

if not df.empty:
    df_show=df.drop(columns=["id"])

    df_show.columns=["product_name","url","target_price","current_price"]
    st.dataframe(df_show,use_container_width=True,hide_index=True)
else:
    st.info("No product in track")