# GeoJson-Data-of-Indian-States
GeoJson Data of Indian States with boundaries 

JSON format contains all Indian states with Proper unique "ID", "ISO", "State_Name" and the most important part is Geological Points of each State boundaries which matches with World MAP Standardization.


# 📊 PhonePe Transaction & Insurance Insights Dashboard

An end-to-end data analysis and interactive visualization dashboard built on real PhonePe Pulse data — covering transactions, users, and insurance across all Indian states and districts.

![PhonePe Logo](PhonePe-Logo.wine.png)

---

## 🚀 Live Demo


---

## 📌 Features

- 🗺️ **Geo-visualization** of transactions and insurance data across Indian states using GeoJSON maps
- 📈 **Interactive charts** for aggregated transaction trends, user growth, and insurance adoption
- 🏦 **MySQL integration** for structured data storage and querying
- 🔍 **Drill-down analysis** — State → District → Pincode level insights
- 📊 **PowerPoint report** summarizing key business insights

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Streamlit | Interactive web dashboard |
| MySQL | Database storage and querying |
| Pandas & NumPy | Data processing and analysis |
| Plotly | Interactive charts and geo maps |
| GeoJSON | India state boundary mapping |
| Jupyter Notebook | Exploratory data analysis |

---

## 📂 Project Structure

```
├── app.py                          # Main Streamlit dashboard
├── phonepay_insight1.ipynb         # Exploratory Data Analysis notebook
├── phonepaymysql.sql               # MySQL schema and queries
├── aggregated_transactions.csv     # State-level transaction data
├── aggregated_users.csv            # State-level user data
├── aggregated_insurance_phonepe.csv# State-level insurance data
├── map_transactions1.csv           # District-level transaction data
├── map_users1.csv                  # District-level user data
├── map_insurance_phonepe.csv       # District-level insurance data
├── top_transactions.csv            # Top pincode/district transactions
├── top_users.csv                   # Top pincode/district users
├── top_insurance_phonepe.csv       # Top pincode/district insurance
├── india_state.geojson             # India GeoJSON boundary file
├── PhonePay Insightsreport.docx    # Detailed analysis report
├── PhonePe Transaction & Insurance Insights Analysisppt.pptx  # PPT report
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/amitkumarjy/remo.git

# 2. Navigate to project folder
cd remo

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up MySQL database
mysql -u root -p < phonepaymysql.sql

# 5. Run the Streamlit app
streamlit run app.py
```

---

## 🧠 How It Works

1. **Data Collection** — PhonePe Pulse public dataset covering transactions, users, and insurance across states, districts, and pincodes
2. **Data Processing** — Cleaned and structured using Pandas, stored in MySQL for efficient querying
3. **Geo Visualization** — India state boundaries mapped using GeoJSON with Plotly choropleth maps
4. **Dashboard** — Streamlit app with filters for Year, Quarter, State, and Metric type
5. **Insights** — Transaction volume trends, top performing states, insurance penetration analysis

---

## 📊 Key Insights

- 📍 Top states by digital transaction volume
- 📱 User growth trends across quarters
- 🛡️ Insurance adoption patterns across India
- 💳 Transaction type distribution (Peer-to-peer, Merchant payments, etc.)

---

## 📸 Screenshots

![Dashboard](phnoepay.png)

> Add more screenshots of your dashboard here

---

## 👨‍💻 Author

**Amit Mutyalwar**  
Data Scientist | ML Engineer  
[LinkedIn](https://www.linkedin.com/in/amitkumar-mutyalwar-56519723b/) | [GitHub](https://github.com/amitkumarjy)

---

## 📄 Reports

- 📝 [Detailed Analysis Report](PhonePay%20Insightsreport.docx)
- 📊 [Presentation](PhonePe%20Transaction%20%26%20Insurance%20Insights%20Analysisppt.pptx)

---

## ⭐ If you found this useful, give it a star!
