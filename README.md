# Junior ML Engineer Test – Translation Service

This project implements a backend service using FastAPI that is designed to:

- Store translation pairs
- Generate translation prompts based on similarity search
- (Advanced) Detect stammering in translated text

The application demonstrates both basic and advanced features as per the test requirements.

## Features

- **Translation Pair Storage:**  
  A `POST /pairs` endpoint to receive and store translation pairs in an in-memory database.

- **Translation Prompt Generation:**  
  A `GET /prompt` endpoint that accepts a query sentence plus source and target language parameters. It performs a similarity search among the stored translation pairs and returns a prompt message containing similar translation examples.  
  If no examples are found for the specified language pair, a fallback prompt is returned instead of a 404.

- **Stammering Detection (Advanced):**  
  A `GET /stammering` endpoint that analyzes a translated sentence for non-natural repetition (stammering) and returns a boolean value indicating whether stammering was detected.

## Technology Stack

- **Language:** Python 3.x  
- **Framework:** FastAPI  
- **Server:** Uvicorn  
- **Libraries:** NumPy, scikit-learn (cosine similarity), Pydantic

## Setup Instructions

### Prerequisites

- Python 3.x installed
- (Recommended) Virtual Environment tool (e.g., `venv`)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone <your-repository-url>
   cd <your-repository-directory>
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate    # For Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install fastapi uvicorn numpy scikit-learn pydantic
   ```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

### POST /pairs

- **Description:** Stores a translation pair.
- **Input (JSON):**  
  - `source_language` (string): ISO 639-1 code (e.g., "en")
  - `target_language` (string): ISO 639-1 code (e.g., "it")
  - `sentence` (string): Sentence in the source language.
  - `translation` (string): The translated sentence.
- **Response:**  
  ```json
  { "status": "ok" }
  ```

### GET /prompt

- **Description:**  
  Retrieves a translation prompt for a given query sentence by searching for similar translation pairs.
- **Input (Query Parameters):**  
  - `source_language` (string)
  - `target_language` (string)
  - `query_sentence` (string)
- **Response:**  
  Returns a JSON object with a `prompt` key. If there are no sample translations available for the specified language pair, the prompt will indicate that no examples are available.

### GET /stammering

- **Description:**  
  Analyzes a translated sentence for stammering (non-natural repetition).
- **Input (Query Parameters):**  
  - `source_sentence` (string): The original sentence.
  - `translated_sentence` (string): The translated sentence.
- **Response:**  
  ```json
  { "has_stammer": true | false }
  ```
  The response indicates whether stammering is detected.

## Testing the Application

A client script (`client.py`) is provided to help you test the API. The script uses three JSONL files:

- **translation_pairs.jsonl:** Translation pairs for the `/pairs` endpoint.
- **translation_requests.jsonl:** Prompt requests for the `/prompt` endpoint.
- **stammering_tests.jsonl:** Test cases for the `/stammering` endpoint.

### To Run the Client Script:

1. **Ensure the Server is Running:**

   Make sure your FastAPI server is running locally.

2. **Run the Client Script:**

   ```bash
   python client.py
   ```

3. **Follow the On-Screen Prompts:**

   The script displays a menu with these options:
   - **1 - Populate Database:** Uploads translation pairs.
   - **2 - Request Prompts:** Sends queries to generate translation prompts.
   - **3 - Detect Stammering:** Tests the stammering detection endpoint.
   - **4 - Exit**

---

## Captured Client Script Output

Below is a sample output captured from running the client script:

```
Select an option:
1 - Populate Database
2 - Request Prompts
3 - Detect Stammering
4 - Exit
Enter choice (1-4): 1
Line 1: Added translation pair.
Line 2: Added translation pair.
Line 3: Added translation pair.
Line 4: Added translation pair.
Line 5: Added translation pair.
Line 6: Added translation pair.
Line 7: Added translation pair.
Line 8: Added translation pair.
Line 9: Added translation pair.
Line 10: Added translation pair.
Line 11: Added translation pair.
Line 12: Added translation pair.
Line 13: Added translation pair.
Line 14: Added translation pair.
Line 15: Added translation pair.
Line 16: Added translation pair.
Line 17: Added translation pair.
Line 18: Added translation pair.
Line 19: Added translation pair.
Line 20: Added translation pair.

Select an option:
1 - Populate Database
2 - Request Prompts
3 - Detect Stammering
4 - Exit
Enter choice (1-4): 2

Line 1: Received Translation Prompt.
Please translate the following sentence from en to it:
'Good night'

Here are some sample translations for reference:
1. Good morning!  -->  Buongiorno!
2. Good evening!  -->  Buonasera!
3. I love Italian food.  -->  Amo il cibo italiano.
4. Do you speak English?  -->  Parli inglese?

Line 2: Received Translation Prompt.
Please translate the following sentence from en to it:
'Good evening!'

Here are some sample translations for reference:
1. Good evening!  -->  Buonasera!
2. Good morning!  -->  Buongiorno!
3. Do you speak English?  -->  Parli inglese?
4. See you soon.  -->  A presto.

Line 3: Received Translation Prompt.
Please translate the following sentence from en to it:
'How's the weather tomorrow?'

Here are some sample translations for reference:
1. How's the weather today?  -->  Com'è il tempo oggi?
2. How's the weather?  -->  Com'è il tempo?
3. See you tomorrow.  -->  Ci vediamo domani.
4. Where are you from?  -->  Di dove sei?

Line 4: Received Translation Prompt.
Please translate the following sentence from en to it:
'How's your day?'

Here are some sample translations for reference:
1. What's your name?  -->  Come ti chiami?
2. Hello, how are you?  -->  Ciao, come stai?
3. See you tomorrow.  -->  Ci vediamo domani.
4. Do you speak English?  -->  Parli inglese?

