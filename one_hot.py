import pandas as pd
import random

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})

categories = ["robot", "human"]

for category in categories:
    data[f"{category}"] = (data["whoAmI"] == category).astype(int)

data = data.drop("whoAmI", axis=1)

print(data)
