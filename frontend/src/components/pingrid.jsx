import React from "react";
import PinThumbnail from "./pinthumbnail";
import "../styles/pingrid.css"; 

const PinGrid = ({ pins }) => {
  return (
    <div className="pin-grid">
      {pins.map((pin) => (
        <PinThumbnail key={pin.id} pin={pin} />
      ))}
    </div>
  );
};

export default PinGrid;
