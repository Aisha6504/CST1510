"""
RECORD CHECK  -  my version
===========================

Name  : Aisha Ahmed
Lane  :  AI   
Date  : 17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Calculate record statistics."""

    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status
def print_report(label, difference, percent, status):
    """Print a record report."""
    print("Label:", label)
    print("Difference:", difference)
    print("Percent:", percent)
    print("Status:", status)


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
def load_records(path):
    """Load records from a file into a list of dictionaries."""

    records = []

    try:
        with open(path, "r") as f:
            for line in f:
                label, value, limit = line.strip().split(",")

                record = {
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                }

                records.append(record)

    except FileNotFoundError:
        print("File not found:", path)
        return []

    return records


# Load the records
records = load_records("records_sample.txt")

# Print results and write them to results.txt
with open("results.txt", "w") as f:
    for record in records:
        difference, percent, status = check_record(
            record["value"],
            record["limit"]
        )
        f.write(f"{record['label']},{status}\n")

# Read the file back and print its contents
print("\nContents of results.txt:")

with open("results.txt", "r") as f:
    print(f.read())

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

over_limit_count = 0

for record in records:

    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print_report(
        record["label"],
        difference,
        percent,
        status
    )

    if status == "OVER LIMIT":
        over_limit_count += 1

print("OVER LIMIT records:", over_limit_count)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
