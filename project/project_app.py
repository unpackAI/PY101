import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


from project_process_data import get_exchange_rates, get_lego_df, get_lego_image_url

st.set_page_config(page_title="WebScrapping - PY101", page_icon="🛒", layout="wide")
st.image("https://unpackai.github.io/unpackai_logo.svg")
st.title("WebScrapping of Lego Prices around the world 🌏")
st.write("*by <name>*")
# st.write("---")

st.sidebar.button("Refresh Data", on_click=st.legacy_caching.clear_cache)

EXCHANGE_RATES = get_exchange_rates(["USD", "EUR", "GBP"])
st.sidebar.header("Exchange Rates:")
st.sidebar.table(
    pd.DataFrame(EXCHANGE_RATES.items(), columns=["currency", "rate (in CNY)"])
)

LIST_LEGOS = {
    "Apollo Saturn V": 21309,
    "Safari Tree House": 31116,
    "NASA Women": 21312,
    "Jeep Wrangler": 42122,
    "HP Hogwarts": 71043,
    "City Town": 60097,
    "Millennium Falcon": 75257,
    "Frozen Ice Palace": 43172,
    "Classic Box": 10698,
    "Infinity Gauntlet": 76191,
}


def get_df():
    """Get the DataFrame with all the selected legos"""
    dfs = [
        get_lego_df(lego_name, lego_id, EXCHANGE_RATES)
        for lego_name, lego_id in LIST_LEGOS.items()
    ]
    return pd.concat(dfs, ignore_index=True)


# We will get the DataFrame with all the date
# We can then filter the Lego sets and the websites
df_all = get_df()
df = df_all.copy()

st.sidebar.header("Selected Legos:")
SELECTED_LEGOS = [
    n for n, i in LIST_LEGOS.items() if st.sidebar.checkbox(f"{n} ({i})", value=True)
]
df = df[df.legoName.isin(SELECTED_LEGOS)]

st.sidebar.header("Selected Websites:")
list_websites = df.source.unique()
# TODO: Add filtering on list of Websites
# SELECTED_WEBSITES = [
#     website for website in list_websites if st.sidebar.checkbox(website, value=True)
# ]
# df = df[df.source.isin(SELECTED_WEBSITES)]

st.sidebar.header("Filtering by price:")
current_max_price = float(df.price.max())
max_price = st.sidebar.slider(
    "Maximum Price", min_value=0.0, max_value=current_max_price, value=current_max_price
)
df = df[df.price <= max_price]

# TODO: Add filtering on minimum price


# We get a DataFrame with all the Lego
# and another one with the average per Website and Lego Set
df_average = df.groupby(["source", "legoName"]).mean().reset_index()


sns.set_theme(style="darkgrid", rc={"figure.figsize": (16, 8)})

st.header("Average Prices:")
fig_avg, ax_avg = plt.subplots()
sns.stripplot(
    x="legoName",
    y="price",
    hue="source",
    data=df_average,
    size=16,
    marker="D",
    alpha=0.75,
    ax=ax_avg,
)
st.pyplot(fig_avg)


st.header("Details:")
with st.expander("Distribution of prices:"):
    fig_all, ax_all = plt.subplots()
    sns.stripplot(
        x="legoName", y="price", hue="source", data=df, alpha=0.50, size=10, ax=ax_all
    )
    st.pyplot(fig_all)

with st.expander("All prices:", expanded=True):
    st.table(df.drop(["image"], axis=1))


st.header("Pictures of Lego:")
for lego_name, lego_id in LIST_LEGOS.items():
    with st.expander(lego_name):
        img_url = get_lego_image_url(lego_id, df_all)
        if img_url and isinstance(img_url, str):
            st.image(img_url)
        else:
            st.write("No image available")
