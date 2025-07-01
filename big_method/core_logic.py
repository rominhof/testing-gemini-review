from typing import Optional, Iterator
import logging
import textwrap
from dataclasses import dataclass

REPORT_WIDTH = 50

@dataclass
class AnalysisResults:
    total_lines: int
    total_words: int
    total_characters: int
    filtered_lines: list[str]


def read_lines(input_file_path: str) -> Iterator[str]:
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        logging.error(f"Error: The file '{input_file_path}' was not found.")
        raise
    except OSError as e:
        logging.error(f"Error reading file: {e}")
        raise

def compute_statistics(lines: Iterator[str]) -> AnalysisResults:
    total_lines = 0
    total_words = 0
    total_characters = 0
    all_lines = []

    for line in lines:
        total_lines += 1
        total_words += len(line.split())
        total_characters += len(line)
        all_lines.append(line)

    return AnalysisResults(total_lines, total_words, total_characters, all_lines)

def filter_lines(lines: list[str], keyword: Optional[str]) -> list[str]:
    if not keyword:
        return []
    keyword_lower = keyword.lower()
    return [line for line in lines if keyword_lower in line.lower()]


def read_and_analyze(input_file_path: str, keyword_filter: Optional[str]) -> AnalysisResults:
    logging.info(f"Starting file processing: {input_file_path}")

    lines = list(read_lines(input_file_path))
    stats = compute_statistics(iter(lines))
    filtered = filter_lines(stats.filtered_lines, keyword_filter)

    logging.info("Input file processed successfully.")
    if keyword_filter:
        logging.info(f"Filtering by '{keyword_filter}' completed. {len(filtered)} lines found.")
    else:
        logging.info("No filter keyword provided. Skipping filtering.")

    return AnalysisResults(
        total_lines=stats.total_lines,
        total_words=stats.total_words,
        total_characters=stats.total_characters,
        filtered_lines=filtered
    )


def generate_report(input_file_path: str, keyword_filter: Optional[str], analysis_results: AnalysisResults) -> list[str]:
    report_content = []
    report_content.append("="*REPORT_WIDTH)
    report_content.append("           FILE ANALYSIS REPORT           ")
    report_content.append("="*REPORT_WIDTH)
    report_content.append(f"\nAnalyzed File: {input_file_path}")
    report_content.append(f"Total Lines: {analysis_results.total_lines}")
    report_content.append(f"Total Words: {analysis_results.total_words}")
    report_content.append(f"Total Characters: {analysis_results.total_characters}")

    if keyword_filter:
        report_content.append(f"\n--- Lines Containing '{keyword_filter}' ({len(analysis_results.filtered_lines)} lines) ---")
        if analysis_results.filtered_lines:
            for i, f_line in enumerate(analysis_results.filtered_lines):
                report_content.append(f"  {i+1}. {f_line}")
        else:
            report_content.append("  No lines found with the keyword.")
    else:
        report_content.append("\n--- No filter keyword applied ---")

    report_content.append("\n" + "="*REPORT_WIDTH)

    return report_content


def write_report(output_file_path:str, report_content:list[str]) -> None:
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f_out:
            for report_line in report_content:
                f_out.write(report_line + '\n')
        logging.info(f"\nReport successfully generated at: {output_file_path}")
    except OSError as e:
        logging.error(f"Error saving report: {e}")
        raise

def create_sample(input_filename:str) -> None:
    sample_content = textwrap.dedent("""\
        This is the first line of our test file.
        It contains some words for counting.
        It also has the keyword 'demonstration'.
        Another line of text.
        Demonstration of functionality.
        End of test file.\n""")

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
    analysis_results = read_and_analyze(input_filename,keyword_filter)
    # Generate Report
    report_content = generate_report(input_filename, keyword_filter, analysis_results)
    # Write output
    write_report(output_filename, report_content)