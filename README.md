# AI Travel Planner Readme

Welcome to the AI Travel Planner, your powerful assistant for planning efficient and well-organized trips within India. This AI assistant is designed to help you create personalized travel
itineraries based on your specified parameters.

## How to Use

1. **Getting Started:**
   - Ensure you have Python, Flask, LLMS, VectorDBs, and data scraping tools installed.
   - Clone the repository and install the necessary dependencies.

2. **Run the Application:**
   - Execute the command `python app.py` to start the Flask application.
   - Open your web browser and navigate to `http://localhost:5000` to access the AI Travel Planner.

3. **Input Parameters:**
   - Specify the number of days you have for the trip using the `{days}` parameter.
   - Provide the starting location with the `{start}` parameter.
   - Specify the destination location with the `{end}` parameter.
   - Choose the mode of travel with the `{mode}` parameter (e.g., "car," "train," "bus," etc.).

4. **Handling Empty or Incorrect Inputs:**
   - If the `{start}` or `{end}` parameters are empty, the AI assistant will prompt you to fill in the details properly.

5. **Travel Recommendations:**
   - Based on the provided parameters, the AI assistant will suggest an efficient travel plan.
   - It will recommend ways to travel based on the specified mode, providing Google Maps references for each leg of the journey.

6. **Place Descriptions:**
   - Each mentioned place will be accompanied by a one-word description in brackets for a quick overview.

7. **Public Transportation Details:**
   - If the chosen mode of travel is public transportation, the AI assistant will provide specific details in brackets, including relevant transportation information.

8. **Handling Unknowns:**
   - If the AI is unsure about public transportation details, it will suggest alternative modes like taking a taxi or bus without explicitly stating the lack of information.

## Technologies Used

- Python
- Flask
- LLMS (Language Model System)
- VectorDBs
- Data Scraping Tools

Feel free to customize and enhance the AI Travel Planner based on your requirements. Safe travels!
