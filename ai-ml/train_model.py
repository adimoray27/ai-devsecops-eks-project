import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Mock CVE data: exploits, age_days, popularity → vuln_risk
data = {'exploits': [1,0,0,2,1,0], 'age_days': [365,30,90,730,180,45], 
        'popularity': [1000,500,200,5000,1500,300], 'vuln': [1,0,0,1,1,0]}
df = pd.DataFrame(data)

model = RandomForestClassifier(n_estimators=10)
model.fit(df[['exploits','age_days','popularity']], df['vuln'])
joblib.dump(model, 'vuln_model.pkl')
print("✅ AI Model trained & saved!")
