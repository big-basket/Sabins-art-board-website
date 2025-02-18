import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import PinGrid from '../components/pingrid';

export default function HomePage() {
  const [pins, setPins] = useState([]);
  useEffect(() => {
      axios.get("/api/artpins")
          .then(response => {
              setPins(response.data);  
              console.log(response.data);
          })
          .catch(error => console.error("Error fetching pins:", error));
  }, []);
  return (
    <div>
        <h1>Home Page</h1>
        <PinGrid pins={pins} /> 
    </div>
  );
}