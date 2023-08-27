import streamlit as st
import time
from PIL import Image

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!'

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

if expander.checkbox('show Image'):
    img = Image.open('.\ポッキー_アンパンマン.png')
    expander.image(img, caption = 'Pockey Anpanman', use_column_width=True)


# text =st.text_input('あなたの趣味を教えてください。')

# 'あなたの趣味は、', text, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

# 'a' , 'b'

# if st.checkbox('show Image'):
#     img = Image.open('.\ポッキー_アンパンマン.png')
#     st.image(img, caption = 'Pockey Anpanman', use_column_width=True)


