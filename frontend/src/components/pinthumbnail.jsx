import React from "react";
import { Link } from "react-router-dom";
import "../styles/pinthumbnail.css"; 

const PinThumbnail = ({ pin }) => {
  return (
    <Link to={`/art/${pin.id}`} className="pin-link">
      <div className="pin-card">
        <img
          src={pin.image_filename}
          alt={pin.title}
          className="pin-image"
        />
        <div className="pin-info">
          <h3 className="pin-title">{pin.title}</h3>
        </div>
      </div>
    </Link>
  );
};

export default PinThumbnail;
