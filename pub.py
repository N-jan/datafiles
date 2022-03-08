from faker import Faker as fk
fake = fk()

def cook_txn(): 
    cardFull = fake.credit_card_full()
    address = fake.address()
    Amt = fake.pricetag()
    Curr = fake.currency_symbol()
    txnAmt = Curr + Amt[1:]
    txn = cardFull + address + '\n' + txnAmt + '\n'
    print(txn)
    return(txn.encode('utf-8'))



from google.cloud import pubsub_v1

# TODO(developer)
project_id = "de-cert-2022"
topic_id = "txn"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)


for n in range(1, 10):
    data_str = cook_txn()
    # Data must be a bytestring
    data = data_str.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

print(f"Published messages to {topic_path}.")
