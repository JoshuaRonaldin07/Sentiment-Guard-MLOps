import pandas as pd

data = {
    'text': [
        "I absolutely love this new update! Everything is so fast.",
        "The customer support was rude and didn't help me at all.",
        "Average product, does what it says but nothing special.",
        "Total waste of money. The app crashes every five minutes.",
        "Amazing experience, will definitely recommend to my friends!",
        "I am so frustrated with the slow loading times."
    ]
}

df = pd.DataFrame(data)
df.to_csv("./data_inbox/batch_test_01.csv", index=False)
print(" Test file 'batch_test_01.csv' created in data_inbox!")