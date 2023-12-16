# myapp/management/commands/import_data.py
import csv
from django.core.management.base import BaseCommand
import re
import os
from datetime import datetime

from stock.models import IndexModel, StockModel

class Command(BaseCommand):
    help = 'Import data from CSV files in a folder into YourModel'

    def add_arguments(self, parser):
        parser.add_argument('folder_path', type=str, help='Path to the folder containing CSV files')

    def handle(self, *args, **options):
        folder_path = options['folder_path']
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(folder_path, filename)
                self.import_data_from_file(file_path)

    def import_data_from_file(self, csv_file):
        filename = os.path.basename(csv_file)
        match = re.match(
            r'(.+)-(\d{2}-\d{2}-\d{4})-to-(\d{2}-\d{2}-\d{4}).csv', filename)

        if match:
            extracted_filename = match.group(1).strip()
            start_date_string = match.group(2).strip()
            end_date_string = match.group(3).strip()
            start_date = datetime.strptime(start_date_string, "%d-%m-%Y")
            end_date = datetime.strptime(end_date_string, "%d-%m-%Y")

            print("Extracted Information:")
            print(f"Filename: {extracted_filename}")
            print(f"Start Date: {start_date}")
            print(f"End Date: {end_date}")
            # Your logic to read and import data from the CSV file
            index_obj = IndexModel(
                name=extracted_filename.replace(" ", "-"),
                start_date=start_date,
                end_date=end_date,
            )
            index_obj.save()
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row if present

                for row in reader:
                    if row[5]:
                        StockModel.objects.create(
                            date=datetime.strptime(row[0], "%d-%b-%Y"),
                            index_name=index_obj,
                            open_price=row[1],
                            high_price=row[2],
                            low_price=row[3],
                            close_price=row[4],
                            shares_traded=row[5],
                            turnover=row[6]
                        )

            self.stdout.write(self.style.SUCCESS(
                f'Data imported successfully from {filename}.'))
        else:
            print(f"Filename {filename} does not match the expected pattern.")