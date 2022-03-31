# hack 1

InfoDb = []

InfoDb.append({
  "airline": "United",
  "model": "737",
  "manufacturer": "Boeing",
  "yearmade": 2005,
  "pilots": ["James", "Bob", "John"]
})

InfoDb.append({
  "airline": "Air Canada",
  "model": "767",
  "manufacturer": "Boeing",
  "yearmade": 1990,
  "pilots": ["Jim", "Fred", "Bill"]
})

InfoDb.append({
  "airline": "American Airlines",
  "model": "A320",
  "manufacturer": "Airbus",
  "yearmade": 2010,
  "pilots": ["Jason", "Pamela", "Josh"]
})

InfoDb.append({
  "airline": "American Airlines",
  "model": "767",
  "manufacturer": "Boeing",
  "yearmade": 1995,
  "pilots": ["Cherise", "Lucy", "Shawn"]
})


# hack 2a

def print_dbrow(row_idx):
  print(InfoDb[row_idx]["airline"], InfoDb[row_idx]["manufacturer"], InfoDb[row_idx]["model"])
  print("\t", "Pilots:", ", ".join(InfoDb[row_idx]["pilots"]))

def for_loop_print():
  for idx in range(len(InfoDb)):
    print_dbrow(idx)


# hack 2b

def while_loop_print(idx):
  while idx < len(InfoDb):
    print_dbrow(idx)
    idx += 1


# hack 2c

def recursive_print(idx):
  if idx == len(InfoDb):
    return
  print_dbrow(idx)
  recursive_print(idx + 1)

def tester():
  print("Testing for_loop_print")
  for_loop_print()
  print()

  print("Testing while_loop_print")
  while_loop_print(0)
  print()

  print("Testing recursive_print")
  recursive_print(0)
  print()

