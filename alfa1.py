
import streamlit as st
import datetime

st.set_page_config(page_title="Alfa 1 - Smart Assistant", layout="centered")
st.title("مرحباً بك في Alfa 1 - مساعدك الذكي")
st.markdown("### اختر ما تريد القيام به:")

notes = {}

if "notes" not in st.session_state:
    st.session_state.notes = {}

menu = st.radio("القائمة الرئيسية", ["إضافة ملاحظة", "عرض الملاحظات", "بحث", "حول"])

if menu == "إضافة ملاحظة":
    section = st.text_input("القسم", placeholder="مثلاً: الدراسة، الشغل، أفكار...")
    note = st.text_area("اكتب ملاحظتك هنا")
    if st.button("حفظ الملاحظة"):
        if section and note:
            date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            st.session_state.notes[date] = {"section": section, "note": note}
            st.success("تم حفظ الملاحظة بنجاح")
        else:
            st.warning("من فضلك املأ كل الحقول")

elif menu == "عرض الملاحظات":
    if st.session_state.notes:
        for date, data in sorted(st.session_state.notes.items(), reverse=True):
            st.markdown(f"**{data['section']}** - `{date}`")
            st.markdown(f"> {data['note']}")
    else:
        st.info("لا توجد ملاحظات بعد")

elif menu == "بحث":
    query = st.text_input("اكتب كلمة البحث")
    if query:
        results = {d: v for d, v in st.session_state.notes.items() if query.lower() in v['note'].lower() or query in v['section']}
        if results:
            for date, data in results.items():
                st.markdown(f"**{data['section']}** - `{date}`")
                st.markdown(f"> {data['note']}")
        else:
            st.warning("لا توجد نتائج مطابقة")
elif menu == "حول":
    st.markdown("تم تطويره بواسطة Alfa-fares123")
    st.markdown("مشروع مفتوح المصدر لتجربة بناء مساعد ذكي شخصي باستخدام Python و Streamlit")
