
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Alpha 1 - مساعدك الذكي", layout="centered")

st.title("أهلاً بيك في ألفا 1 - مساعدك الذكي")
st.subheader("هنا هتقدر تسجل ملاحظاتك، وتبحث فيها بسهولة")

# تخزين الملاحظات
if "notes" not in st.session_state:
    st.session_state.notes = []

# إضافة ملاحظة
with st.form("add_note_form"):
    content = st.text_area("اكتب ملاحظتك هنا")
    submit = st.form_submit_button("إضافة")
    if submit and content.strip() != "":
        st.session_state.notes.append({
            "text": content.strip(),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success("تمت الإضافة!")

# البحث
search_query = st.text_input("ابحث في ملاحظاتك")
filtered_notes = [
    note for note in st.session_state.notes
    if search_query.lower() in note["text"].lower()
]

# عرض النتائج
st.write("### الملاحظات:")
for note in filtered_notes:
    st.write(f"- {note['date']}: {note['text']}")
