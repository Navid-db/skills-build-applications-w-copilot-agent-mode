import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log('Fetching workouts from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><p>Loading workouts...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Personalized Workouts</h2>
      <div className="row">
        {workouts.length === 0 ? (
          <div className="col-12">
            <p>No workouts available</p>
          </div>
        ) : (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 col-lg-4 mb-3">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{workout.name || workout.title || 'Workout'}</h5>
                  <p className="card-text">
                    <strong>Type:</strong> {workout.workout_type || workout.type || 'N/A'}
                  </p>
                  <p className="card-text">
                    <strong>Duration:</strong> {workout.duration || 0} minutes
                  </p>
                  <p className="card-text">
                    <strong>Difficulty:</strong> {workout.difficulty || 'N/A'}
                  </p>
                  <p className="card-text">
                    <strong>Description:</strong> {workout.description || 'No description'}
                  </p>
                  {workout.suggested_for && (
                    <p className="card-text">
                      <small className="text-muted">Suggested for: {workout.suggested_for}</small>
                    </p>
                  )}
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Workouts;
