# Suspicious Message Classifier

**README prose word count: 293**
## Project Overview and Status
An interactive Streamlit prototype exploring overreliance in human–AI decision-making. 
Users classify predefined messages, receive simulated AI recommendations, and make final decisions. 
Adaptive evidence-review prompts appear when the AI disagrees with the user or reports low confidence.

All interaction features are functional, but AI recommendations and confidence values are predefined. 
No trained AI model or user evaluation is included.

## Technology Stack

- **Python 3.14** — Application logic and decision workflow.
- **Streamlit 1.67.0** — User interface, session state and adaptive interventions.
- **JSON** — Storage of predefined messages, classifications and simulated AI confidence values.

No trained AI model, external API or database is used.

## Running the Prototype

**Requirements:** Python 3.14 and pip.

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Launch the application:

```bash
streamlit run app.py
```

The prototype will open in your web browser. 
Select a message and follow the on-screen steps to complete the interaction.

## Development Record

- **[Initial prototype](https://github.com/egeodabasi10/suspicious-message-classifier/commit/acced80911b33d418a3aa934a5609db3ffe1c714):** Created the Streamlit interface and configured project dependencies to establish the application's foundation.

- **[Message classification](https://github.com/egeodabasi10/suspicious-message-classifier/commit/7d9a3611c1b49226c358c8843016106ec92b149c):** Added three predefined messages and an initial judgement interface, allowing users to classify messages independently before viewing AI recommendations.

- **[Adaptive interventions and final decisions](https://github.com/egeodabasi10/suspicious-message-classifier/commit/a0c106abb3953e53783ef9bebb441b6d1963021a):** Implemented evidence-review prompts and final human decisions to encourage critical evaluation of AI recommendations while preserving user control.

Testing: Manually tested all three scenarios, intervention conditions, final decisions and reset functionality. 
A Streamlit session-state error affecting the reset function was identified and resolved using a button callback.

## AI Assistance

Generative AI (ChatGPT) was used for the following tasks:

- Checking and refining Python/Streamlit code and assisting with debugging.
- Spell-checking and shortening project documentation.

AI-assisted code changes were verified through manual testing of the application's interaction flow and reset functionality.

## Files

- `app.py` — Streamlit interface, decision workflow and adaptive intervention logic.
- `messages.json` — Predefined messages, intended classifications and simulated AI outputs.
- `requirements.txt` — Python dependencies.
- `README.md` — Project documentation and development record.