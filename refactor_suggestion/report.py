def generate_report(data):
    result = []
    for item in data:
        if item['status'] == 'active':
            formatted = f"{item['id']} - {item['name'].upper()}"
            result.append(formatted)
    print("=== Report ===")
    for r in result:
        print(r)