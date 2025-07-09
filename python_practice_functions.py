def clean_rows(data):
    cleaned_data = []
    for row in data:

        if row["score"].strip() != "":
            score = int(row["score"].strip())
        else:
            continue

        if row["name"]:
            name = row["name"].strip()

        if row["city"]:
            city = row["city"].strip()

        cleaned_data.append({"name": name, "score": score, "city": city})

    return cleaned_data


def clean_rows_efficient(data):
    cleaned_data = []
    for row in data:
        if row["score"].strip():
            score = int(row["score"].strip())
            if score and row["name"] and row["city"]:
                cleaned_data.append(
                    {"name": row["name"], "score": score, "city": row["city"]}
                )

    return cleaned_data


def filter_high_scores(data, threshold):
    threshold_names = []
    for row in data:
        if row["score"].strip():
            score = int(row["score"].strip())
            if score >= threshold:
                threshold_names.append(row["name"].strip())
    return threshold_names


def clean_sales_data(data):
    cleaned_rows = []
    for row in data:
        if row["amount"].strip():
            amount = float(row["amount"].strip())
            customer = row["customer"].strip()
            date = row["date"].strip()
            cleaned_rows.append({"customer": customer, "amount": amount, "date": date})
    return cleaned_rows


def filter_transactions(data, threshold):
    valid_ids = []
    for row in data:
        if row["amount"].strip():
            amount = int(row["amount"].strip())
            if amount >= threshold and row["status"] == "complete":
                valid_ids.append(row["id"].strip())
    return valid_ids
