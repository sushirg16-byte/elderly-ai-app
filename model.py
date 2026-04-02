from sklearn.ensemble import RandomForestClassifier

# Sample data
X = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1],
    [0, 0, 0]
]

y = ["Flu", "Cold", "Flu", "Healthy"]

model = RandomForestClassifier()
model.fit(X, y)

def predict(data):
    return model.predict([data])[0]