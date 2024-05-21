import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)


a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)