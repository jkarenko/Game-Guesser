# Game Riddler
## A game that tests your knowledge of games

### Requirements
- Python 3.6+
- OpenAI API key

### Install and run
1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Go to [OpenAI](https://platform.openai.com/) and create an account
4. Create a new API key in [API keys](https://platform.openai.com/account/api-keys)
5. Copy the API key 
6. Set the API key as an environment variable
   1. On Windows
      1. press `Win + R` and type `cmd`
      2. Type `setx OPENAI_API_KEY <your_api_key>`
      3. Press `Enter`
   2. On Linux and macOS
      1. Open a terminal
      2. Type `export OPENAI_API_KEY=<your_api_key>`
      3. Press `Enter`

### How to play
1. Run `python game-riddler.py`
2. Wait for game to formulate a riddle
3. Type your answer when asked

### How to add questions
1. Open `games.txt`
2. Add a new game name as a new line

### To do
- [ ] Add localisations
- [ ] Add more riddle difficulties
- [ ] Add more riddle categories
- [ ] Add more riddle styles
