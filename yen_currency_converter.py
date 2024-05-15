import streamlit as st

st.subheader("Yen to SGD currency converter")

st.session_state.orig_yen = ""
st.session_state.exchange_rate = "0.008634"
st.session_state.sgd_comparison = ""


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def format_number(string, is_yen=False):
    formatted =  "{0:,.2f}".format(string)
    if is_yen:
        return formatted[:-3]
    return formatted


tab1, tab2, tab3 = st.tabs(["  Just Convert  ", "  Include Tax  ", "  Exclude Tax  "])

with tab1:
    st.session_state.orig_yen = st.text_input("Amount (¥)", value=st.session_state.orig_yen, key="tab1_orig_yen")
    st.session_state.exchange_rate = st.text_input("Exchange rate", value=st.session_state.exchange_rate, key="tab1_fx_rate")

    if len(st.session_state.orig_yen) > 0 and len(st.session_state.exchange_rate) > 0:
        if is_float(st.session_state.orig_yen) and is_float(st.session_state.exchange_rate):
            converted_sgd = float(st.session_state.orig_yen) * float(st.session_state.exchange_rate)

            st.write("")
            st.markdown('''
                        **Amount in SGD** : :red[\$ {}]
                        '''.format(
                            format_number(converted_sgd,is_yen=False)
                        )
            )
        else:
            st.error("Input is not a number!")

with tab2:
    st.session_state.orig_yen = st.text_input("Amount (¥)", value=st.session_state.orig_yen, key="tab2_orig_yen")
    st.session_state.exchange_rate = st.text_input("Exchange rate", value=st.session_state.exchange_rate, key="tab2_fx_rate")
    tax_rate = st.radio("Tax rate",["10%", "8%"],horizontal=True, key="tab2_tax_rate")

    if len(st.session_state.orig_yen) > 0 and len(st.session_state.exchange_rate) > 0:
        if is_float(st.session_state.orig_yen) and is_float(st.session_state.exchange_rate):

            orig_yen = float(st.session_state.orig_yen)
            tax_rate = int(tax_rate[:-1])/100

            tax_amount =  orig_yen * tax_rate
            amt_including_tax = orig_yen + tax_amount
            converted_sgd = amt_including_tax * float(st.session_state.exchange_rate)

            st.write("")
            st.markdown('''
                        Tax amount : ¥ {}

                        Amount including tax : ¥ {}
                        
                        **Amount in SGD** : :red[\$ {}]
                        '''.format(
                            format_number(tax_amount, is_yen=True),
                            format_number(amt_including_tax, is_yen=True),
                            format_number(converted_sgd,is_yen=False)
                        )
            )

            st.write("---")
            st.session_state.sgd_comparison = st.text_input("SGD comparison (SGD)", value=st.session_state.sgd_comparison, key="tab2_sgd_comparison")

            if len(st.session_state.sgd_comparison) > 0 and is_float(st.session_state.sgd_comparison):
                sgd_comparison = float(st.session_state.sgd_comparison)
                diff = sgd_comparison - converted_sgd
                perc_diff = (sgd_comparison - converted_sgd) / sgd_comparison * 100

                st.write("")
                st.markdown('''
                            Difference : :red[\$ {} ({}%)]
                            '''.format(
                                format_number(diff,is_yen=False),
                                round(perc_diff,4),
                            )
                )

        else:
            st.error("Input is not a number!")
    

with tab3:
    st.session_state.orig_yen = st.text_input("Amount (¥)", value=st.session_state.orig_yen, key="tab3_orig_yen")
    st.session_state.exchange_rate = st.text_input("Exchange rate", value=st.session_state.exchange_rate, key="tab3_fx_rate")
    tax_rate = st.radio("Tax rate",["10%", "8%"],horizontal=True, key="tab3_tax_rate")

    if len(st.session_state.orig_yen) > 0 and len(st.session_state.exchange_rate) > 0:
        if is_float(st.session_state.orig_yen) and is_float(st.session_state.exchange_rate):

            orig_yen = float(st.session_state.orig_yen)
            tax_rate = int(tax_rate[:-1])/100

            amt_excluding_tax = orig_yen / (1+tax_rate)
            tax_amount =  orig_yen - amt_excluding_tax
            
            converted_sgd = amt_excluding_tax * float(st.session_state.exchange_rate)

            st.write("")
            st.markdown('''
                        Tax amount : ¥ {}

                        Amount excluding tax : ¥ {}
                        
                        **Amount in SGD** : :red[\$ {}]
                        '''.format(
                            format_number(tax_amount, is_yen=True),
                            format_number(amt_excluding_tax, is_yen=True),
                            format_number(converted_sgd,is_yen=False)
                        )
            )

            st.write("---")
            st.session_state.sgd_comparison = st.text_input("SGD comparison (SGD)", value=st.session_state.sgd_comparison, key="tab3_sgd_comparison")

            if len(st.session_state.sgd_comparison) > 0 and is_float(st.session_state.sgd_comparison):
                sgd_comparison = float(st.session_state.sgd_comparison)
                diff = sgd_comparison - converted_sgd
                perc_diff = (sgd_comparison - converted_sgd) / sgd_comparison * 100

                st.write("")
                st.markdown('''
                            Difference : :red[\$ {} ({}%)]
                            '''.format(
                                format_number(diff,is_yen=False),
                                round(perc_diff,4),
                            )
                )

        else:
            st.error("Input is not a number!")    

