# battle-royale

## Development Log

### 2024-08-31 - Character Creation and Editing
- **Implemented**: Add and edit functionality for game characters
- **Challenges**: Resolved issues with form fields retaining previously submitted data
- **Learned**: 
  - Created multiple form instances for individual character editing
  - Implemented Post/Redirect/Get pattern to refresh forms after submission
- **Next Steps**: Begin implementing core battle royale mechanics, focusing on creating a Minimum Viable Product (MVP) before adding additional features like beautification and character images

### 2024-09-01 - Creating the MVP
- **Implemented**: Basic gameplay loop in which events are generated and displayed for each character, and deaths are tracked, it is now a working 'simulator'
- **Challenges**: Struggled with 'tagging' each event to indicate whether it includes a character death or not
- **Learned**: 
  - Resolved the event tagging issue by using objects to track attributes
  - Created events as a list of tuples, making it easier to manage and process event information
  - This approach allowed for more efficient tracking of event details, including character deaths
- **Next Steps**:
  - Implement AI-generated events to replace premade ones, enhancing game variety
  - Consider basic UI improvements using Bootstrap for better visual appeal
  - Explore adding small features to enrich gameplay experience

### 2024-09-03 - Involving AI
- **Implemented**: Added AI generated events that consider character health and items
- **Challenges**: Inconsistant events generated by LLM, often creates issues with rounds
- **Learned**: 
  - Using Anthropic's API to send and recieve data
- **Next Steps**:
  - Implement a three strike system that checks for valid outputs from LLM
  - Adjust system prompt for higher quality responses OR upgrade to higher quality model (current model Haiku, upgraded is Sonnet 3.5)
  - Making sure events are definitive and not open ended so that the game flows as intended

### 2024-09-05 - Refactoring
- **Implemented**: Completely seperated concerns, moving logic and routes into seperate files, made efforts to make the code as modular as possible
- **Learned**: 
  - Gamestate class is useful, instead of passing in characters, round numbers and more, I can pass in the 'game' object of GameState class where I can track all values and render them in my template as needed
- **Next Steps**:
  - System prompt still needs to be adjusted
  - Need to start adjusting quality of life, making the game replayable, adding images of characters
  - Use BrantSteele's Hunger Games as reference for what quality of life features to add
