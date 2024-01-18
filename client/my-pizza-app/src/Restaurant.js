import React, { useState, useEffect } from 'react';

const apiUrl = 'http://127.0.0.1:5555';

function Restaurant({ id, name }) {
  const [details, setDetails] = useState('');
  const [showDetails, setShowDetails] = useState(true);


  useEffect(() => {
    fetch(`${apiUrl}`)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setDetails(data.details);
      });
  }, [id]);

  const toggleDetails = () => {
    setShowDetails(!showDetails);
  };

  return (
    <div onClick={toggleDetails}>
      <h3>{name}</h3>
      {showDetails && <p>{details}</p>}
    </div>
  );
}

export default Restaurant;