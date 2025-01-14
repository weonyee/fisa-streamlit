import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 텍스트 입력받기
# inpt = st.text_area("검색할 애니메이션을 입력하세용가리 .^__")

# # ani_list에 있는 글자가 일부라도 들어가면 img_list에 있는 해당 그림이 출력되는 검색창

# dct = {ani_list[0] : img_list[0],
#        ani_list[1] : img_list[1],
#        ani_list[2] : img_list[2]}

# cnt = 0
# for item in ani_list:
#     if inpt in item:
#         cnt += 1
#         st.image(dct[item], width= 400)

# if cnt == 0:
#     st.write('그런 건 없습니다 !! ㅡ..ㅡ')

search = st.text_input('애니메이션 입력')
print(search)
st.write(search)

for ani in ani_list:
    if search in ani:
        print(ani)
        img_idx = ani_list.index(search)

if search != '':
    st.image(img_list[img_idx])