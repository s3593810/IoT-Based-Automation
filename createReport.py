import csv
import sqlite3 as lite
from glob import glob
from SenseHatDB import SensehatDB
from os.path import expanduser
from App_Logging import SenseHatApp_logging
# Generating report in CSV file
log = SenseHatApp_logging()


class Report:
    db = SensehatDB()

    def Rep(self):
        data = self.db.reportDB()
        with open("Report.csv", "w", newline='') as csv_file:  # Python 3 version
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Date", "States", "Message"])  # Header
            for date, value in data.items():
                if value[1] and value[2] is not None:
                    message = [' and  '.join([value[1], value[2]])]
                    csv_writer.writerow(
                        [date, value[0], message[0]])
                elif value[1] is None:
                    csv_writer.writerow(
                        [date, value[0], value[2]])
                else:
                    csv_writer.writerow(
                        [date, value[0], value[1]])
        log.logger.info("The report is successfully generated")


# Execute program.
if __name__ == "__main__":
    Report().Rep()
