import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



st.title("Streamlit 超入門")

st.write("Display Image")

img = Image.open("ocean-g787e36393_1920.jpg")
st.image(img, caption="Ocean", use_column_width=True)


#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=["lat", "lon"]
#)

#st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
#writeでもいいが、高さや幅のような引数を設定できないので、dataframeが理想
#行の場合はaxis=1,列の場合はaxis=0

#st.map(df)
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)