import streamlit as st
import datetime

# تعديل شكل الصفحة والألوان
st.set_page_config(
    page_title="Genetic and Chronic Diseases App",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# خلفية وألوان مبهجة
page_bg_img = """
<style>
body {
background-color: #e0f7fa;
color: #00695c;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# عنوان رئيسي
st.title("🧬 Genetic and Chronic Diseases Explorer")
st.write("استكشاف شامل للأمراض الوراثية والمزمنة - Detailed medical insights.")

# خانة الموبايل أو الإيميل
st.sidebar.header("Set Reminder")
contact = st.sidebar.text_input("Enter your phone number or email (أدخل رقم هاتفك أو بريدك الإلكتروني):")
reminder_time = st.sidebar.time_input("Select reminder time (حدد وقت التذكير):", datetime.time(9, 0))

# قائمة الأمراض
diseases = [
    "Type 1 Diabetes",
    "Cystic Fibrosis",
    "Sickle Cell Anemia",
    "Hereditary Cancer",
    "Down Syndrome",
    "Aplastic Anemia",
    "Hereditary Blindness",
    "Wilson's Disease",
    "Multiple Sclerosis",
    "Lupus (SLE)",
    "Rheumatoid Arthritis",
    "Hypertension",
    "Asthma",
    "Type 2 Diabetes",
    "Autism Spectrum Disorder",
    "Schizophrenia",
    "Breast Cancer",
    "Alzheimer's Disease",
    "Amyotrophic Lateral Sclerosis (ALS)"
]

# اختيار المرض
selected_disease = st.selectbox("Choose a Disease (اختر مرضًا):", diseases)

# دالة عرض المعلومات
def show_disease_info(name):
    if name == "Type 1 Diabetes":
        st.header("Type 1 Diabetes (سكري النوع الأول)")
        st.subheader("Definition (تعريف):")
        st.write("Type 1 diabetes is a chronic condition in which the pancreas produces little or no insulin. It usually appears during childhood or adolescence.")
        st.write("سكري النوع الأول هو حالة مزمنة حيث ينتج البنكرياس القليل أو لا ينتج الإنسولين. يظهر عادة في الطفولة أو المراهقة.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Increased thirst (العطش الشديد)
        - Frequent urination (التبول المتكرر)
        - Hunger (الجوع)
        - Fatigue (التعب)
        - Blurred vision (تشوش الرؤية)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("An autoimmune destruction of insulin-producing beta cells in the pancreas triggered by genetic factors and possibly viruses.")
        st.write("تدمير مناعي ذاتي لخلايا بيتا المنتجة للإنسولين في البنكرياس، ناجم عن عوامل وراثية وربما فيروسات.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("""
        - Administer fast-acting sugar if low blood sugar suspected (تناول سكر سريع الامتصاص في حالة الاشتباه في انخفاض السكر).
        - Monitor blood glucose levels regularly (مراقبة مستويات السكر باستمرار).
        - Seek emergency help if unconsciousness occurs (طلب إسعاف في حالة فقدان الوعي).
        """)

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Autoimmune Genetic Disorder (اضطراب مناعي وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with genes like HLA-DR3 and HLA-DR4, affecting immune response.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Maintain a consistent eating schedule and monitor your blood sugar before and after meals.")
        st.success("احرص على تناول وجبات منتظمة ومراقبة السكر قبل وبعد الأكل.")

    elif name == "Cystic Fibrosis":
        st.header("Cystic Fibrosis (التليف الكيسي)")
        st.subheader("Definition (تعريف):")
        st.write("A genetic disorder that affects the lungs, pancreas, and other organs, causing thick, sticky mucus production.")
        st.write("اضطراب جيني يؤثر على الرئتين والبنكرياس وأعضاء أخرى، ويسبب إنتاج مخاط سميك ولزج.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Chronic cough (سعال مزمن)
        - Difficulty breathing (صعوبة في التنفس)
        - Frequent lung infections (عدوى رئوية متكررة)
        - Poor growth (نمو ضعيف)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Caused by mutations in the CFTR gene, affecting chloride channels and leading to mucus buildup.")
        st.write("ينتج عن طفرات في جين CFTR تؤثر على قنوات الكلوريد وتؤدي إلى تراكم المخاط.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("""
        - Chest physiotherapy to clear mucus (العلاج الطبيعي للصدر لتنظيف المخاط).
        - Use of medications like bronchodilators (استخدام أدوية مثل موسعات الشعب الهوائية).
        - Seek medical advice for respiratory distress (طلب استشارة طبية في حالة ضيق التنفس).
        """)

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Disorder (اضطراب وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Caused by mutations in the CFTR gene, leading to faulty chloride transport.")
        st.write("ناجم عن طفرات في جين CFTR مما يؤدي إلى النقل الخاطئ للكلوريد.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Early diagnosis and lung function monitoring are crucial for better management.")
        st.success("التشخيص المبكر ومراقبة وظائف الرئة أمران حاسمان لإدارة أفضل.")

    # (تكملة الأمراض الأخرى بنفس الطريقة)
    # نكمل باقي الأمراض بالطريقة نفسها

# عرض معلومات المرض
show_disease_info(selected_disease)
