import pandas as pd
import matplotlib.pyplot as plt
import os
import random
import folium

# ================= SETUP =================
if not os.path.exists("graphs"):
    os.makedirs("graphs")

# ================= LOAD DATA =================
df = pd.read_csv("cdr_voice.csv")
df_sms = pd.read_csv("cdr_sms.csv")

# ================= CLEANING =================
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour
df_sms['Hour'] = pd.to_datetime(df_sms['Time'], format='%H:%M:%S').dt.hour
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# ================= BASIC INFO =================
print("=== BASIC INFO ===")
print("Total Calls:", len(df))
print("Total SMS:", len(df_sms))
print("Total Duration:", df['Duration_sec'].sum())

# ================= TOP CONTACTS =================
top_calls = df['Number'].value_counts().head(5)

print("\n=== TOP CONTACTED NUMBERS ===")
print(top_calls)

plt.figure()
top_calls.plot(kind='bar')
plt.title("Top Contacts (Calls)")
plt.xlabel("Number")
plt.ylabel("Call Count")
plt.tight_layout()
plt.savefig("graphs/top_contacts.png")
plt.close()

# ================= ACTIVE HOURS =================
active_hours = df['Hour'].value_counts().sort_index()

print("\n=== ACTIVE HOURS (CALLS) ===")
print(active_hours)

plt.figure()
active_hours.plot(kind='bar')
plt.title("Active Hours (Calls)")
plt.xlabel("Hour")
plt.ylabel("Calls")
plt.tight_layout()
plt.savefig("graphs/active_hours.png")
plt.close()

# ================= DAILY TREND =================
daily_calls = df.groupby(df['Date'].dt.day).size()

print("\n=== DAILY CALL TREND ===")
print(daily_calls)

plt.figure()
daily_calls.plot(kind='line', marker='o')
plt.title("Daily Call Activity")
plt.xlabel("Day")
plt.ylabel("Calls")
plt.tight_layout()
plt.savefig("graphs/daily_trend.png")
plt.close()

# ================= SMS ANALYSIS =================
top_sms = df_sms['Number'].value_counts().head(5)

print("\n=== TOP SMS CONTACTS ===")
print(top_sms)

plt.figure()
top_sms.plot(kind='bar')
plt.title("Top SMS Contacts")
plt.xlabel("Number")
plt.ylabel("SMS Count")
plt.tight_layout()
plt.savefig("graphs/top_sms.png")
plt.close()

sms_hours = df_sms['Hour'].value_counts().sort_index()

print("\n=== SMS ACTIVE HOURS ===")
print(sms_hours)

plt.figure()
sms_hours.plot(kind='bar')
plt.title("SMS Active Hours")
plt.xlabel("Hour")
plt.ylabel("SMS Count")
plt.tight_layout()
plt.savefig("graphs/sms_hours.png")
plt.close()

# ================= TELECOM DETAILS =================
operator_map = {
    "733": ("404", "45", "Airtel"),
    "756": ("404", "10", "Airtel"),
    "784": ("405", "51", "Jio"),
    "779": ("404", "84", "Vi"),
    "822": ("405", "52", "Jio"),
    "897": ("404", "86", "BSNL")
}

def generate_telecom_data(number):
    prefix = str(number)[:3]
    mcc, mnc, operator = operator_map.get(prefix, ("404", "00", "Unknown"))

    cell_id = random.randint(10000, 99999)
    lac = random.randint(1000, 9999)
    tac = random.randint(10000, 99999)

    return pd.Series([mcc, mnc, operator, cell_id, lac, tac])

df[['MCC','MNC','Operator','Cell_ID','LAC','TAC']] = df['Number'].apply(generate_telecom_data)

print("\n=== TELECOM DETAILS ===")
print(df[['Number','MCC','MNC','Operator','Cell_ID','LAC','TAC']].drop_duplicates().head(10))

# ================= MAP =================
base_lat = 12.9716
base_lon = 77.5946

def generate_location(cell_id):
    lat = base_lat + (cell_id % 100) * 0.0001
    lon = base_lon + (cell_id % 100) * 0.0001
    return lat, lon

m = folium.Map(location=[base_lat, base_lon], zoom_start=12, tiles='CartoDB positron')

for _, row in df.iterrows():
    lat, lon = generate_location(row['Cell_ID'])

    folium.Marker(
        location=[lat, lon],
        popup=f"Number: {row['Number']} | Operator: {row['Operator']} | Cell: {row['Cell_ID']}"
    ).add_to(m)

m.save("graphs/map.html")

print("\nMap saved → graphs/map.html")

# ================= SUSPICIOUS ANALYSIS =================
print("\n=== SUSPICIOUS ANALYSIS ===")

freq = df['Number'].value_counts()
long_calls = df[df['Duration_sec'] > 1000]['Number'].value_counts()
late_night = df[(df['Hour'] >= 0) & (df['Hour'] <= 5)]['Number'].value_counts()
short_calls = df[df['Duration_sec'] < 30]['Number'].value_counts()

score_df = pd.DataFrame({
    'Frequency': freq,
    'LongCalls': long_calls,
    'LateNight': late_night,
    'ShortCalls': short_calls
}).fillna(0)

score_df['Score'] = (
    score_df['Frequency']*2 +
    score_df['LongCalls']*3 +
    score_df['LateNight']*2 +
    score_df['ShortCalls']
)

score_df = score_df.sort_values(by='Score', ascending=False)

print("\nTop Suspicious Numbers:")
print(score_df.head())

plt.figure()
score_df.head(5)['Score'].plot(kind='bar')
plt.title("Top Suspicious Numbers")
plt.xlabel("Index")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("graphs/suspicious.png")
plt.close()