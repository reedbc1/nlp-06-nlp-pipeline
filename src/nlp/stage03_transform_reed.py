"""
stage03_transform_case.py
(EDIT YOUR COPY OF THIS FILE)

Source: validated BeautifulSoup object
Sink:   analysis-ready Pandas DataFrame

NOTE: We use Pandas for consistency with Module 5.
You may use Polars or another library if you prefer.
The pipeline pattern is identical; only the DataFrame API differs.

======================================================================
THE ANALYST WORKFLOW: Transform is not a single step
======================================================================

In a real NLP project, Transform is an iterative loop, not a
linear sequence of operations.

The loop looks like this:

  inspect → clean → inspect → engineer → inspect → clean → repeat

We need to inspect the data to know what cleaning is needed.
We inspect the cleaner data and begin to engineer additional features.
We inspect again to see how the cleaning worked and do more as needed.

This loop continues until the data is analysis-ready,
meaning a model or analyst could use the data without being misled
by noise, inconsistency, or missing signal.

This transform module is the SETTLED VERSION of that loop.
It captures decisions that survived inspection.
It does not show the full iterative process.
You should run it, inspect the logged output at each substage,
and ask yourself:

  - Does this look cleaner than the previous step?
  - Is there still noise I should remove?
  - Am I losing signal I want to keep?
  - What derived features would help a model or analyst?

The answers often suggest more work and that increases value.
That's the analyst workflow in action.

======================================================================
MODERN LLM Tools
======================================================================

Modern LLM tools are powerful, but only as good as the data provided.

`Garbage in, garbage out` is not a cliche.
It's why good data analysts are still very much needed.

A valuable analyst is one who understands:
  - why text needs cleaning before analysis
  - what signal looks like vs what noise looks like
  - how to inspect, iterate, and improve data quality
  - how to document those decisions so they are reproducible

The goal in this stage is not just to produce a clean DataFrame.
The goal is to develop the judgment to know when a DataFrame
is ready for use, and to professionally document why choices were made.

Judgment is what makes an analyst irreplaceable.

======================================================================
THIS STAGE
======================================================================

This stage runs three substages, each logged separately:

  03a. Extract fields from the validated HTML into a raw DataFrame.
       Inspect: does the raw data look right?

  03b. Clean and normalize the text fields.
       Inspect: is the text cleaner? Did we lose anything we needed?

  03c. Engineer derived features (tokens, word count, frequency).
       Inspect: do the derived fields add signal for downstream analysis?

The final DataFrame is the settled result of these three passes.

======================================================================
PURPOSE AND ANALYTICAL QUESTIONS
======================================================================

Purpose

  Transform validated HTML into a clean, analysis-ready DataFrame.

Analytical Questions

  - What does the raw extracted text look like before cleaning?
  - What noise is present and how should it be removed?
  - What derived features would support NLP analysis?
  - How does the cleaned text differ from the raw text?
  - Is the DataFrame genuinely ready for downstream use?

======================================================================
NOTES
======================================================================

Following our process, do NOT edit this _case file directly.
Keep it as a working example.

In your custom project, copy this file and rename it
by appending _yourname.py.

Then edit your copy to:
  - inspect your own extracted text carefully
  - apply cleaning steps appropriate to the data
  - engineer features that support the analytical goals
  - document every decision with a comment explaining why
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
import re
import string

import pandas as pd
import spacy

# Load the spaCy English model.
# This model provides tokenization, stopword lists, and linguistic annotations.
# It must be downloaded once before use:
#   uv run python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# ============================================================
# Section 2. Define Helper Functions
# ============================================================


def _clean_text(text: str, nlp_model: spacy.language.Language) -> str:
    """Clean and normalize a text string for NLP analysis.

    Cleaning steps applied in order:
      1. Lowercase
      2. Remove punctuation
      3. Normalize whitespace
      4. Remove stopwords using spaCy

    Each step has a tradeoff documented below.

    Args:
        text (str): Raw text string to clean.
        nlp_model: Loaded spaCy language model.

    Returns:
        str: Cleaned text string.
    """
    # Step 1: Lowercase.
    # WHY: "The" and "the" are the same word for analysis purposes.
    # TRADEOFF: Proper nouns lose their case signal.
    text = text.lower()

    # Step 2: Remove punctuation.
    # str.maketrans creates a translation table that maps each punctuation
    # character to None (removes it).
    # WHY: Punctuation adds noise for frequency analysis.
    # TRADEOFF: Sentence boundary information is lost.
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Step 3: Normalize whitespace.
    # re.sub replaces one or more whitespace characters (\s+) with a single space.
    # WHY: Multiple spaces and newlines are artifacts of HTML extraction.
    text = re.sub(r"\s+", " ", text).strip()

    # Step 4: Remove stopwords using spaCy.
    # spaCy processes the text and returns a Doc object.
    # Each token has an is_stop attribute that is True for stopwords.
    # We keep only tokens that are not stopwords and not whitespace-only.
    # WHY: Common words (the, a, is) carry little semantic signal.
    # TRADEOFF: Some stopwords matter in certain contexts (e.g., "not").
    doc = nlp_model(text)
    text = " ".join(
        [token.text for token in doc if not token.is_stop and not token.is_space]
    )

    return text


# ============================================================
# Section 3. Define Run Transform Function
# ============================================================


def run_transform(
    LOG: logging.Logger, text_path, cleaned_text_path, headings, cleaned_headings
):

    # divide text into sections by header
    sections = {}
    for heading in cleaned_headings:
        sections[heading] = ""

    with open(text_path, encoding="utf-8") as file:
        i = 0
        start_adding = False
        max_idx = len(headings) - 1

        for line in file:
            if line == headings[0]:
                start_adding = True
            if start_adding:
                if i < max_idx:
                    if line == headings[i + 1]:
                        i += 1
                sections[cleaned_headings[i]] += line + " "

    # clean sections
    cleaned_sections = {}
    for key in sections.keys():
        cleaned_sections[key] = _clean_text(sections[key], nlp)

    df = pd.DataFrame([cleaned_sections])

    corpus = ""
    for key in sections:
        corpus += cleaned_sections[key]

    return df, corpus
