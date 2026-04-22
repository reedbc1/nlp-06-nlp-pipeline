# NLP Portfolio
This portfolio summarizes various skills learned and used in projects throughout the course.

## 1. NLP Techniques Implemented

- **Converting text to tokens** by splitting on spaces, removing punctuation and leading spaces, removing stop words, and converting text to lowercase. ([nlp-02-text-processing]())
- **Frequency analysis** of individual tokens and bigrams using tables and histograms. ([nlp-03-text-exploration]())
- **API-based text analysis (and JSON)** using X API to extract X posts and potterapi to gather a list of Harry Potter spells and their descriptions. 2nd and 4th projects
- **Web scraping / content extraction from HTML** using the Python Requests library to retrieve the HTML and Beautifulsoup for parsing. See [nlp-01-getting-started](https://github.com/reedbc1/nlp-01-getting-started) for Wikipedia articles and [nlp-05-web-documents](https://github.com/reedbc1/nlp-05-web-documents) for working with arxiv paper abstracts.

## 2. Systems and Data Sources
- **Fetched HTML** with Python Requests library
- **Parsed HTML** with BeautifulSoup library
- **Fetched JSON** from API endpoints
- **Extracted text from a PDF file** using pypdf

## 3. Pipeline Structure (EVTL)

- **Extract** - Fetch data from source
- **Validate** - Check that data structure is as expected
- **Transform** - Perform NLP processing steps, including tokenization and finding token counts
- **Load (to sink)** - Create outputs, inlcuding csv file of transformed data and image files containing graphs (histogram, word cloud)

## 4. Signals and Analysis Methods
- Word frequency: computed token totals to identify most common keywords in corpus
- Co-occurrence (bigrams): found most common repeating pairs of words, giving more information about context

## 5. Insights
Describe what your analysis revealed:
- Frequency from X API of the word "you"
- Frequency from word cloud for abstract of arxiv paper

## 6. Representative Work

### [X API Data Extraction and Analysis](https://github.com/reedbc1/nlp-02-text-preprocessing)
Uses the X API to capture most recent tweets that contain "AI" and identifies tokens with the highest frequency.

### [PDF Parsing Pipeline](https://github.com/reedbc1/nlp-06-nlp-pipeline)
Modified an existing pipeline to take PDFs from arxiv as the input. Headings are parsed to divide the paper by headings so that frequencies for different sections can be compared.

### 7. Skills
- Utilize different APIs to retrieve data in JSON format
- Use Python Requests library for web scraping
- Parse returned data into tokens for analysis
- Generate visualizations for token frequency
- Communcate results via console logging and markdown text
