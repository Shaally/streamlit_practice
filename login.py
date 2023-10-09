import streamlit
import streamlit_authenticator as stauth
from PIL import Image
from SmartEvalution import SmartEvalution
from EquipmentEvalution import EquipmentEvalution
from DcfxStandard import DcfxStandard
import pickle


class Login:
    def __init__(self):
        # info.pkl 用來儲存帳號密碼資訊
        self.information_path = './info.pkl'
        with open(self.information_path, 'rb') as f:
            self.credentials = pickle.load(f)
        # 建立申請帳號按鈕session
        if 'account' not in streamlit.session_state:
            streamlit.session_state.account = False
        # 建立 "智能評估書" 按鈕session
        if 'smart_evalution' not in streamlit.session_state:
            streamlit.session_state.smart_evalution = False
        # 建立 "設備驗收平台" 按鈕session
        if 'equipment_evalution' not in streamlit.session_state:
            streamlit.session_state.equipment_evalution = False
        # 建立 "DCFX標準" 按鈕session
        if 'dcfx_standard' not in streamlit.session_state:
            streamlit.session_state.dcfx_standard = False

    def get_credentials(self):
        return self.credentials

    def account_button(self):
        streamlit.session_state.account = True

    def smart_evalution_button(self):
        streamlit.session_state.smart_evalution = True
        streamlit.session_state.equipment_evalution = False
        streamlit.session_state.dcfx_standard = False

    def equipment_evalution_button(self):
        streamlit.session_state.equipment_evalution = True
        streamlit.session_state.smart_evalution = False
        streamlit.session_state.dcfx_standard = False


    def dcfx_standard_button(self):
        streamlit.session_state.dcfx_standard = True
        streamlit.session_state.smart_evalution = False
        streamlit.session_state.equipment_evalution = False

    def set_style(self):
        streamlit.markdown("""<style>
                            div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > button {
                               background-color: #d1e2ed;
                               color:#090814;
                               border-radius: 0.75rem;
                               }
                            div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > button:hover {
                                background-color: #487ad9;
                                color:#ff0000;
                            }
                           </style>""", unsafe_allow_html=True)
        streamlit.markdown("""<style>
                            div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > button {
                                background-color: #d1e2ed;
                                color:#090814;
                                border-radius: 0.75rem;
                                }
                            div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(4) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > button:hover {
                                background-color: #487ad9;
                                color:#ff0000;
                            }
                            </style>""", unsafe_allow_html=True)
        streamlit.markdown("""<style>
                            div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(1) > div > div > div > button {
                                background-color: #d1e2ed;
                                color:#090814;
                                border-radius: 0.75rem;
                                }
                            div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div:nth-child(1) > div > div:nth-child(1) > div.st-emotion-cache-14qiv68.e1f1d6gn1 > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(1) > div > div > div > button:hover {
                                background-color: #487ad9;
                                color:#ff0000;
                            }
                            </style>""", unsafe_allow_html=True)

    # 忘記密碼
    def forget_password(self):
        username_of_forgotten_password, email_of_forgotten_password, new_random_password = (
            authenticator.forgot_password('Forgot password'))
        if username_of_forgotten_password:
            streamlit.success('New password to be sent securely')
            # Random password should be transferred to user securely

        elif username_of_forgotten_password is None:
            pass
        else:
            streamlit.error('Username not found')

    # 申請帳號
    def register_user(self): # 回傳申請狀態
        try:
            new_email, new_username, new_name, new_password = authenticator.register_user()
            #########################
            ### 要不要加一些審核機制 ###
            ### (原本的有權限控制)  ###
            ########################
            if new_name != '':
                self.credentials[new_name] = {'username':new_username, 'password':new_password, 'email':new_email}
                print(self.credentials)
                # save new password
                # with open(information_path, 'wb') as f:
                #     pickle.dump(credentials, f)
                return True
            else:
                return None
        except Exception:
            return False

    def user_login(self, authentication_status):
        if streamlit.session_state.account:
            register_user_state = self.register_user()
            print("register_user_state", register_user_state)
            if register_user_state:
                streamlit.success("registe successful")

        if username is None or username == "":
            streamlit.warning('Please enter username')
        elif authentication_status is False:  # 密碼錯誤
            streamlit.error('Password incorrect')
            self.forget_password()  # 忘記密碼表單
        elif authentication_status:  # 順利登入

            # 設定title
            col1, col2, col3, col4 = title_container.columns([3, 3, 1, 1])
            with col2:
                streamlit.empty()  # 先藏原本的title圖片
            # with col1:
            #     img = Image.open('D:/project/SmartEvaluation/title.png')
            #     streamlit.image(img, use_column_width=True)
            with col3:
                streamlit.button(username, use_container_width=True)
            with col4:
                authenticator.logout("登出", "main")

            # 如果按下"智能評估書"按鈕
            if streamlit.session_state.smart_evalution:
                obj = SmartEvalution()
                obj.smart_evalution()
            # 如果按下"設備驗收平台"按鈕
            elif streamlit.session_state.equipment_evalution:
                obj = EquipmentEvalution()
            # 如果按下"DCFX標準"按鈕
            elif streamlit.session_state.dcfx_standard:
                obj = DcfxStandard()


if __name__ == "__main__":
    login_obj = Login()

    # header
    col1, col2, col3 = streamlit.columns([3, 0.5, 5])
    with col1:
        image = Image.open('D:/project/SmartEvaluation/core3_logo.png')
        streamlit.image(image, use_column_width=True)
    with col3:
        col3_1, col3_2, col3_3 = streamlit.columns(3)
        with col3_1:
            streamlit.button(" 智能評估書 ", use_container_width=True, on_click=login_obj.smart_evalution_button)
        with col3_2:
            streamlit.button("設備驗收平台", use_container_width=True, on_click=login_obj.equipment_evalution_button)
        with col3_3:
            streamlit.button("  DCFX標準 ", use_container_width=True, on_click=login_obj.dcfx_standard_button)

    title_container = streamlit.empty()
    credentials = login_obj.get_credentials()
    hashed_passwords = stauth.Hasher(credentials).generate()

    # 建立 authenticator
    authenticator = stauth.Authenticate(credentials, hashed_passwords,
        'some_cookie_name', 'some_signature_key', cookie_expiry_days=0)

    name, authentication_status, username = authenticator.login('Login', 'main')

    # use container to show title
    col1, col2, col3 = title_container.columns([1, 3, 1])
    if not authentication_status:  # 還沒成功登入才要顯示 title 圖片
        with col2:
            img = Image.open('D:/project/SmartEvaluation/title_login.png')
            streamlit.image(img, use_column_width=True)

    # 申請帳號
    col1, col2 = streamlit.columns(2)
    if not authentication_status:  # 還沒成功登入才要顯示"申請帳號"按鈕
        with col1:
            streamlit.button("申請帳號", on_click=login_obj.account_button)


    login_obj.user_login(authentication_status)

    login_obj.set_style()
