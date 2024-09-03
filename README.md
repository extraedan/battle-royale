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
