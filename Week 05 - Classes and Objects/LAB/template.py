class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the value as a percentage of the limit."""
        if self.limit <= 0:
            raise ValueError("The limit must be greater than zero.")

        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        return "OK"


def load_records(path):
    """Load comma-separated label, value, and limit rows from a file."""
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            fields = [field.strip() for field in line.split(",")]
            if len(fields) != 3:
                raise ValueError(f"Invalid record on line {line_number}.")
            label, value, limit = fields
            try:
                records.append(Record(label, float(value), float(limit)))
            except ValueError as error:
                raise ValueError(f"Invalid record on line {line_number}: {error}") from error

    return records


def main():
    """Load records and print a status report for each one."""
    try:
        records = load_records("records_sample.txt")
    except FileNotFoundError:
        records = [
            Record("Water", 92, 100),
            Record("Electricity", 105, 100),
            Record("Heating", 75, 100),
        ]

    over_count = 0
    for record in records:
        status = record.status()
        print("=" * 34)
        print(f"  RECORD CHECK - {record.label}")
        print(f"Value : {record.value:g}")
        print(f"Limit : {record.limit:g}")
        print(f"Status: {status}")
        print("=" * 34)
        if status == "OVER LIMIT":
            over_count += 1

    print(f"Records over limit: {over_count}")


if __name__ == "__main__":
    main()
