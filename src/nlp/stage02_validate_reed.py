"""
src/nlp/stage02_validate_case.py - Validate Stage
(EDIT YOUR COPY OF THIS FILE)

Source: Raw HTML string
Sink:   BeautifulSoup object (in memory)

Purpose

  Validates that the expected page structure is present.

Analytical Questions

- What is the top-level structure of the HTML document?
- What elements are present in the document?
- What data types are associated with each field?
- Does the data meet expectations for transformation?

Notes

Following our process, do NOT edit this _case file directly,
keep it as a working example.

In your custom project, copy this _case.py file and
append with _yourname.py instead.

Then edit your copied Python file to:
- inspect the JSON structure for your API,
- validate required keys and types,
- confirm the data is usable for your analysis.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from bs4 import BeautifulSoup
import re

# ============================================================
# Section 2. Define Run Validate Function
# ============================================================


def run_validate(
    LOG: logging.Logger,
    text_path
):
    headings = []
    pattern = r'^(?:\d+(?:\.\d+)?\s+(?=.*[A-Za-z]).+|Abstract|References)$'

    with open(text_path, "r", encoding="utf-8") as file:
        for line in file:
            if bool(re.match(pattern, line)):
                headings.append(line)

    cleaned_headings = [text.replace("\n", "") for text in headings]
    LOG.info(f"Returned headings: {cleaned_headings}")

    is_abstract = True if "Abstract" in cleaned_headings else None
    is_references = True if "References" in cleaned_headings else None

    missing = []
    if not is_abstract:
        missing.append("title")
    if not is_references:
        missing.append("authors")

    if missing:
        raise ValueError(
            f"VALIDATE: Required elements missing: {missing}. "
            "Page structure may have changed."
        )

    LOG.info("VALIDATE: HTML structure is valid.")

    return headings, cleaned_headings
