import os

def process_and_generate_report(input_file_path, output_file_path, keyword_filter):
    print(f"Starting file processing: {input_file_path}")
    
    file_lines = []
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                file_lines.append(line.strip())
        print("Input file read successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    total_lines = len(file_lines)
    total_words = 0
    total_characters = 0
    for line in file_lines:
        words = line.split()
        total_words += len(words)
        total_characters += len(line)

    print("Data processed: counts performed.")

    filtered_lines = []
    if keyword_filter:
        for line in file_lines:
            if keyword_filter.lower() in line.lower():
                filtered_lines.append(line)
        print(f"Filtering by '{keyword_filter}' completed. {len(filtered_lines)} lines found.")
    else:
        print("No filter keyword provided. Skipping filtering.")

    report_content = []
    report_content.append("="*50)
    report_content.append("           FILE ANALYSIS REPORT           ")
    report_content.append("="*50)
    report_content.append(f"\nAnalyzed File: {input_file_path}")
    report_content.append(f"Total Lines: {total_lines}")
    report_content.append(f"Total Words: {total_words}")
    report_content.append(f"Total Characters: {total_characters}")

    if keyword_filter:
        report_content.append(f"\n--- Lines Containing '{keyword_filter}' ({len(filtered_lines)} lines) ---")
        if filtered_lines:
            for i, f_line in enumerate(filtered_lines):
                report_content.append(f"  {i+1}. {f_line}")
        else:
            report_content.append("  No lines found with the keyword.")
    else:
        report_content.append("\n--- No filter