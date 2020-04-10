import csv

subscribers_older_than_30_referred_by_google = []

# Read csv
with open('csv/newsletter_subscribers.csv', 'r') as newsletter_subscribers_csv:
    csv_dict_reader = csv.DictReader(newsletter_subscribers_csv)

    for row in csv_dict_reader:
        # Subscriber must be older than 30 years old
        # Subscriber must have been referred by google
        age = int(row['age'])
        referred_by = row['referred_by']
        if age >= 30 and referred_by == 'google':
            subscribers_older_than_30_referred_by_google.append({
                'name': row['name'],
                'email': row['email']
            })

# Write new csv
with open(
        'csv/subscribers_older_than_30_referred_by_google.csv',
        'w',
        newline=''
) as subscribers_older_than_30_referred_by_google_csv:
    fieldnames = ['name', 'email']
    csv_dict_writer = csv.DictWriter(subscribers_older_than_30_referred_by_google_csv, fieldnames=fieldnames)
    csv_dict_writer.writeheader()

    for subscribe in subscribers_older_than_30_referred_by_google:
        csv_dict_writer.writerow(subscribe)
