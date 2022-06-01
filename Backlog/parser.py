with open('./data_1.txt', 'r') as f:
    data_str = f.read()
data_str = data_str[1:-1]
text_2 = str(data_str)
for i in range(100):
  text_2 = text_2.replace(f"id\":{i},", f"id\":{i},\"responses\":"+"{")
text_2 = text_2.replace(",{\"subject", "},{\"subject")
text_2 = text_2 + "}"
print(text_2)

with open('data_1.json', 'w') as f:
  f.write(text_2)