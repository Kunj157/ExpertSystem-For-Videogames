# Play-Smart: Video Game Expert System

Play-Smart is a professional-grade expert system designed to provide end-to-end video game recommendations based on a comprehensive dataset of over 16,000 titles. It leverages a rule-based engine to filter games across multiple dimensions, including platform, genre, release year, and critical/user reception.

## 🚀 Overview
The system provides a graphical user interface (GUI) that allows users to define their gaming preferences. By applying expert rules to the `Video_Games_Sales.csv` dataset, it identifies and presents games that match the user's specific criteria.

## ✨ Key Features
- **Dynamic Filtering**: Narrow down your search by:
  - **Platform**: Support for dozens of consoles (e.g., PS4, Wii, X360, PC, etc.).
  - **Genre**: Filter by Action, Sports, RPG, Strategy, and more.
  - **Year Range**: Define a specific era of gaming (e.g., 2000 to 2015).
  - **Reception Scores**: Set minimum thresholds for both Critic Scores (0-100) and User Scores (0-10).
  - **ESRB Ratings**: Select specific age ratings (E, T, M, etc.) using interactive checkboxes.
- **Interactive Navigation**: Seamlessly browse through matching results using 'Next' and 'Previous' controls.
- **Detailed Analytics**: Each result displays comprehensive data, including Developer, Global Sales, and precise rating details.
- **Real-time Processing**: Fast data loading and filtering using the Pandas library.

## 🛠️ Technology Stack
- **Language**: Python 3
- **Data Processing**: Pandas
- **GUI Framework**: Tkinter
- **Dataset**: Video Games Sales with Ratings (CSV)

## 📂 File Structure
- `expert.py`: The main entry point. Orchestrates the Tkinter GUI and coordinates between the data and evaluation layers.
- `VideoGame.py`: Defines the `VideoGame` class, which transforms raw dataset rows into structured objects.
- `ActionData.py`: Handles data persistence, CSV loading, and manages the state of the current search results.
- `Evaluation.py`: The heart of the expert system. Contains the `Evaluation` class which implements the logic for "qualifying" a game based on user-defined rules.
- `Video_Games_Sales.csv`: The source dataset containing game metadata and performance metrics.

## 🏁 How to Run

### Prerequisites
Ensure you have Python 3 and Pandas installed:
```bash
pip install pandas
```

### Execution Steps
1. **Launch the Application**:
   ```bash
   python3 expert.py
   ```
2. **Load the Dataset**: 
   Upon startup, a file dialog will appear. Select the `Video_Games_Sales.csv` file located in the project root.
3. **Configure Preferences**:
   Use the dropdowns, sliders, and checkboxes to set your desired game attributes.
4. **Search**:
   Click the **Submit** button to trigger the expert system's evaluation engine.
5. **Explore**:
   If matches are found, use the **Next** and **Prev** buttons to view the recommendations.

## 🧠 Expert System Logic (End-to-End)
1. **Data Ingestion**: The system reads the CSV and populates a list of `VideoGame` objects, sanitizing missing records (NaN) into a searchable state.
2. **Rule Definition**: User inputs are captured via the GUI and passed to the `Evaluation` agent.
3. **Filtering (Inference)**: The system iterates through the entire library, checking each game against the following boolean logic:
   - `Platform` and `Genre` match exactly.
   - `YearOfRelease` falls within the inclusive range $[lb, rb]$.
   - `CriticScore` $\ge$ minimum threshold.
   - `UserScore` $\ge$ minimum threshold.
   - `Rating` exists within the user's allowed set.
4. **Result Presentation**: Qualified games are sorted by release year (newest first) and presented in a detailed format within the result window.

---
*Enjoy finding your next favorite game with Play-Smart!* 🎮