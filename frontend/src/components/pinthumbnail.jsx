import React from "react";

const PinThumbnail = ({ pin }) => {
  return (
    <div className="bg-white shadow-lg rounded-lg overflow-hidden">
      <img
        src={pin.image_location}
        alt={pin.title}
        className="w-full h-48 object-cover"
      />
      <div className="p-3">
        <h3 className="text-lg font-semibold">{pin.title}</h3>
      </div>
    </div>
  );
};

export default PinThumbnail;