Line 5: Received Translation Prompt.
Please translate the following sentence from en to it:
'See you later, my friend.'

Here are some sample translations for reference:
1. See you later.  -->  Ci vediamo dopo.
2. Where are you from?  -->  Di dove sei?
3. Where is the nearest station?  -->  Dov'è la stazione più vicina?
4. Do you speak English?  -->  Parli inglese?

Line 6: Received Translation Prompt.
Please translate the following sentence from en to it:
'What's my name?'

Here are some sample translations for reference:
1. What's your name?  -->  Come ti chiami?
2. What is the time?  -->  Che ore sono?
3. How's the weather today?  -->  Com'è il tempo oggi?
4. Where is the nearest station?  -->  Dov'è la stazione più vicina?

Line 7: Received Translation Prompt.
Please translate the following sentence from en to it:
'What's your hometown?'

Here are some sample translations for reference:
1. What's your name?  -->  Come ti chiami?
2. How's the weather today?  -->  Com'è il tempo oggi?
3. See you tomorrow.  -->  Ci vediamo domani.
4. How's the weather?  -->  Com'è il tempo?

Line 8: Received Translation Prompt.
Please translate the following sentence from en to it:
'Where is the bus stop?'

Here are some sample translations for reference:
1. Where is the station?  -->  Dov'è la stazione?
2. Where is the nearest station?  -->  Dov'è la stazione più vicina?
3. How's the weather?  -->  Com'è il tempo?
4. How's the weather today?  -->  Com'è il tempo oggi?

Line 9: Received Translation Prompt.
Please translate the following sentence from en to it:
'I love pizza and I love italian food in general.'

Here are some sample translations for reference:
1. I love Italian food.  -->  Amo il cibo italiano.
2. Do you speak Italian?  -->  Parli italiano?
3. I love pizza.  -->  Amo la pizza.
4. Good evening!  -->  Buonasera!

Line 10: Received Translation Prompt.
Please translate the following sentence from en to it:
'I love music.'

Here are some sample translations for reference:
1. I love Italian food.  -->  Amo il cibo italiano.
2. I love pizza.  -->  Amo la pizza.
3. Do you speak English?  -->  Parli inglese?
4. Do you speak Italian?  -->  Parli italiano?

Line 11: Received Translation Prompt.
Please translate the following sentence from en to it:
'Do you understand Italian?'

Here are some sample translations for reference:
1. Do you speak Italian?  -->  Parli italiano?
2. I love Italian food.  -->  Amo il cibo italiano.
3. What's your name?  -->  Come ti chiami?
4. Do you speak English?  -->  Parli inglese?

Line 12: Received Translation Prompt.
Please translate the following sentence from en to it:
'Do you speak German or Italian?'

Here are some sample translations for reference:
1. Do you speak Italian?  -->  Parli italiano?
2. What's your name?  -->  Come ti chiami?
3. Do you speak English?  -->  Parli inglese?
4. I love Italian food.  -->  Amo il cibo italiano.

Line 13: Received Translation Prompt.
Please translate the following sentence from en to it:
'What time does the train leave?'

Here are some sample translations for reference:
1. Where is the nearest station?  -->  Dov'è la stazione più vicina?
2. Where is the station?  -->  Dov'è la stazione?
3. What is the time?  -->  Che ore sono?
4. How's the weather today?  -->  Com'è il tempo oggi?

Line 14: Received Translation Prompt.
Please translate the following sentence from en to it:
'I'm feeling hungry now.'

Here are some sample translations for reference:
1. I'm hungry.  -->  Ho fame.
2. Good evening!  -->  Buonasera!
3. Good morning!  -->  Buongiorno!
4. Do you speak English?  -->  Parli inglese?

Line 15: Received Translation Prompt.
Please translate the following sentence from en to it:
'Is there a library nearby?'

Here are some sample translations for reference:
1. Where is the nearest station?  -->  Dov'è la stazione più vicina?
2. See you later.  -->  Ci vediamo dopo.
3. Where are you from?  -->  Di dove sei?
4. What's your name?  -->  Come ti chiami?

Line 16: Received Translation Prompt.
Please translate the following sentence from en to it:
'Can you help me find the park?'

Here are some sample translations for reference:
1. Do you speak English?  -->  Parli inglese?
2. Do you speak Italian?  -->  Parli italiano?
3. What's your name?  -->  Come ti chiami?
4. Where is the nearest station?  -->  Dov'è la stazione più vicina?

Line 17: Received Translation Prompt.
Please translate the following sentence from it to en:
'Che ore sono?'

No sample translations available.

Line 18: Received Translation Prompt.
Please translate the following sentence from it to en:
'Ci vediamo'

No sample translations available.

Select an option:
1 - Populate Database
2 - Request Prompts
3 - Detect Stammering
4 - Exit
Enter choice (1-4): 3

Line 1: Response -> No (Expected: No)

Line 2: Response -> No (Expected: No)

Line 3: Response -> Yes (Expected: Yes)

Line 4: Response -> No (Expected: No)

Line 5: Response -> No (Expected: No)

Line 6: Response -> No (Expected: No)

Line 7: Response -> No (Expected: No)

Line 8: Response -> No (Expected: No)

Line 9: Response -> No (Expected: No)

Line 10: Response -> Yes (Expected: Yes)

Line 11: Response -> Yes (Expected: Yes)

Line 12: Response -> Yes (Expected: Yes)
```

---

## Code Organization

- **main.py:** Contains the FastAPI application, endpoints, and helper functions (e.g., compute_embedding, detect_stammering).
- **client.py:** The testing client script.
- **JSONL Files:**  
  - `translation_pairs.jsonl`
  - `translation_requests.jsonl`
  - `stammering_tests.jsonl`

