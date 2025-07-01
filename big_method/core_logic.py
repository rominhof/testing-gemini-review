import os
import logging
import textwrap

def read_and_analyze(input_file_path, keyword_filter):
    logging.info(f"Starting file processing: {input_file_path}")
    
    total_lines = 0
    total_words = 0
    total_characters = 0
    filtered_lines = []
    
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f_in:
            keyword_lower = keyword_filter.lower() if keyword_filter else None
            for line in f_in:
                stripped_line = line.strip()
                total_lines += 1
                total_words += len(stripped_line.split())
                total_characters += len(stripped_line)
                
                if keyword_lower and keyword_lower in stripped_line.lower():
                    filtered_lines.append(stripped_line)
        logging.info("Input file processed successfully.")
    except FileNotFoundError:
        logging.error(f"Error: The file '{input_file_path}' was not found.")
        raise
    except OSError as e:
        logging.error(f"Error reading file: {e}")
        raise

    if keyword_filter:
        logging.info(f"Filtering by '{keyword_filter}' completed. {len(filtered_lines)} lines found.")
    else:
        logging.info("No filter keyword provided. Skipping filtering.")

    return total_lines, total_words, total_characters, filtered_lines


def generate_report(input_file_path, total_lines, total_words, total_characters, keyword_filter, filtered_lines):
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
        report_content.append("\n--- No filter keyword applied ---")

    report_content.append("\n" + "="*50)

    return report_content


def write_report(output_file_path, report_content):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f_out:
            for report_line in report_content:
                f_out.write(report_line + '\n')
        logging.info(f"\nReport successfully generated at: {output_file_path}")
    except OSError as e:
        logging.error(f"Error saving report: {e}")

def create_sample(input_filename):
    sample_content = textwrap.dedent("""\
        This is the first line of our test file.
        It contains some words for counting.
        It also has the keyword 'demonstration'.
        Another line of text.
        Demonstration of functionality.
        End of test file.""")

    with open(input_filename, 'w', encoding='utf-8') as f_sample:
        f_sample.write(sample_content.strip())
    logging.info(f"Sample file '{input_filename}' created for testing.\n")    


if __name__ == "__main__":
    input_filename = "sample_data.txt"
    output_filename = "analysis_report.txt" 
    keyword_filter = "demonstration"
   
    # Create sample file to be processed   
    create_sample(input_filename)
    # Process the report
    total_lines, total_words, total_characters, filtered_lines = read_and_analyze(input_filename,keyword_filter)
    # Generate Report
    report_content = generate_report(input_filename, total_lines, total_words, total_characters, keyword_filter, filtered_lines)
    # Write output
    write_report(output_filename, report_content)