import React from "react";
import { Link } from "react-router-dom";

const PinThumbnail = ({ pin }) => {
  return (
    <Link to={`/art/${pin.id}`} style={{ textDecoration: "none", color: "inherit" }}>
      <div className="bg-white shadow-lg rounded-lg overflow-hidden cursor-pointer">
        <img
          src={pin.image_filename}
          alt={pin.title}
          className="w-full h-48 object-cover"
        />
        <div className="p-3">
          <h3 className="text-lg font-semibold">{pin.title}</h3>
        </div>
      </div>
    </Link>
  );
};

export default PinThumbnail;
