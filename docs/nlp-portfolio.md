# NLP Portfolio
This portfolio summarizes various skills learned and used in projects throughout the course.

## 1. NLP Techniques Implemented

### Tokenization
- **Converting text to tokens** by splitting on spaces, removing punctuation and leading spaces, removing stop words, and converting text to lowercase. ()[nlp-02-text-processing]
- **Frequency analysis** of individual tokens and bigrams using tables and histograms ()[nlp-03-text-exploration]
- **API-based text analysis (and JSON)** using X API to extract X posts and potterapi to gather a list of Harry Potter spells and their descriptions. 2nd and 4th projects
- **Web scraping / content extraction from HTML** using the Python Requests library to retrieve the HTML and Beautifulsoup for parsing. See ()[Project] for Wikipedia articles and ()[Project] for working with arxiv paper abstracts

## 2. Systems and Data Sources
Sources analyzed include the following:

### Web pages
- Used Python Requests library to fetch HTML
- Parsed HTML with BeautifulSoup library

### APIs
- Used Python Requests library to fetch JSON data

### Documents
- Utilized pypdf to extract text from PDF

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
Provide links to 2–3 of your strongest projects.

For each project:

include a clickable link
provide 1–2 sentences describing what it does and why it is representative

### X API Data Extraction and Analysis 
- Project 2

### PDF Parsing Pipeline
- Project 6

### 7. Skills
- Utilize many different APIs to retrieve data in JSON format
- Use Python Requests library for web scraping
- Parse returned data into tokens for analysis
- Generate visualizations for token frequency
- Communcate results via console logging and markdown text
