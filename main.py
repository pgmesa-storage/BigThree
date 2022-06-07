
from big_three import get_big_three, today

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title('Big Three')
accum = st.checkbox("Accumulative", value=True)
since_year = st.slider('Since year', value=2000, min_value=2000, max_value=today.year)

rafa, djoko, federer = get_big_three()

years, rafa_arr = rafa.get_slams_per_year(get_years=True, since_year=since_year, accumulative=accum)
djoko_arr = djoko.get_slams_per_year(since_year=since_year, accumulative=accum)
federer_arr = federer.get_slams_per_year(since_year=since_year, accumulative=accum)

if accum:
    figure = plt.figure()
    plt.plot(years, djoko_arr, '-o')
    plt.plot(years, rafa_arr, '-o')
    plt.plot(years, federer_arr, '-o')
    plt.ylabel("Grand Slam Count")
    plt.xlabel("Years")
    plt.legend([
        f"{djoko.name}",
        f"{rafa.nickname}",
        f"{federer.name}"
    ], loc=2)
else:
    x = np.arange(len(years))  # the label locations
    width = 0.7 # the width of the bars
    figure, ax = plt.subplots(figsize=(15,5))
    rects1 = ax.bar(x - width/3, djoko_arr, width/3, label=djoko.name)
    rects2 = ax.bar(x, rafa_arr, width/3, label=rafa.nickname)
    rects3 = ax.bar(x + width/3, federer_arr, width/3, label=federer.name)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    years_str = [str(y)[2:] for y in years]
    ax.set_xticks(x, years_str)
    plt.ylabel("Grand Slam Year Count")
    plt.xlabel("Years")
    ax.legend(loc=2)

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    figure.tight_layout()

st.pyplot(figure)

headers, rafa_sum = rafa.get_summary_as_list(return_headers=True)
djoko_sum = djoko.get_summary_as_list()
federer_sum = federer.get_summary_as_list()
df = pd.DataFrame([rafa_sum, djoko_sum, federer_sum], columns=headers)
st.dataframe(df)
