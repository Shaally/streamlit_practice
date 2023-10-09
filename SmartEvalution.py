import streamlit
import pandas as pd
from PIL import Image

# streamlit.set_page_config(layout="wide")

class SmartEvalution():
    def __init__(self):
        if 'submit' not in streamlit.session_state:
            streamlit.session_state.submit = False  # initial session state for submit button
        if 'inspect' not in streamlit.session_state:
            streamlit.session_state.inspect = False
        if 'complete' not in streamlit.session_state:
            streamlit.session_state.complete = False

    ## session for button
    def submit_button(self):
        streamlit.session_state.submit = True
        streamlit.session_state.inspect = False
        streamlit.session_state.complete = False

    def inspect_button(self):
        streamlit.session_state.inspect = True
        streamlit.session_state.submit = False
        streamlit.session_state.complete = False

    def complete_button(self):
        streamlit.session_state.complete = True
        streamlit.session_state.submit = False
        streamlit.session_state.inspect = False

    def change_df(self):
        streamlit.session_state.df = True

    def set_style(self):
        # 智能評書 button style
        streamlit.markdown("""<style>
                    div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > button {
                       background-color: #FFFFFF;
                       color:#090814;
                       border-radius: 0.75rem;
                       }
                    div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > button:hover {
                        background-color: #87CEFA;
                        color:#ff0000;
                    }
                   </style>""", unsafe_allow_html=True)

        # 設備驗收平台 button style
        streamlit.markdown("""<style>
                    div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > button {
                       background-color: #FFFFFF;
                       color:#090814;
                       border-radius: 0.75rem;
                       }
                    div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > button:hover {
                        background-color: #87CEFA;
                        color:#ff0000;
                    }
                   </style>""", unsafe_allow_html=True)

        # DCFX標準 button style
        streamlit.markdown("""<style>
                    div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(1) > div > div > div > button {
                        background-color: #FFFFFF;
                        color:#090814;
                        border-radius: 0.75rem;
                        }
                    div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(1) > div > div > div > button:hover {
                        background-color: #87CEFA;
                        color:#ff0000;
                    }
                    </style>""", unsafe_allow_html=True)

        # 提交 button style
        streamlit.markdown("""<style>
                    div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > button {
                       background-color: #c2bfbe;
                       color:#090814;
                       border-radius: 0.75rem;
                       }
                    div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > button:hover {
                        background-color: #EE82EE;
                        color:#ffffff;
                    }
                   </style>""", unsafe_allow_html=True)

        # 審查中 button style
        streamlit.markdown("""<style>
                    div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > button {
                       background-color: #c2bfbe;
                       color:#090814;
                       border-radius: 0.75rem;
                       }
                    div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > button:hover {
                        background-color: #EE82EE;
                        color:#ffffff;
                    }
                   </style>""", unsafe_allow_html=True)

        # 審查完成 button style
        streamlit.markdown("""<style>
                    div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(1) > div > div > div > button {
                       background-color: #c2bfbe;
                       color:#090814;
                       border-radius: 0.75rem;
                       }
                    div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(1) > div > div > div > button:hover {
                        background-color: #EE82EE;
                        color:#ffffff;
                    }
                   </style>""", unsafe_allow_html=True)

    def smart_evalution(self):

        tab_list = ["智能評估書審查", "審查資訊清單", "審查資訊看板", "驗收資訊清單", "驗收資訊看板"]
        tab1, tab2, tab3, tab4, tab5 = streamlit.tabs(tab_list)

        with tab1:
            col1, col2 = streamlit.columns(2)
            with col1:
                col1_1, col1_2, col1_3 = streamlit.columns(3)
                with col1_1:
                    streamlit.button("提交", on_click=self.submit_button, use_container_width=True)
                with col1_2:
                    streamlit.button("審查中", on_click=self.inspect_button, use_container_width=True)
                with col1_3:
                    streamlit.button("審查完成", on_click=self.complete_button, use_container_width=True)

            # print(streamlit.session_state.submit)
            # print(streamlit.session_state.inspect)
            # print(streamlit.session_state.complete)
            if streamlit.session_state.submit:
                col1, col2 = streamlit.columns([1.5, 5])
                with col1:
                    choose = streamlit.selectbox("設備上位系統:", ("PLC", "PC"))
                with col2:
                    df1 = pd.DataFrame(
                        {'需求單位': [""], '設備名稱': [""], '設備型號(台達)': [""], '設備型號(廠商)': [""]},
                        index=['填充位置(mm)'])
                    streamlit.table(df1)
                df2 = pd.DataFrame({'項目': [1.1, 1.2, 1.3, 1.4, 1.5],
                                    '項目說明': ['是否通過', '可配合提供', '', '', ''],
                                    '是否支持': [False, False, False, False, False]})
                df3 = pd.DataFrame({'備註(相關不滿足說明)': ["", "", "", "", ""]})

                ## 確認是否支持的表格
                col1, col2 = streamlit.columns([2, 3])
                with col1:
                    container1 = streamlit.empty()
                    if 'df' not in streamlit.session_state:
                        streamlit.session_state.df = False
                    edited_df = container1.data_editor(df2, on_change=self.change_df, hide_index=True)
                    selection = edited_df[edited_df['是否支持']]
                    # print(selection.index.tolist())
                with col2:
                    container2 = streamlit.empty()
                    container2.dataframe(df3, hide_index=True, use_container_width=True)

                    for i in selection.index.tolist():
                        if edited_df['是否支持'].loc[i]:
                            df3['備註(相關不滿足說明)'].loc[i] = 'OK'
                            container2.dataframe(df3, hide_index=True, use_container_width=True)
            elif streamlit.session_state.inspect:
                streamlit.write("To be design 1")
            elif streamlit.session_state.complete:
                streamlit.write("To be design 2")
        self.set_style()
