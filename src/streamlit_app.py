import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# TIÊU ĐỀ WEB
# =========================

st.title("🔍 Hệ Thống Phát Hiện Gian Lận Kế Toán")

st.write(
    "📂 Tải file CSV hoặc Excel để phân tích giao dịch bất thường"
)

# =========================
# UPLOAD FILE
# =========================

uploaded_file = st.file_uploader(
    "Chọn file dữ liệu",
    type=["csv", "xlsx"]
)

# =========================
# ĐỌC FILE
# =========================

if uploaded_file is not None:

    try:

        # Nếu là CSV
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)

        # Nếu là Excel
        elif uploaded_file.name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file)

        # =========================
        # HIỂN THỊ DỮ LIỆU
        # =========================

        st.subheader("📄 Dữ liệu giao dịch")

        st.dataframe(data.head(20))

        # =========================
        # KIỂM TRA CỘT
        # =========================

        required_columns = ['Time', 'Amount', 'Class']

        missing_columns = []

        for col in required_columns:

            if col not in data.columns:
                missing_columns.append(col)

        # Nếu thiếu cột
        if len(missing_columns) > 0:

            st.error(
                f"❌ Thiếu cột dữ liệu: {missing_columns}"
            )

        else:

            # =========================
            # THỐNG KÊ
            # =========================

            fraud_count = data['Class'].sum()

            normal_count = len(data) - fraud_count

            total_transactions = len(data)

            st.subheader("📊 Thống kê giao dịch")

            st.success(
                f"✅ Giao dịch bình thường: {normal_count}"
            )

            st.error(
                f"🚨 Giao dịch gian lận: {fraud_count}"
            )

            st.info(
                f"📌 Tổng số giao dịch: {total_transactions}"
            )

            # =========================
            # LỌC GIAO DỊCH GIAN LẬN
            # =========================

            suspicious = data[
                data['Class'] == 1
            ].copy()

            # =========================
            # PHÂN TÍCH LÝ DO
            # =========================

            reasons = []

            risk_levels = []

            for index, row in suspicious.iterrows():

                reason = []

                score = 0

                # Giao dịch lớn
                if row['Amount'] > 1000:
                    reason.append("💰 Số tiền lớn")
                    score += 1

                # Giao dịch thời gian bất thường
                if row['Time'] > 50000:
                    reason.append("🌙 Giao dịch đêm")
                    score += 1

                # Mức độ rủi ro
                if score >= 2:
                    risk = "🔴 Cao"

                elif score == 1:
                    risk = "🟠 Trung bình"

                else:
                    risk = "🟢 Thấp"

                reasons.append(", ".join(reason))

                risk_levels.append(risk)

            # =========================
            # THÊM CỘT PHÂN TÍCH
            # =========================

            suspicious['Mức độ rủi ro'] = risk_levels

            suspicious['Lý do nghi ngờ'] = reasons

            # =========================
            # HIỂN THỊ GIAO DỊCH ĐÁNG NGỜ
            # =========================

            st.subheader(
                "⚠️ Danh sách giao dịch đáng ngờ"
            )

            st.dataframe(

                suspicious[
                    [
                        'Time',
                        'Amount',
                        'Mức độ rủi ro',
                        'Lý do nghi ngờ'
                    ]
                ]

            )

            # =========================
            # BIỂU ĐỒ
            # =========================

            st.subheader("📈 Biểu đồ phân bố giao dịch")

            fig, ax = plt.subplots()

            ax.bar(
                ['Bình thường', 'Gian lận'],
                [normal_count, fraud_count]
            )

            ax.set_ylabel("Số lượng")

            ax.set_title(
                "Phân bố giao dịch tài chính"
            )

            st.pyplot(fig)

            # =========================
            # GIAO DỊCH GIÁ TRỊ CAO
            # =========================

            st.subheader(
                "💸 Giao dịch giá trị lớn"
            )

            high_amount = data[
                data['Amount'] > 5000
            ]

            st.dataframe(
                high_amount[
                    ['Time', 'Amount', 'Class']
                ]
            )

    except Exception as e:

        st.error(f"❌ Lỗi xử lý file: {e}")