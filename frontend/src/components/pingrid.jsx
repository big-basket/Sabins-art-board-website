import React from "react";
import PinThumbnail from "./pinthumbnail";

const PinGrid = ({ pins }) => {
  return (
    <div className="grid grid-cols-3 gap-4">
      {pins.map((pin) => (
        <PinThumbnail key={pin.id} pin={pin} />
      ))}
    </div>
  );
};

export default PinGrid;
