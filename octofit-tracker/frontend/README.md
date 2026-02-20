# OctoFit Tracker Frontend

React frontend for the OctoFit Tracker fitness application.

## Setup

1. **Set up environment variables**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and replace `your-codespace-name-here` with your actual Codespace name. You can find this in your Codespace URL.

2. **Install dependencies**
   
   Dependencies should already be installed. If not, run:
   ```bash
   npm install
   ```

## Running the Application

Start the development server:
```bash
npm start
```

The app will open at `http://localhost:3000`

## Features

- **Activities**: View and track all fitness activities
- **Leaderboard**: See competitive rankings
- **Teams**: Manage and view team information
- **Users**: Browse user profiles
- **Workouts**: Access personalized workout suggestions

## API Integration

The frontend connects to the Django REST API backend running on port 8000. All components:
- Log fetched data to the console for debugging
- Support both paginated (`.results`) and plain array responses
- Use the environment variable `REACT_APP_CODESPACE_NAME` to construct API URLs

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production
- `npm run eject` - Ejects from Create React App (one-way operation)

## Technologies Used

- React 19
- React Router DOM 7
- Bootstrap 5
- React Scripts 5
