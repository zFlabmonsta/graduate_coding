from faker import Faker
import random
import json
fake = Faker(['en-AU'])

members = []
for id in range(15000):
    members.append({
        'id': id, 
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'address': fake.address(),
        'active': bool(random.getrandbits(1))

    })

json_file = open('members.json', 'w')
json_file.write(json.dumps(members))
json_file.close()

print(fake.address())